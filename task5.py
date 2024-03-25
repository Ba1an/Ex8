from functools import reduce

a = 1
b = 40
c = 2

numbers = list(filter(lambda x: x % c == 0 and int(x ** 0.5) ** 2 == x, range(a, b+1)))
sum = reduce(lambda x, y: x * y, numbers)
print(sum)
