from typing import Optional, Tuple, List, Any, Callable
import asyncio
from numpy import linspace
from collections import namedtuple


from Orange.misc.server_embedder import ServerEmbedderCommunicator
from orangecontrib.dicom.utils.embedder_utils import ImageLoader
from Orange.util import dummy_callback

from httpx import AsyncClient
from Orange.misc.utils.embedder_utils import get_proxies

TaskItem = namedtuple("TaskItem", ("id", "item", "no_repeats"))

class ServerEmbedder(ServerEmbedderCommunicator):
    def __init__(
        self,
        model_name: str,
        max_parallel_requests: int,
        server_url: str,
        embbedder_type: str,
        image_size: Tuple[int, int],
    ) -> None:
        super().__init__(
            model_name, max_parallel_requests, server_url, embbedder_type
        )
        self.content_type = "image/jpeg"
        self.image_size = image_size
        self._image_loader = ImageLoader()

    async def _encode_data_instance(self, file_path_frame: List[Any]) -> Optional[bytes]:
        return self._image_loader.load_image_bytes(
            file_path_frame[0], file_path_frame[1], self.image_size)

    def embedd_data(
        self,
        data: List[Any],
        *,
        callback: Callable = dummy_callback,
    ) -> List[Optional[List[float]]]:
        """
        This function repeats calling embedding function until all items
        are embedded. It prevents skipped items due to network issues.
        The process is repeated for each item maximally MAX_REPEATS times.

        Parameters
        ----------
        data
            List with data that needs to be embedded.
        callback
            Callback for reporting the progress in share of embedded items

        Returns
        -------
        List of float list (embeddings) for successfully embedded
        items and Nones for skipped items.

        Raises
        ------
        EmbeddingConnectionError
            Error which indicate that the embedding is not possible due to
            connection error.
        EmbeddingCancelledException:
            If cancelled attribute is set to True (default=False).
        """
        # if there is less items than 10 connection error should be raised earlier
        self.max_errors = min(len(data) * self.MAX_REPEATS, 10)

        return asyncio.run(
            self.embedd_batch(data, callback=callback)
        )
    
    async def embedd_batch(
        self,
        data: List[Any],
        *,
        callback: Callable = dummy_callback,
    ) -> List[Optional[List[float]]]:
        """
        Function perform embedding of a batch of data items.

        Parameters
        ----------
        data
            A list of data that must be embedded.
        callback
            Callback for reporting the progress in share of embedded items

        Returns
        -------
        List of float list (embeddings) for successfully embedded
        items and Nones for skipped items.

        Raises
        ------
        EmbeddingCancelledException:
            If cancelled attribute is set to True (default=False).
        """
        progress_items = iter(linspace(0, 1, len(data)))

        def success_callback():
            """Callback called on every successful embedding"""
            callback(next(progress_items))

        results = [None] * len(data)
        queue = asyncio.Queue()

        # fill the queue with items to embedd
        for i, item in enumerate(data):
            queue.put_nowait(TaskItem(id=i, item=item, no_repeats=0))

        async with AsyncClient(
            timeout=self.timeout, base_url=self.server_url, proxies=get_proxies()
        ) as client:
            tasks = self._init_workers(client, queue, results, success_callback)

            try:
                # wait for workers to stop - they stop when queue is empty
                # if one worker raises exception wait will raise it further
                await asyncio.gather(*tasks)
            finally:
                await self._cancel_workers(tasks)
                self._cache.persist_cache()

        return results