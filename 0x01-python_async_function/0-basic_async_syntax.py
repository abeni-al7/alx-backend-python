#!/usr/bin/env python3
'''A module for delaying the execution of code asynchronously'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait