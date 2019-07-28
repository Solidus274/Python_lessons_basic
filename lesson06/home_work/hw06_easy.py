# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, a, b, c):
        def side(i, j):
            return math.sqrt((j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2)
        self.a = a
        self.b = b
        self.c = c
        self.a = a
        self.b = b
        self.c = c
        self.AB = side(self.a, self.b)
        self.BC = side(self.b, self.c)
        self.AC = side(self.a, self.c)

    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2

        return math.sqrt(semi_perimeter
                        * (semi_perimeter - self.AB)
                        * (semi_perimeter - self.BC)
                        * (semi_perimeter - self.AC))

    def perimeterTriangle(self):
        return self.AB + self.BC + self.AC

    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)


tri_1 = Triangle([0, 0], [1, 1], [2, 0])
tri_2 = Triangle([1, 1], [1, 2], [2, 1])
tri_3 = Triangle([0, 1], [1, 0], [2, 0])

print("Треугольник:")
print("Периметр треугольника: ", tri_1.perimeterTriangle())
print("Периметр треугольника: ", tri_2.perimeterTriangle())
print("Периметр треугольника: ", tri_3.perimeterTriangle())
print("Площадь треугольника: ", tri_1.areaTriangle())
print("Площадь треугольника: ", tri_2.areaTriangle())
print("Площадь треугольника: ", tri_3.areaTriangle())
print("Высота треугольника: ", tri_1.heightTriangle())
print("Высота треугольника: ", tri_2.heightTriangle())
print("Высота треугольника: ", tri_3.heightTriangle())
print()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze:
    def __init__(self, a, b, c, d):

        def side(i, j):
            return math.sqrt((j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2)

        def areaTriangle(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2

            return math.sqrt(semi_perimeter
                             * (semi_perimeter - len1)
                             * (semi_perimeter - len2)
                             * (semi_perimeter - len3))
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.AB = side(self.a, self.b)
        self.BC = side(self.b, self.c)
        self.CD = side(self.c, self.d)
        self.DA = side(self.d, self.a)
        self.diagonal_AC = side(self.c, self.a)
        self.diagonal_BD = side(self.b, self.d)
        self.perimeter = self.AB + self.BC + self.CD + self.DA
        self.area = areaTriangle(self.AB, self.diagonal_BD, self.DA) \
                    + areaTriangle(self.diagonal_BD, self.BC, self.CD)

    def isTrapezeEqu(self):
        if self.diagonal_AC == self.diagonal_BD:
            return "Да"
        return "Нет"


trap_1 = Trapeze([0, 0], [1, 1], [2, 1], [3, 0])
trap_2 = Trapeze([1, 1], [1, 2], [2, 1], [3, 0])
trap_3 = Trapeze([0, 1], [1, 0], [2, 0], [3, 0])

print("Трапеция:")
print("Является ли эта трапеция равнобочной? ", trap_1.isTrapezeEqu())
print("Является ли эта трапеция равнобочной? ", trap_2.isTrapezeEqu())
print("Является ли эта трапеция равнобочной? ", trap_3.isTrapezeEqu())
print("Длина стороны AB: ", trap_1.AB)
print("Длина стороны AB: ", trap_2.AB)
print("Длина стороны AB: ", trap_3.AB)
print("Площадь трапеции: ", trap_1.area)
print("Площадь трапеции: ", trap_2.area)
print("Площадь трапеции: ", trap_3.area)
print("Периметр трапеции: ", trap_1.perimeter)
print("Периметр трапеции: ", trap_2.perimeter)
print("Периметр трапеции: ", trap_3.perimeter)
