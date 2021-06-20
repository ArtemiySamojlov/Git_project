class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f'I started in {self.x} {self.y}')

    def __del__(self):
        print(f'I finished in {self.x} {self.y}')

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(self.x, self.y)

    @staticmethod
    def Hello():
        print("Hello world, I am a dot.")

    @classmethod
    def show_x(cls):
        print(cls.x)


'''point = Point(1, 2)
point.color = 'red'

point.move(1, 3)
print(point.color)'''


class Warcraft():
    def __init__(self):
        self.game_type = 'strategy'


class Dota(Warcraft):
    def __init__(self):
        super().__init__()


dota = Dota()
print(dota.game_type)
