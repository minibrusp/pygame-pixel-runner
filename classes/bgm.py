from random import choice
import sys 

sys.path.append('..')

from config.settings import *

class BGM():

  mixer = pygame.mixer

  mixer.init()
  mixer.set_num_channels(8)

  channel = mixer.Channel(2)
  channel.set_volume(0.7)

  in_game_BGM_1 = pygame.mixer.Sound('audio/ingame1.wav')
  in_game_BGM_2 = pygame.mixer.Sound('audio/ingame2.wav')
  in_menu_BGM_1 = pygame.mixer.Sound('audio/menu1.wav')
  in_menu_BGM_2 = pygame.mixer.Sound('audio/menu2.wav')

  def stop_BGM():
    BGM.channel.stop()
  

  def play_BGM(chosen_BGM):

    BGM.channel.play(Sound = chosen_BGM, loops = -1)

  def is_BGM_channel_busy():

    return BGM.channel.get_busy()
        
  
  def play_random_BGM(type = 'ingame'):
    match type:
      case 'ingame':
        chosen_BGM = choice([BGM.in_game_BGM_1, BGM.in_game_BGM_2])
        BGM.play_BGM(chosen_BGM)
      case 'menu':
        chosen_BGM = choice([BGM.in_menu_BGM_1, BGM.in_menu_BGM_2])
        BGM.play_BGM(chosen_BGM)
