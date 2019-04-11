import asyncio
import random


async def my_other(id):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print(f"Coroutine {id}, has successfully completed after {process_time} seconds")


async def my_coroutine():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(my_other(i)))
    await asyncio.gather(*tasks)
    print("All done")


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(my_coroutine())
    finally:
        loop.close()


if __name__ == '__main__':
    main()
