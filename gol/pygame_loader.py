import pygame
from pygame.locals import *
from gol.gol import GOL
import numpy as np

class pygameLoader:

  def __init__(self, kT=0):

    pygame.init()

    self.fps = 60
    self.fpsClock = pygame.time.Clock()
    
    self.width = 640
    self.height = 480
    self.screen = pygame.display.set_mode((self.width, self.height))

    self.gol = GOL(self.width,self.height, kT=kT)

  def render_surface(self, img_arr:np.ndarray) -> pygame.Surface:
      """
      Process numpy data into a pygame surface
      
      :param im_arr: data as a numpy array
      :return: pygame surface
      """
      # add explicit color axis,
      img_rgb = np.reshape(img_arr, newshape=(img_arr.shape[0],img_arr.shape[1],1))
      # binary to uint8 greyscale
      img_rgb = (img_rgb*255).astype(np.uint8)
      # and greyscale to RGB
      img_rgb = np.repeat(img_rgb,3,axis=2)
      img_surface = pygame.surfarray.make_surface(img_rgb)
      return img_surface

  def start(self):
    # Game loop.

    while True:
      self.screen.fill((0, 0, 0))
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()


      surf = self.render_surface(self.gol.board)
      self.screen.blit(surf,(0,0))
      self.gol.step()
      
      pygame.display.flip()
      self.fpsClock.tick(self.fps)
