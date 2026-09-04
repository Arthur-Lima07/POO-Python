from abc import ABC
from math import sqrt

class Shape(ABC):
    __baseId = 0
    @classmethod
    def _getNextId(cls):
        id = cls.__baseId
        cls.__baseId = cls.__baseId + 1
        return id
    def __init__(self, x = 0 , y = 0 , radius = 1.0, angle = 0.0):
        self.__id = Shape._getNextId() # Acessa direto por ser propriedade somente-leitura
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
    @property
    def id(self):
        return self.__id
    @id.setter # Evita escrita de propriedade somente-leitura
    def id(self, value):
        raise RuntimeError('id is read-only')

    @property
    def radius(self):
        return self.__radius
    @radius.setter # Evita escrita de propriedade somente-leitura
    def radius(self, value):
        if isinstance(value, (int,float)) and value > 0:
            self.__radius = value
        else:
            raise AttributeError('radius must be positive')

    @property
    def x(self):
        return self.__x
    @x.setter # Evita escrita de propriedade somente-leitura
    def x(self, value):
        if isinstance(value, (int,float)) and value >= 0:
            self.__x = value
        else:
            raise AttributeError('x must be positive')

    @property
    def y(self):
        return self.__y
    @y.setter # Evita escrita de propriedade somente-leitura
    def y(self, value):
        if isinstance(value, (int,float)) and value >= 0:
            self.__y = value
        else:
            raise AttributeError('y must be positive')

    @property
    def angle(self):
        return self.__angle
    @angle.setter # Evita escrita de propriedade somente-leitura
    def angle(self, value):
        if isinstance(value, (int,float)) and value >= 0:
            self.__angle = value
        else:
            raise AttributeError('angle must be positive')
        
    #@abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        return 3/4*sqrt(3)*self.radius**2
    
class Square(Shape):
    def area(self):
        return 2*self.radius**2

class Pentagon(Shape):
    pass

class Hexagon(Shape):
    pass

if __name__ == '__main__':
    t1 = Triangle(0, 1, 1)
    print(f't1.id: {t1.id}, t1.area: {t1.area()}')
    t2 = Triangle(1,0,1)
    print(f't2.id: {t2.id}')
    t3 = Triangle(1,1,2)
    print(f't3.id: {t3.id}')

    q1 = Square()
    print(f'q1.id: {q1.id}, q1.x: {q1.x}, q1.y: {q1.y}, q1.radius: {q1.radius}')
    q2 = Square()
    print(f'q2.id: {q2.id}')
    q3 = Square()
    print(f'q3.id: {q3.id}')

    p1 = Pentagon()
    print(f'p1.id: {p1.id}')
    p2 = Pentagon()
    print(f'p2.id: {p2.id}')
    p3 = Pentagon()
    print(f'p3.id: {p3.id}')

    h1 = Hexagon()
    print(f'h1.id: {h1.id}')
    h2 = Hexagon()
    print(f'h2.id: {h2.id}')
    h3 = Hexagon()
    print(f'h3.id: {h3.id}')