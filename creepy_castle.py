from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        print("Welcome to Spooky Castle. A game inside a spooky castle.")
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):
    def enter(self):
        print("This is your death scene.")
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print('You made it to the central corridor!')
        return 'the_bridge'

class LaserWeaponArmory(Scene):
    def enter(self):
        print("Welcome to the Armory")
        return 'escape_pod'

class TheBridge(Scene):
    def enter(self):
        print("The Bridge is here.")
        return 'death'

class EscapePod(Scene):
    def enter(self):
        print("Escape the pod!")
        return 'finished'

class Finished(Scene):
    def enter(self):
        print("You're Finished!")
        return 'finished'

class Map(object):
    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.scenes[scene_name]

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
