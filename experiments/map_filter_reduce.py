
from functools import reduce


data = [1, 2, 3, 4, 5, 6, 7]

data_increased = list(map(lambda x : x+1, data))
print(data)
print(data_increased)

even_values = list(filter(lambda x : x % 2 == 0, data))
print(even_values)

total = reduce(lambda a, b : a + b, data)
print(total)