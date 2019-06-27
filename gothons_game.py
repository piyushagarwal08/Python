from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("this scene is not yet confirmed")
        prin("Subclass it and implement enteR().")
        exit(1)
class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_game = current_scene.enter()

class CentralCorridor(Scene):
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class Escapepod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self,start_scene):
        pass

    def next_scene(self,scene_game):
        pass

    def opening_scene(self):
        pass

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
