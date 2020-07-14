#dec.py

def add(x, y=10):
    return x + y


def print_add_attrs():
    print('add.__name__:',  add.__name__)
    print('add.__module__:', add.__module__)
    print('add.__defaults__:', add.__defaults__)
    print('add.__code__:', add.__code__)
    # actual byte code for the function
    print('add.__code__.co_code:', add.__code__.co_code) 
    print('add.__code__.co_varnames:', add.__code__.co_varnames)
    print()
    from inspect import getsource
    print('getsource(add):')
    print(getsource(add))
    print()
    from inspect import getfile
    print('getfile(add):')
    print(getfile(add))
    

if __name__ == '__main__':
    print_add_attrs()
