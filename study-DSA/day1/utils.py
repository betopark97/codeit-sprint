import time
from functools import wraps

# 런타인 측정해주는 데코레이터
def runtime_calculator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"Function '{func.__name__}' executed in: {runtime:.6f} seconds")
        return result
    return wrapper


import numpy as np

# 숫자 배열을 만드는 함수
def create_num_array(n):
    arr = np.arange(1, n, 2)
    return arr