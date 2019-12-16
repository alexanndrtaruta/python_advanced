from datetime import datetime

def timetodo(func):
    def wrapper(*args):
        start = datetime.now()
        result  = func(*args)
        print(datetime.now() - start)
        return result
    return wrapper

@timetodo
def hello(count):
    for i in range(count):
        print('Hello world')


hello(1000000)
