class Point2d:
    def __init__(self, id=0, x=0.0, y=0.0):
        self.id = id
        self.x = x
        self.y = y

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, int) and value >= 0:
            self.__id = value
        else:
            raise RuntimeError("id deve ser int e não-negativo.")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, float):
            self.__x = value
        else:
            raise RuntimeError("x deve ser float e não-negativo.")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, float):
            self.__y = value
        else:
            raise RuntimeError("y deve ser float e não-negativo.")

    def __add__(self, other):
        if isinstance(other, Point2d):
            res = Point2d()
            res.id = self.id + other.id
            res.x = self.x + other.x
            res.y = self.y + other.y
            return res
        else:
            raise RuntimeError("other deve ser objeto do tipo Point2d")

    def __sub__(self, other):
        if isinstance(other, Point2d):
            res = Point2d()
            res.id = self.id + other.id
            res.x = self.x - other.x
            res.y = self.y - other.y
            return res
        else:
            raise RuntimeError("other deve ser objeto do tipo Point2d")

    def __eq__(self, other):
        if isinstance(other, Point2d):
            return self.id == other.id
        else:
            raise RuntimeError("other deve ser objeto do tipo Point2d")

    def __str__(self):
        # return f'{self.__class__.__name__}: [id: {self.__id}, x: {self.__x}, y: {self.__y}]' #Funciona
        return f"{self.__class__.__name__}: [id: {self.id}, x: {self.x}, y: {self.y}]"  # Dica de formatação mais bonita


class Polygon2d:
    def __init__(self, id=0, name="poly1"):
        self.id = id
        self.name = name
        self.__points = []

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, int) and value >= 0:
            self.__id = value
        else:
            raise RuntimeError("id deve ser int e não-negativo.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self.__name = value
        else:
            raise RuntimeError("name deve ser str e não-vazio.")

    def add(self, point):
        if isinstance(point, Point2d) and point not in self.__points:
            self.__points.append(point)
        else:
            raise RuntimeError("point deve ser um objeto do tipo Point2d e não estar na lista.")

    def remove(self, point):
        if isinstance(point, Point2d) and point in self.__points:
            self.__points.remove(point)
        else:
            raise RuntimeError("point deve ser um objeto do tipo Point2d e estar na lista. ")
        
    def __len__(self):
        return len(self.__points)

    def __str__(self):
        res = f"{self.__class__.__name__}: [id: {self.id}, name: {self.name}]"
        i = 0
        for p in self.__points:
            res += f'\n{i}: ' + p.__str__()
            i += 1

        return res

if __name__ == "__main__":

    p1 = Point2d(1, 1.0, 1.0)
    print(p1)
    p2 = Point2d(2, 1.0, 1.0)
    print(p2)
    p3 = p1 + p2
    print(p3)
    p4 = p1 - p2
    print(p4)
    print(p3 == p4)
    P1 = Polygon2d(1, 'triangulo')
    try:
        po1 = Point2d(-1, 1.0, 1.0)
    except RuntimeError as e:
        print(f"Ocorreu o erro: {e}")
    try:
        po1 = Point2d(0, 10, 10)
    except RuntimeError as e:
        print(f"Ocorreu o erro: {e}")
    try:
        p5 = p1 + "texto"
    except RuntimeError as e:
        print(f"Ocorreu o erro: {e}")
    print(P1)
    P1.add(p1)
    P1.add(p2)
    P1.add(p3)
    print(len(P1))
    P1.remove(p3)
    print(len(P1))
    P1.add(p4)
    print(len(P1))