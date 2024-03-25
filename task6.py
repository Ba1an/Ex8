def decarator(func):
    """
    This function is decorator
    :param func: function that we are changing
    :return: Changed function
    """
    def wrapper(args):
        """
        This function is a wrapper around another function to prints the result of the function
        :param args: function parameter
        :return: function result
        """
        result = func(args)
        print('Результат работы функции:', result)
        return result
    return wrapper


@decarator
def summator(num_list):
    return sum(num_list)


summator([1, 2, 3, 4, 5])