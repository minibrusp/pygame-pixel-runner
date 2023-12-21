import time
from config.settings import *
from sys import exit
from random import choice

# components
from classes.player import Player
from classes.obstacle import Obstacle
from classes.sfx import SFX
from classes.bgm import BGM

class Main:
  def __init__(self):

    # general

    pygame.init()
    self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    pygame.display.set_caption('Pixel Runner')
    self.clock = pygame.time.Clock()
    self.font_face_n_size = pygame.font.Font('font/Pixeltype.ttf', 50)
    self.credits_font_face = pygame.font.Font('font/Pixeltype.ttf', 25)
    self.game_active = False
    

    # statics
    _sky_surface_image = pygame.image.load('graphics/Sky.png')
    self.sky_surface = pygame.transform.scale(_sky_surface_image, (SKY_SURFACE_WIDTH, SKY_SURFACE_HEIGHT)).convert()
    _ground_surface_image = pygame.image.load('graphics/ground.png').convert()
    self.ground_surface = pygame.transform.scale(_ground_surface_image, (GROUND_SURFACE_WIDTH, GROUND_SURFACE_HEIGHT))

    # Components

    # Player
    self.player = pygame.sprite.GroupSingle()
    self.player.add(Player())

    self.player_menu = pygame.sprite.GroupSingle()
    self.player_menu.add(Player('menu'))

    # Obstacles 
    self.obstacle_group = pygame.sprite.Group()
    self.obstacle_rect_list = []

    # Text

    # Score
    self.start_time = 0
    self.score = 0

    # Timers
    self.obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(self.obstacle_timer, 1500)

    # SFX 
    self.collision_sound_1 = SFX('collision_1')
    self.collision_sound_2 = SFX('collision_2')
    self.collision_sound_3 = SFX('collision_3')

    # BGM

  def display_text(self, message, color, x_pos, y_pos):
    text = self.font_face_n_size.render(message, False, color)
    text_rect = text.get_rect(center = (x_pos, y_pos))
    self.screen.blit(text, text_rect)
    
  def display_credits(self):
    credits = self.credits_font_face.render('github.com/minibrusp', False, SCORE_COLOR)
    credits_rect = credits.get_rect(center = (100, GAME_HEIGHT - 50))
    self.screen.blit(credits, credits_rect)

  def display_score(self):
    current_time = int(pygame.time.get_ticks() / 1000) - self.start_time
    self.display_text(f' Score: {current_time}', SCORE_COLOR, TEXT_CENTER_X, SCORE_POS_Y)
    return current_time
  
  def collision_sprite(self):
    if pygame.sprite.spritecollide(self.player.sprite, self.obstacle_group, False):
      BGM.channel.stop()
      self.obstacle_group.empty()
      SFX.random_play_SFX(self.collision_sound_1, self.collision_sound_2, self.collision_sound_3)
      time.sleep(3)
      return False
    else: return True

  def update(self):
    pygame.display.update()
    self.clock.tick(60) # max 60fps

  def run(self):
    while True:

      # event loop
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()

        if self.game_active:

          if event.type == self.obstacle_timer:
            self.obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail'])))

        else: 
          if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            BGM.channel.stop()
            self.game_active = True
            self.start_time = int(pygame.time.get_ticks() / 1000)

      # game loop
      if self.game_active:
        self.screen.blit(self.sky_surface, (0, 0))
        self.screen.blit(self.ground_surface, (0, GROUND_SURFACE_POS_Y))

        # score
        self.score = self.display_score()

        # Player 
        self.player.draw(self.screen)
        self.player.update()

        # Obstacles      
        self.obstacle_group.draw(self.screen)
        self.obstacle_group.update()

        # collision
        self.game_active = self.collision_sprite()

        # BGM
        if not BGM.is_BGM_channel_busy() and self.game_active:
          BGM.play_random_BGM('ingame')

        # text 
        self.display_credits()
        


      else:
        self.screen.fill((94, 129, 162))

        # Player
        self.player_menu.draw(self.screen)
        self.player_menu.update()

        # text
        self.display_text('Pixel Runner', TEXT_COLOR, TEXT_CENTER_X, TITLE_POS_Y)

        if self.score == 0: self.display_text('Press space to run', TEXT_COLOR, TEXT_CENTER_X, GAME_MSG_POS_Y)
        else: self.display_text(f'Your score: {self.score}', TEXT_COLOR, TEXT_CENTER_X, GAME_MSG_POS_Y)

        self.display_credits()

        if not BGM.is_BGM_channel_busy():
          BGM.play_random_BGM('menu')



      # update 
      self.update()

if __name__ == '__main__':
  main = Main()
  main.run()
  