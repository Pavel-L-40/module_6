class Figure:
    sides_count = 0

    def __init__(self, __color, __sides, filled=True):
        self.__color = __color
        self.__sides = __sides
        self.filled = filled
# ======================================================================================================================

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        print('ошибка цвета')
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        # print(len(sides) == self.sides_count)
        if len(sides) != self.sides_count: return False # =================== self.sides ????????  Len(sides) ??????
        # print('x', sides)
        for i in range(len(sides)):                          # =================== проверить работу цикла ?????
            # print(sides[i])
            if type(sides[i]) != int or sides[i] <= 0: return False # проверить сравнение типа
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):                # возвращает периметр фигуры
        if isinstance(self, Circle):
            return self.get_sides()[0]
        elif isinstance(self, Triangle):
            return self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2]
        elif isinstance(self, Cube):
            return self.get_sides()[0] * 12

    def set_sides(self, *new_sides):
        # print(self.__is_valid_sides(new_sides))
        # print(len(new_sides))
        # print(self.sides_count)
        if self.__is_valid_sides(new_sides) and len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else: print(f'стороны не меняются')

# === Circle ===

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            # print('True')
            sides = [1]
        super().__init__(color, sides)
        self.color = color
        self.sides = sides[0]
        self.__radius = self.sides / (2 * 3.14) # радиус круга

    def get_square(self):                  # площадь круга
        return 3.14 * self.__radius ** 2


# === Triangle ===

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = [1, 1, 1]
        super().__init__(color, sides)
        self.color = color
        self.sides = sides

    def get_square(self):  #площадь треугольника
        perimetr = 0.5 * (self.sides[0] + self.sides[1] + self.sides[3])
        return perimetr * (perimetr - self.sides[0]) * (perimetr - self.sides[1]) * (perimetr - self.sides[2])


# === Cube ===

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            side = [1]
        else: side = sides
        sides = []
        for i in range(12):
            sides.append(side[0])
        super().__init__(color, sides)
        self.color = color
        self.sides = sides

    def get_volume(self):
        return self.sides[0] **3


# ====================== test case =====================


circle1 = Circle((200, 200, 100), 10, 16) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
