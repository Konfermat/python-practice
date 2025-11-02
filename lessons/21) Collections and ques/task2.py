from collections import defaultdict
counter = defaultdict(int)

def group_products_bby_category(items):
    grouped_products = defaultdict(list)

    for category, products in items:
        grouped_products[category].append(products)

    return grouped_products

shopping_list = [
    ('фрукты', 'яблоко'),
    ('молочное', 'молоко'),
    ('овощи', 'помидор'),
    ('фрукты', 'виноград'),
    ('молочное', 'сыр')
]
for item in shopping_list:
    print(item)
result = group_products_bby_category(shopping_list)
# print(result)
for category, products in result.items():
    print(f'Категория: {category}')
    print(f'\tПродукты: {', '.join(products)}')


