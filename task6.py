def decarator(func):
    def wrapper(args):
        result = func(args)
        print('Результат работы функции:', result)
        return result
    return wrapper

@decarator
def summator(num_list):
    return sum(num_list)

summator([1, 2, 3, 4, 5])