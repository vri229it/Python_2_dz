class Road:

    _length = 0
    _width = 0

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass (self):
        return self._length * self._width * 25 * 5 / 1000


r = Road(5, 200)
print(r.mass())
