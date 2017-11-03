# How to sort a Python dict by value
# (== get a representation sorted by value)

list_order = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

order_list = sorted(list_order.items(), key=lambda value: value[1])

print(order_list)

# OR

import operator

order_list_two = sorted(list_order.items(), key=operator.itemgetter(1))

print(order_list_two)
