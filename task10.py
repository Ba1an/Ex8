import time
import  functools

def rate_limited(max_calls, period, max_time):
    def decorator(func):
        call_times = []
        @functools.wraps(func)# Встроенный декоратор который позволяет сохранять имя функции
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            call_times.append(start_time)
            for t in call_times:
                if end_time - t > period:
                    call_times.remove(t)
            if end_time - start_time > max_time:
                raise Exception(f"Function took longer than {max_time} seconds to execute")
            if len(call_times) >= max_calls:
                raise Exception("Rate limit exceeded")
            return
        return wrapper
    return decorator

@rate_limited(8, 60, 5)
def run(i):
    time.sleep(i)
    print("...", i)
for i in range(6):
    run(i)