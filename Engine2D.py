'''
Реализовать 2D-движок, который умеет “рисовать” простейшие
двумерные примитивы на экране. Сам движок должен быть
представлен в виде объекта класса Engine2D.
• Движок должен иметь “холст” (canvas) и возможность добавлять
на него фигуры. Холст будет содержать текущий список
примитивов для отрисовки.
• Реализовать классы для 3-х геометрических фигур: окружность,
треугольник, прямоугольник. Необходимые параметры для
создания фигур выбрать самостоятельно.
• Каждая фигура должна иметь метод draw(), при вызове которого
выводится информация в виде print’а, например “Drawing Circle:
(0, 1) with radius 5”.
• При завершении добавления фигур, у движка необходимо
вызвать публичный метод draw(), который последовательно
вызовет методы для отрисовки у всех фигур на холсте и очистит
его.
• Добавить возможность менять цвет отрисовки, путем вызова
публичного метода у движка (можно воспринимать это как
«смена карандаша»):
        • После вызова этого метода, все последующие фигуры
    должны рисоваться указанным цветом, до очередного
    выставления нового цвета.
        • В тексте “отрисовки” фигуры должен появиться цвет,
    которым она будет рисоваться.
        • Написать юниттесты с использованием pytest. Необходимое
    количество тестов определить самостоятельно
'''


class Figure:

    def __init__(self, name: str):
        self.name = name
        if self.name not in ('Triangle', 'Rectangle', 'Circle'):
            raise TypeError(f'This is not a figure')


class Triangle(Figure):

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(self.__class__.__name__)

    def __repr__(self):
        return f'with {self.a}, {self.b} and {self.c} sides'


class Rectangle(Figure):

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        super().__init__(self.__class__.__name__)

    def __repr__(self):
        return f'with {self.a} and {self.b} sides'


class Circle(Figure):

    def __init__(self, center: tuple, radius: int):
        self.center = center
        self.radius = radius
        super().__init__(self.__class__.__name__)

    def __repr__(self):
        return f'with center in {self.center} and {self.radius} radius'
        #raise TypeError


class Engine2D:

    def __init__(self):
        self.color = None
        self.canvas = []

    def add(self, obj):
        if isinstance(obj, Figure):
            self.canvas.append(obj)

    def draw(self):
        if not self.canvas:
            return None
        for obj in self.canvas:
            try:
                canvas_figure = f'Drawing:', obj.name, obj.__repr__(), f'| {self.color} color.' if self.color else ''
                print(f'Drawing:', obj.name, obj.__repr__(), f'| {self.color} color.' if self.color else '')
            except:
                pass
        self.canvas = []

    def set_color(self, color):
        self.color = color


class TestUnit:

    def test_create_a_figures(self):
        test_figure1 = Triangle(10, 10, 10)
        test_figure2 = Rectangle(10, 10)
        test_figure3 = Circle((0, 0), 10)

        test_figures = [test_figure1, test_figure2, test_figure3]

        for test_figure in test_figures:
            assert isinstance(test_figure, Figure)

    def test_create_not_a_figure(self):
        try:
            test_not_a_figure1 = Triangle(10, 10)
            test_not_a_figure2 = Rectangle(10)
            test_not_a_figure3 = Circle((0, 0))
        except TypeError:
            assert TypeError

    def test_create_a_figure_from_parent_class(self):
        try:
            test_figure = Figure(0)
        except TypeError:
            assert TypeError

    def test_add_a_figure_on_canvas(self):
        test_engine = Engine2D()
        test_figure = Triangle(10, 10, 10)

        test_engine.add(test_figure)

        assert test_engine.canvas[0] == test_figure
        
    def test_correct_type_of_added_figure(self):
        test_engine = Engine2D()
        test_figure = Triangle(10, 10, 10)

        test_engine.add(test_figure)

        assert isinstance(test_engine.canvas[0], Triangle)

    def test_add_not_a_figure_on_canvas(self):
        test_engine = Engine2D()
        test_engine.add(0)

        assert not test_engine.canvas

    def test_adding_a_lot_of_figures(self):
        test_engine = Engine2D()
        test_figure1 = Triangle(10, 10, 10)
        test_figure2 = Rectangle(10, 10)
        test_figure3 = Circle((0, 0), 10)

        test_figures = [test_figure1, test_figure2, test_figure3]

        for test_figure in test_figures:
            test_engine.add(test_figure)

        test_engine.add(0)

        assert len(test_engine.canvas) == 3

    def test_change_color(self):
        test_engine = Engine2D()
        test_engine.set_color('green')
        test_engine.set_color('blue')

        assert test_engine.color == 'blue'

    def test_draw_empty_canvas(self):
        test_engine = Engine2D()

        assert test_engine.draw() is None

    def test_correct_attributes_of_figure_on_canvas(self):
        test_engine = Engine2D()
        test_figure = Circle((0, 0), 5)

        test_engine.add(test_figure)

        assert str(test_engine.canvas[0]) == f'with center in (0, 0) and 5 radius'



if __name__ == '__main__':
    triangle = Triangle(10, 10, 10)
    rectangle = Rectangle(10, 10)
    circle = Circle((0, 0), 5)
    #not_a_figure = Figure(11)
    engine = Engine2D()
    #engine.add(not_a_figure)
    engine.set_color('green')
    engine.add(circle)
    engine.add(rectangle)
    engine.add(11)
    engine.set_color('blue')
    engine.add(triangle)
    engine.set_color(None)
    engine.draw()

