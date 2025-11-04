from pico2d import *
import game_framework

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = 400, 400
        self.size = 100
        self.dir = 1
        self.speed = 10#일단 상수
        self.frame = 0

        self.fly = Fly(self)
        self.state = self.fly
        self.state.enter()  # 상태 진입

    def update(self):
        self.state.do()

    def draw(self):
        self.state.draw()


class Fly:
    def __init__(self, bird):


    def enter(self):
        pass

    def exit(self):
        pass

    def do(self):
        pass

    def draw(self):
        pass

