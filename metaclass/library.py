

class Base:
    def foo(self):
        return self.bar()

old_bc = __build_class__

def my_bc(func, name, base=None, **kw):
    if base == Base:
        print('check if bar method is defined')
        # Not sure how to acutally check if the bar method
        # is defined in the derived class though
    if base is not None:
        return old_bc(func, name, base, **kw)
    return old_bc(func, name, **kw)

import builtins
builtins.__build_class__ = my_bc
