from timeit import timeit


STEP = 2


def global_ref():
    res = 0
    
    for i in range(1000):
        res += STEP
        

def local_ref():
    res = 0
    step = STEP
    
    for i in range(1000):
        res += step


def global_improved():
    res = 0
    
    for i in range(1000):
        global STEP
        
        res += STEP
        

def global_param(step):
    res = 0
    
    for i in range(1000):
        res += step
        


print(f'global-ref => {timeit(lambda: global_ref(), number=100000)}')
print(f'local-ref => {timeit(lambda: local_ref(), number=100000)}')
print(f'global_improved => {timeit(lambda: global_improved(), number=100000)}')
print(f'global_param => {timeit(lambda: global_param(STEP), number=100000)}')
