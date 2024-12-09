import tkinter as tk

# Абстрактный класс для графических объектов
class Shape:
    def draw(self, canvas):
        pass

# Класс для точки
class Point(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas):
        canvas.create_oval(self.x - 2, self.y - 2, self.x + 2, self.y + 2, fill="black")

# Класс для линии
class Line(Shape):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill="black", tags="line")

# Класс редактора
class GraphicEditor:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        # Список точек
        self.points = []

        # Индекс текущей линии, которую нужно нарисовать
        self.line_index = 1

        # Переменная для хранения текущего режима (точка или линия)
        self.current_mode = None

        # Кнопка для рисования точек
        self.point_button = tk.Button(root, text="Точка", command=self.set_point_mode)
        self.point_button.pack(side="left")

        # Кнопка для рисования линий
        self.line_button = tk.Button(root, text="Линия", command=self.set_line_mode)
        self.line_button.pack(side="left")

        # Событие клика мыши на холсте
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def set_point_mode(self):
        self.current_mode = "point"

    def set_line_mode(self):
        self.current_mode = "line"
        self.draw_next_line()

    def on_canvas_click(self, event):
        if self.current_mode == "point":
            # Добавляем точку в список и рисуем её
            point = Point(event.x, event.y)
            self.points.append(point)
            point.draw(self.canvas)

    def draw_next_line(self):
        # Рисуем линию между первой точкой и следующей точкой
        if self.line_index < len(self.points):
            point1 = self.points[self.line_index - 1]
            point2 = self.points[self.line_index]
            line = Line(point1, point2)
            line.draw(self.canvas)
            self.line_index += 1  # Переходим к следующей линии

# Создание основного окна и запуск программы
root = tk.Tk()
root.title("Графический редактор")
editor = GraphicEditor(root)
root.mainloop()
