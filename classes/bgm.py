from random import choice
import sys 

sys.path.append('..')

from config.settings import *

class BGM():
  in_game_bgm_1 = 'audio/ingame1.wav'
  in_game_bgm_2 = 'audio/ingame2.wav'

  mixer = pygame.mixer

  mixer.init()
  mixer.set_num_channels(8)
  channel = mixer.Channel(2)
  channel.set_volume(0.7)

  def __init__(self, name):
    self.name = name
    # self.mixer = pygame.mixer

    match self.name:
      case 'in_game_1':
        self.sound = BGM.mixer.Sound(BGM.in_game_bgm_1)
      case 'in_game_2':
        self.sound = BGM.mixer.Sound(BGM.in_game_bgm_2)

    
    # self.channel = self.mixer.Channel(2)
    
    # self.mixer.init()
    # self.mixer.set_num_channels(8)
    # self.mixer.music.set_volume(0.7)


  def play_BGM(self):
    BGM.channel.play(Sound = self.sound, loops = -1)

  def is_BGM_channel_busy():
    return BGM.channel.get_busy()
  
  def play_random_BGM(*args):
    chosen_BGM = choice(args)
    chosen_BGM.play_BGM()





# from random import choice
# import sys 

# sys.path.append('..')

# from config.settings import *

# class BGM():
#   in_game_bgm_1 = 'audio/ingame1.wav'
#   in_game_bgm_2 = 'audio/ingame2.wav'

#   def __init__(self, name):
#     self.name = name
#     self.mixer = pygame.mixer

#     match self.name:
#       case 'in_game_1':
#         self.sound = self.mixer.Sound(BGM.in_game_bgm_1)
#       case 'in_game_2':
#         self.sound = self.mixer.Sound(BGM.in_game_bgm_2)

    
#     self.channel = self.mixer.Channel(2)
    
#     self.mixer.init()
#     self.mixer.set_num_channels(8)
#     self.mixer.music.set_volume(0.7)


#   def play_BGM(self):
#     self.channel.play(Sound = self.sound, loops = -1)

#   def is_BGM_channel_busy(self):
#     return self.channel.get_busy()

