"""
This module contains classes and functions to deal with ibov archive downloads.
"""
import asyncio
import concurrent.futures
from typing import Optional, List

import requests


class DownloadManager:
    def __init__(self, dest: str) -> None:
        self.loop = asyncio.get_event_loop()
        self.dest = dest

    def _fetch(self, url: str, dest: str, results: List[str]) -> None:
        """
        Downloads an archive from an url and writes it to the `dest` path (absolute path).
        
        It also appends `dest` to `results`.
        """
        with requests.get(url, stream=True) as s:
            with open(dest, 'wb') as f:
                for chunk in s.iter_content(chunk_size=8192):
                    f.write(chunk)
        results.append(dest)
    
    async def __call__(self, urls: List[str], results: List[str], workers: Optional[int] = None) -> None:
        """
        Async call that downloads all archives by invoking `self._fetch` in a pool.

        It will spawn a worker per url if `workers` is not provided.
        """
        if workers is None:
            workers = len(urls)
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            for url in urls:
                fname = url.split('/')[-1]
                self.loop.run_in_executor(
                    executor,
                    self._fetch,
                    url,
                    f'{self.dest}/{fname}',
                    results
                )

