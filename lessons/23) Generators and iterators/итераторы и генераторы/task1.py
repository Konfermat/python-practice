# 1
orders = ['кофе', 'чай', 'пирожное', 'сэндвич']
order_iter = iter(orders)
while True:
    try:
        order = next(order_iter)
        print(f'обрабатывается заказ {order}')
    except StopIteration:
        print('все заказы обработаны')
        break