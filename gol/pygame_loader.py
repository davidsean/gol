import pygame
from pygame.locals import *

class pygameLoader:

  def __init__(self):

    pygame.init()

    self.fps = 60
    self.fpsClock = pygame.time.Clock()
    
    self.width, height = 640, 480
    self.screen = pygame.display.set_mode((width, height))

  def start(self):
    # Game loop.
    while True:
      self.screen.fill((0, 0, 0))
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      
      
      pygame.display.flip()
      self.fpsClock.tick(self.fps)
