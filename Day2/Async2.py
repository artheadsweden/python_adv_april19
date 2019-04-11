import asyncio


async def my_other(future):
    await asyncio.sleep(1)
    future.set_result("The future is here. Here it is")


async def my_coroutine():
    future = asyncio.Future()
    await asyncio.ensure_future(my_other(future))
    print(future.result())


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(my_coroutine())
    finally:
        loop.close()


if __name__ == '__main__':
    main()
