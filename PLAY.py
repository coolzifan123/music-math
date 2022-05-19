import pygame
def play_midi(file):
   freq = 44100
   bitsize = -16
   channels = 2
   buffer = 1024
   pygame.mixer.init(freq, bitsize, channels, buffer)
   pygame.mixer.music.set_volume(1)
   clock = pygame.time.Clock()
   try:
       pygame.mixer.music.load(file)
   except:
       import traceback
       print(traceback.format_exc())
   pygame.mixer.music.play()
   while pygame.mixer.music.get_busy():
       clock.tick(30)

play_midi(r'new_song.midi')
