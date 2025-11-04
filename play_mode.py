from pico2d import *

from boy import Boy
from grass import Grass
import game_world

import game_framework
from bird import Bird

boy = None

def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global running

    running = True
    grass = Grass()
    game_world.add_object(grass, 0)

    #boy = Boy()
   # game_world.add_object(boy, 1)

    birds = [
        Bird(x=200, y=450),
        Bird(x=400, y=400),
        Bird(x=600, y=500, dir=-1),
        Bird(x=800, y=350),
        Bird(x=1000, y=450, dir=-1),
        Bird(x=1200, y=400),
        Bird(x=1400, y=480, dir=-1),
        Bird(x=300, y=520),
        Bird(x=900, y=370),
        Bird(x=1100, y=530)
    ]
    game_world.add_objects(birds, 1)

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

