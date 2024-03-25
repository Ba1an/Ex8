import json
import yaml
import  functools

def to_smth(type=None):
    '''
    function changes result in new type
    :param type: New format
    :return:
    '''
    def decorator(func):
        '''
        The decorator wraps the target function.
        :param func: Function that we are changing
        :return: Changed function
        '''
        @functools.wraps(func)
        def wrapper(*arg, **kwargs):
            '''
            This function is a wrapper of another function and is designed to check whether conditions are met.
            :param arg: parameters of the function to be decorated
            :param kwargs: default parameters of the decorated function
            :return: Result in new format
            '''
            result = func(*arg, **kwargs)
            if type == None or type == 'json':
                return json.dumps(result)
            elif type == 'yalm':
                return yalm.dump(result)
        return wrapper
    return decorator

@to_smth('yaml')
def to_yaml():
    return '1 2 3 4 5'

@to_smth('json')
def to_json():
    return '1 2 3 4 5'

print(to_yaml(), type(to_yaml()))
print(to_json(), type(to_json()))