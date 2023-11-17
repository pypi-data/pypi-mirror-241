import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def is_point_outside(self, point_x, point_y):
        distance = math.sqrt((point_x - self.center_x)**2 + (point_y - self.center_y)**2)

        return distance > self.radius

if __name__ == "__main__":
    lingkaran = Circle(0, 0, 5)

    titik_x = 3
    titik_y = 4

    if lingkaran.is_point_outside(titik_x, titik_y):
        print(f"Titik ({titik_x}, {titik_y}) berada di luar lingkaran.")
    else:
        print(f"Titik ({titik_x}, {titik_y}) berada di dalam lingkaran.")
