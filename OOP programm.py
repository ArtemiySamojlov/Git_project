class Point():  # making a point
    def __init__(self, x, y):  # initialising
        self.x = x
        self.y = y
        self._z = 1
        print(f'I started in {self.x} {self.y}')  # printing the location

    def __del__(self):  # writing steps after death
        print(f'I finished in {self.x} {self.y}')

    def move(self, dx, dy):  # moving a point
        self.x += dx
        self.y += dy
        print(self.x, self.y)

    @staticmethod
    def Hello():  # adding a function to print the greeting
        print("Hello world, I am a dot.")

    @classmethod
    def show_x(cls):  # showing x position
        print(cls.x)


'''point = Point(1, 2)
point.color = 'red'

point.move(1, 3)
print(point.color)'''


class Warcraft():  # class of a game
    def __init__(self):  # initialising
        self.game_type = 'strategy'


class Dota(Warcraft):  # class of another game
    def __init__(self):  # initialising
        super().__init__()


dota = Dota()
print(dota.game_type)
