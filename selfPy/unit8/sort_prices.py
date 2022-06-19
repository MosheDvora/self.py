products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]

def price(list_of_tuples):
    return list_of_tuples[1]

def sort_prices(list_of_tuples):
    sorted_products = []
    sorted_products = sorted(list_of_tuples, key=price, reverse=True)
    print(sorted_products)


sort_prices(products)




# sort_prices(products)