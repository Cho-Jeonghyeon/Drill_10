from pico2d import *
import game_framework

class Bird:
    def __init__(self, x=400, y=400, size=100, dir=1):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.size = size
        self.dir = dir
        self.speed = 10#일단 상수
        self.frame = 0

        self.fly = Fly(self)
        self.state = self.fly
        self.state.enter()  # 상태 진입

    def update(self):
        self.state.do()

    def draw(self):
        self.state.draw()

PIXEL_PER_METER = (10.0 / 0.2)  # 10 pixel == 20cm
FLY_SPEED_KMPH = 15.0           # 새의 실제 평균 속도
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.3               # 날개짓 1사이클 0.3초
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Fly:
    def __init__(self, bird):
        self.bird = bird

    def enter(self):
        pass

    def exit(self):
        pass

    def do(self):
        self.bird.frame = (self.bird.frame + 1) % 3

        self.bird.x += self.bird.dir * self.bird.speed

        if self.bird.x > 800 - self.bird.size // 2:
            self.bird.dir = -1
        elif self.bird.x < self.bird.size // 2:
            self.bird.dir = 1

    def draw(self):
        if self.bird.dir == 1:
            self.bird.image.clip_draw(int(self.bird.frame) * 183, 168, 183, 168,
                                      self.bird.x, self.bird.y, self.bird.size, self.bird.size)
        else:
            self.bird.image.clip_composite_draw(int(self.bird.frame) * 183, 168, 183, 168,
                                                0, 'h', self.bird.x, self.bird.y, self.bird.size, self.bird.size)