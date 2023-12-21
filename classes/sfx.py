from random import choice
import sys 

sys.path.append('..')

from config.settings import *

class SFX():
  player_jump = 'audio/jump.mp3'
  collision_1 = 'audio/collision1.wav'
  collision_2 = 'audio/collision2.wav'
  collision_3 = 'audio/collision3.wav'

  def __init__(self, name):
    self.name = name

    match self.name:
      case 'player_jump':
        self.sound = pygame.mixer.Sound(SFX.player_jump)
      case 'collision_1':
        self.sound = pygame.mixer.Sound(SFX.collision_1)
      case 'collision_2':
        self.sound = pygame.mixer.Sound(SFX.collision_2)
      case 'collision_3':
        self.sound = pygame.mixer.Sound(SFX.collision_3)

    # self.sound.set_volume(0.7)

  def play_SFX(self):
    self.sound.play()

  def random_play_SFX(*args):
    chosen_SFX = choice(args)
    chosen_SFX.play_SFX()
      