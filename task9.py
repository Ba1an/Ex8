import json
import yaml
import  functools

def to_smth(type=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg, **kwargs):
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