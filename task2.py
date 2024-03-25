a = 2
b = 12
c = 2
d = 3

ls = list(filter(lambda x: x % d == 0 and x % c == 0, range(a, b+1)))
print(sum(ls))
