import sys 

sys.path.append('..')

from config.settings import *
from classes.sfx import SFX

class Player(pygame.sprite.Sprite):
  
  
  
  def __init__(self, name = 'ingame'):
    super().__init__()

    self.name = name

    match self.name:
      case 'ingame':
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
        
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, GROUND_SURFACE_POS_Y))
      
        self.gravity = 0

        self.jump_sound = SFX('player_jump')

      case 'menu':
        self.image = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 2)
        self.rect = self.image.get_rect(center = (GAME_WIDTH / 2, GAME_HEIGHT / 2))


  def player_input(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and self.rect.bottom >= GROUND_SURFACE_POS_Y:
      self.gravity = -20
      self.jump_sound.play_SFX()


  def appy_gravity(self):
    self.gravity += 1
    self.rect.y += self.gravity
    if self.rect.bottom >= GROUND_SURFACE_POS_Y:
      self.rect.bottom = GROUND_SURFACE_POS_Y

  def animation_state(self):
    if self.rect.bottom < GROUND_SURFACE_POS_Y:
      self.image = self.player_jump
    else:
      self.player_index += 0.1
      if self.player_index >= len(self.player_walk): self.player_index = 0
      self.image = self.player_walk[int(self.player_index)]


  def update(self):
    if self.name == 'ingame':
      self.animation_state()
      self.player_input()
      self.appy_gravity()
    if self.name == 'menu':
      pass

