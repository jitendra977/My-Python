import time
from functools import lru_cache


@lru_cache(maxsize=32)
def somework(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("now running")
    somework(3)
    somework(1)
    print('done')
    somework(3)
    print('called again...')
