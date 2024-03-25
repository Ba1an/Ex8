a = 10
b = 100
c = 2
d = 5

ls = list(map(lambda x: x % c != 0 and x % 10 == d, range(a, b+1)))

count = 0
for num in ls:
    if num == True:
        count += 1

print(count)