import asyncio

users = [("Alice", 2), ("Bob", 3), ("Charlie", 1), ("Diana", 4)]
tasks = []

async def send_email(recipient, delay):
    print(f'{recipient} отправил письмо.')
    await asyncio.sleep(delay)
    print(f'Письмо от {recipient} доставлено.')

async def main():
    for i in users:
        tasks.append(asyncio.create_task(send_email(i[0], i[1])))

    for task in tasks:
        await task

asyncio.run(main())