import json


def to_json(func):
    """

    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        '''
        This function is a wrapper of another function and is designed to check whether conditions are met.
        :param args: parameters of the function to be decorated
        :param kwargs: default parameters of the decorated function
        :return:
        '''
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapper


@to_json
def get_dic(lst):
    numbers = dict.fromkeys(lst)
    return numbers


@to_json
def get_list(num, l=[]):
    for i in range(1, num + 1):
        l.append(i)
    return l


print(get_dic(['first', 'second', 'third']))
print(get_list(5))
