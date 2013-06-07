from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        print "This scene is not yet configured.  Subclass it and implement enter()."

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    
    quips = [
        "You died.  You kinda suck at this.",
        "Your mom would be proud...if you were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."
        ]
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
      print "The Gothons of Planet Percal #25 have invaded your ship and"
      print "destroyed your entire crew.  You are the last surviving"
      print "member and your last mission is to get the neutron destruct"
      print "bomb from the Weapons Armory, put it in the bridge, and blow"
      print "the ship up after getting into an escape pod.\n"
      print "You're running down the central corridor to the Weapons Armory"
      print "when a Gothon jumps out, red scaly skin, dark grimy teeth, and"
      print "evil clown costume flowing around his hate filled body."
      print "He's blocking the door to the Armory and about to pull a weapon"
      print "to blast you."

      action = raw_input("> ")

      if action == "shoot!":
          print "Quick on the draw you yank out you blaster and fire it"
          print "at the Gothon.  His clown costume is flowing and moving"
          print "around his body, which throws off your aim.  Your laster"
          print "hits his costume but misses him entirely.  This completely"
          print "ruins his brand new costume his mother bought him, which"
          print "makes him fly into an insane rage and blast you repeatedly"
          print "in the face until you are dead.  Then he eats you."
          return 'death'
      
      if action == "dodge!":
          print "Like a world class boxer you dodge, weave, slip and slide"
          print "right as the Gothon's blaste cranks a laser past your head."
          print "In the middle of your artful dodge your foot slips and you"
          print "bang your head on the metal wall and pass out."
          print "You wake up shortly after only to die as the Gothon stomps"
          print "on your head and eats you."
          return 'death'
      
      if action == "tell a joke":
          print "Lucky for you they made you learn Gothon insults in the"
          print "academy.  You tell the one Gothon joke you know:"
          print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,"
          print "fur fvgf nebhaq gur ubhfr."
          print "The Gothon stops, tries not to laugh, then busts out"
          print "laughing and can't move.  While he's laughing you run up"
          print "and shoot him square in the head putting him down, then"
          print "jump through the Weapon Armory door."

      else:
          print "DOES NOT COMPUTE!"
          return 'central_corridor'
      

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass

