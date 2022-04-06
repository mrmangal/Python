#  Accessing class attribute

class Enemy:

    init_num_lives = 5

    def __init__(self, x_coord, y_coord, speed):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.speed = speed


classAttribute = Enemy.init_num_lives

enemy01 = Enemy(54, 67, 200)

print(Enemy.init_num_lives)