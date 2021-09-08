# Список товаров
goods = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

# Множества для добавления (чтобы не было дубликатов)
products = set([])
prices = set([])
qty = set([])
values = set([])

for el in goods:
    single_product = el[1]
    for key in single_product:
        products.add(single_product.get("название"))
        prices.add(single_product.get("цена"))
        qty.add(single_product.get("количество"))
        values.add(single_product.get("eд"))

result_dictionary = {
    "название": products,
    "цена": prices,
    "количество": qty,
    "ед": values,
}
print(result_dictionary)
