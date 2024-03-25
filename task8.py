from datetime import datetime
import functools

def exept(filename):
    '''
    This function returns a decorator that handles exceptions thrown when the decorated function is called.
    :param filename: The name of the file in which information about exceptions will be written.
    :return: A decorator that handles exceptions.
    '''
    def decorator(func):
        '''
        The decorator wraps the target function and catches exceptions that may occur during its execution.
        :param func: Function that we are changing
        :return: Changed function
        '''
        @functools.wraps(func)
        def wrapper(*arg, **kwargs):
            '''
            This function is a wrapper around another function for the purpose of catching exceptions.
            :param arg: parameters of the function to be decorated
            :param kwargs: default parameters of the decorated function
            :return: Absent. The function either succeeds or handles an exception.
            '''
            try:
                func(*arg, **kwargs)
            except Exception as e:
                with open(filename, 'a') as f:
                    print(f'{type(e).__name__} happend at {datetime.now()}', file=f)
            return
        return wrapper
    return decorator

@exept('out.txt')
def dividing(x, y):
    result = int(x) / int(y)
    print(result)

dividing(1, 0)
dividing(1, 'a')