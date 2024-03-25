import json

json_str = '[["яблоко", 5], ["апельсин", 3], ["банан", 7]]'
lst = json.loads(json_str)
lst = sorted(lst, key=lambda x: x[1])
final = lst[::-1]
print(final)

