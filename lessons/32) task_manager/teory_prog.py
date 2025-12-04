# Pool
import multiprocessing
# apply() - блокируетосновной процесс до завеуршения задачи
# apply_async() - ассинхронно, возвращает объект AsyncResult
# map()
# map_async() - возвращает, объект AsssyncResult
# startmap() аналог map() ринимает несколько аргументов в виде кортежа

from multiprocessing import Pool
import time



def square(n):
    time.sleep(1)
    return n ** 2


# apply_async()
# if __name__ == '__main__':
#     with Pool(processes=4) as p:
#         # AsyncResult
#         # results = []
#         # for i in range(1, 6):
#         #     async_res = p.apply_async(square, args=)
#         #     results.append(async_res)
#         # for i, res in enumerate(results, 1):
#         #     print(f'{i}: {res.get()}')
#
#         # map_async()
#         nums = list(range(1, 11))
#         async_result = p.map_async(square, nums)
#         print('запущены. делаем что- другое')
#         time.sleep(0.7)
#         print('проверяем готовность')
#         # метод ready проверка готовности
#         # будет вызываться от AsyncResult
#         print(f'{async_result.ready()} (результаты готовы?)')
#         try:
#             results = async_result.get(timeout=2)
#             print(results)
#         except multiprocessing.TimeoutError:
#             print('время ожидания истекло')

# if __name__ == '__main__':
#     # контекстный менеджер
#     with Pool(processes=4) as p:
#         result1 = p.apply(square, args=(5,))
#         print(result1)
#         result2 = p.apply(square, args=(10,))
#         print(result2)

    #     nums = [1, 2, 3, 4, 5, 6, 7, 8]
    #     results = p.map(square, nums)
    # print(results)

def power(base, exponent):
    return base ** exponent

if __name__ == '__main__':
    with Pool(processes=4) as p:
        arguments = [(2, 2), (3, 3), (4, 2), (5, 3)]
        results = p.starmap(power, arguments)
        print(results)



