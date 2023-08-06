"""
This module contains CLI handlers.

There is a handler function for each CLI subcommand.

All handlers/subcommands must support text and json outputs.
"""
import json
import asyncio
from typing import Optional, List

import requests

from .version import VERSION
from .download import DownloadManager
from .archive import ArchiveManager


def version(output: str = 'text') -> str:
    """
    Handler for the `version` subcommand.

    It jus shows the CLI version.
    """
    if output == 'text':
        return VERSION
    
    return json.dumps({'version': VERSION}, indent=4)


def download(years: str = '', dest: str = '', workers: Optional[int] = None, extract: bool = False,  output: str = 'text') -> str:
    """
    Handler for the `download` subcommand.

    It downloads archives from the ibov website, right now just yearly archives are supported.

    It will also extract the archives from the downloaded zipfiles if `extracted` is set to `True`.

    Return the list of download and extracted files.
    """
    results: List[str] = []
    
    loop = asyncio.get_event_loop()
    manager = DownloadManager(dest)
    urls = [f'http://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A{i}.ZIP' for i in years.split(',')]
    loop.run_until_complete(manager(urls, results, workers=workers))    

    if extract:
        manager1 = ArchiveManager(results, f'{dest}/extracted')
        loop.run_until_complete(manager1(results, workers=workers))

    results.sort()

    if output == 'text':
        return '\n'.join(results)
    return json.dumps({'files': results}, indent=4)

