from datetime import datetime
import functools

def exept(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg, **kwargs): #
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