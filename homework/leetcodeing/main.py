import sys
import asyncio

async def main():
    await asyncio.sleep(10)
    print('hello!')

asyncio.run(main())