from __future__ import annotations

import asyncio
import re
from tqdm import tqdm
from typing import Callable


async def concurrent(n, *coros):
    semaphore = asyncio.Semaphore(n)
    progress_bar = tqdm(total=len(coros))

    async def sem_coro(coro):
        async with semaphore:
            result = await coro
            progress_bar.update(1)
            return result

    results = await asyncio.gather(*(sem_coro(c) for c in coros))
    progress_bar.close()
    return results


def replace_with_correction(
        text: str,
        correction: dict[str, str],
        replace_func: Callable[[str, str], str] = lambda _, y: y,
):
    match_regex = re.compile('(' + "|".join(re.escape(m) for m in correction) + ')')
    parts = re.split(match_regex, text)
    return ''.join([
        replace_func(p, correction[p])
        if p in correction else p for p in parts
    ])
