import math

class Sphere:
    def __init__(self, radius = 1, center_x = 0, center_y = 0, center_z = 0):
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y
        self.center_z = center_z
    def get_volume(self):
        return 'Объем шара: ' + str(int(4/3*math.pi*self.radius**3))
    def get_square(self):
        return 'Площадь внешней поверхности сферы: ' + str(int(4*math.pi*self.radius*self.radius))
    def get_radius(self):
        return 'Радиус сферы: ' + str(int(self.radius))
    def get_center(self):
        return (self.center_x, self.center_y, self.center_z)
    def set_radius(self, r):
        self.radius = r
    def set_center(self, x, y, z):
        self.center_x = x
        self.center_y = y
        self.center_z = z
    def is_point_inside(self, x, y, z):
        if math.sqrt((self.center_x - x) ** 2 + (self.center_y - y) ** 2 + (self.center_z - z) ** 2) <= self.radius:
            return True
        return False
    def __del__(self):
        print('Класс очищен')

object = Sphere(5, 5, 5, 5)
print(object.get_volume())
print(object.get_square())
print(object.get_radius())
print(object.get_center())
object.set_radius(4)
object.set_center(6, 7, 8)
print(object.is_point_inside(7, 6, 4))