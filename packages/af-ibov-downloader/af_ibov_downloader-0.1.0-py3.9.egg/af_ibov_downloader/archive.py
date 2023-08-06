"""
this module contains classes and utilities to deal with ibov archives.
"""
import os
from zipfile import ZipFile
import asyncio
import concurrent.futures
from typing import Optional, List


class ArchiveManager:
    """
    Archive manager class.

    This class reads a dir of archives in zip format and
    extracts all of its members to `{self.dest}/extracted`
    """
    def __init__(self, results: List[str], dest: str) -> None:
        self.loop = asyncio.get_event_loop()
        self.results = results
        self.dest = dest

    def _extract(self, src: str, dest: str) -> None:
        """
        Extract the content of a zifile located at "src" to "dest".

        All members will be extracted.
        """
        with ZipFile(src, 'r') as z:
            z.extractall(path=dest)

    async def __call__(self, paths: List[str], workers: Optional[int] = None) -> None:
        """
        Run `self.extract` on an executor.

        It will create one worker per element in path if `workers` is not provided.
        """
        if workers is None:
            workers = len(paths)
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            for path in paths:
                self.loop.run_in_executor(
                    executor,
                    self._extract,
                    path,
                    self.dest
                )
        self.results += [f'{self.dest}/{f}' for f in os.listdir(self.dest)]



