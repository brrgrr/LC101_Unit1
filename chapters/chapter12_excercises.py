import math


class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def distance_from_point(self, other_point):
        Dx = self.x - other_point.x
        Dy = self.y - other_point.y
        return math.sqrt((Dx ** 2) + (Dy ** 2))

    def reflect_x(self):
        return Point(self.x, 0 - self.y)

    def slope_from_origin(self):
        if self.x != 0:
            return self.y / self.x

    def move(self, Dx, Dy):

        pass

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


def main_point():
    p = Point(3, 3)
    q = Point(6, 7)
    r = Point(3, 5)
    print(p.distance_from_origin())
    print(r.reflect_x())
    print(p.distance_from_point(q))


def main():
    main_point()


if __name__ == "__main__":
    main()
