class Coordinates:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_coordinates(self):
        return f'x:{self._x}  y: {self._y} z: {self._z} '

    def set_coordinates(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, point):
        return Coordinates(self._x + point._x, self._y + point._y, self._z + point._z)

    def __truediv__(self, point):
        return Coordinates(self._x / point._x, self._y / point._y, self._z / point._z)

    def __sub__(self, point):
        return Coordinates(self._x - point._x, self._y - point._y, self._z - point._z)

    def __mul__(self, point):
        return Coordinates(self._x * point._x, self._y * point._y, self._z * point._z)

    def __neg__(self):
        return Coordinates(-self._x, -self._y, -self._z)

point1 = Coordinates(1, 3, 9)
print(point1.get_coordinates())
point2 = Coordinates(1, 3, 9)
print(point2.get_coordinates())
result = point1.__mul__(point2)
posResult = point1.__neg__()
print(posResult.get_coordinates())
