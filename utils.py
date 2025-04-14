import time
import functools

def timeit(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        t1=time.time()
        r=f(*args, **kwargs)
        t2=time.time()
        print(f"Time spent: {t2-t1}")
        return r
    return wrapper

if __name__=='__main__':
    @timeit
    def f(x):
        #time.sleep(1)
        return x**2
    
    f(2)
