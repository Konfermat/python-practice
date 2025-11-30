# import asyncio
# # event loop - цикл событий, который управляет корутин
# # coroutine (корутины) - асинхронные функции
# # tasks - объекты, которые представляют выполнение корутины
#
# # async def main():
# #     print('Hello')
# #     await asyncio.sleep(1) # приостанавливает, но не блокирует весь поток программы
# #     print('world')
# # asyncio.run(main()) # управляет жизненым циклом event loop
#
# # Event Loop работает в фоновом режиме
#
# async def task1():
#     print('task 1: start')
#     await asyncio.sleep(2)
#     print('task 1: end')
# async def task2():
#     print('task 2: start')
#     await asyncio.sleep(1)
#     print('task 2: end')
#
# async def main(): # создалии объект Task
#     t1 = asyncio.create_task(task1())
#     t2 = asyncio.create_task(task2())
#     # ждем завершение обеих задач
#     await t1
#     await t2
#
# # asyncio.run(main())
#
# # конкурентно запускают
#
# async def coroutine():
#     print('start')
#     await asyncio.sleep(1)
#     print('end')
#
# async def main():
#     t1 = asyncio.create_task(coroutine())
#     t2 = asyncio.create_task(coroutine())
#     await t1
#     await t2
# # asyncio.run(main())
#
# # Task
# # task.done() - проверяет завершение
# # task.result() - результат выполнения корутины (InvalidStateError)
# # task.cancel() - отменяет выполнене таски
# # task.exception() - возвращает исключение (з коорутины)
#
# async def coroutine():
#     print('start')
#     await asyncio.sleep(1)
#     print('end')
#     return 'done'
#
# async def main():
#     t1 = asyncio.create_task(coroutine())
#     print(t1.done())
#     # t2 = asyncio.create_task(coroutine())
#     await t1
#     print(t1.result())
#     print(t1.done())
#     # await t2
# asyncio.run(main())
#

import asyncio

async def fetch_data(task_id, delay):
    print(f'Task {task_id} started')
    await asyncio.sleep(delay)
    print(f'Task {task_id} finished')
    return f'Data from task {task_id}'

async def main():
    tasks = [
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3)
    ]
    results = await asyncio.gather(*tasks) # сбор
    print('all tasks finished')
    print(f'results: {results}')
asyncio.run(main())