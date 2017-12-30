

from library import Base


assert hasattr(Base, 'foo'), 'you broke it, you fool'


class Derivied(Base):
    def bar(self):
        return self.foo()
