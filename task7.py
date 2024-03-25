import json

def to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapper


@to_json
def get_dic(lst):
    numbers = dict.fromkeys(lst)
    return numbers


@to_json
def get_list(num, l=[]):
    for i in range(1, num+1):
        l.append(i)
    return l

print(get_dic(['first', 'second', 'third']))
print(get_list(5))