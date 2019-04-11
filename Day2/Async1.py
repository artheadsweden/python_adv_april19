import asyncio


async def my_other():
    await asyncio.sleep(2)
    return "The message"


async def my_coroutine():
    print("Starting my_coroutine()")
    message = await my_other()
    print(message)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_coroutine())
    loop.close()


if __name__ == '__main__':
    main()
