from config.settings import *
from sys import exit
from random import choice

# components
from classes.player import Player
from classes.obstacle import Obstacle

class Main:
  def __init__(self):

    # general

    pygame.init()
    self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    pygame.display.set_caption('Pixel Runner')
    self.clock = pygame.time.Clock()
    self.font_face_n_size = pygame.font.Font('font/Pixeltype.ttf', 50)
    

    # statics
    _sky_surface_image = pygame.image.load('graphics/Sky.png')
    self.sky_surface = pygame.transform.scale(_sky_surface_image, (SKY_SURFACE_WIDTH, SKY_SURFACE_HEIGHT)).convert()
    _ground_surface_image = pygame.image.load('graphics/ground.png').convert()
    self.ground_surface = pygame.transform.scale(_ground_surface_image, (GROUND_SURFACE_WIDTH, GROUND_SURFACE_HEIGHT))

    # Components

    # Player
    self.player = pygame.sprite.GroupSingle()
    self.player.add(Player())

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

  def display_score(self):
    current_time = int(pygame.time.get_ticks() / 1000) - self.start_time
    score_surf = self.font_face_n_size.render(f' Score: {current_time}', False, TEXT_COLOR)
    score_rect = score_surf.get_rect(center = (TEXT_CENTER_X, SCORE_POS_Y))
    self.screen.blit(score_surf, score_rect)
    return current_time

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

        if event.type == self.obstacle_timer:
          self.obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail'])))


      # game loop
      self.screen.fill((94, 129, 162))
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


      # update 
      self.update()

if __name__ == '__main__':
  main = Main()
  main.run()
  