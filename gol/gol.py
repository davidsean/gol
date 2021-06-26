
# import pygame
import numpy as np

from numpy.lib.stride_tricks import as_strided

class GOL:

    def __init__(self, width, height, kT=0):
        """
        init
        """
        self.width = width
        self.height = height
        # add padding
        self.full = np.zeros((self.width+2, self.height+2), dtype=bool)
        nd_slice = (slice(1, -1),) * 2
        self.kT = kT
        # just an inner-view
        self.board = self.full[nd_slice]
        
        # rules: index represents num neighbors
        # alive stays alive iff 2 or 3 neighbors
        self.ruleOfLifeAlive =  np.array([0, 0, 1, 1, 0, 0, 0, 0, 0])
        # dead switches to living iff 3 neighbors
        self.ruleOfLifeDead = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0])

    def __repr__(self):
        return str(self.board.astype(np.uint8))

    def grid_nD(self):
        newShape = (self.width, self.height, 3, 3) 
        newStrides = self.full.strides + self.full.strides
        return as_strided(self.full, shape=newShape, strides=newStrides)

    def step(self, num_steps = 1):
        """Step forward
        This uses a trick fromm http://drsfenner.org/blog/2015/08/game-of-life-in-numpy-2/

        :param num_steps: Number of steps to take, defaults to 1
        :type num_steps: int, optional
        """
        for _ in range(num_steps):
            neighborhoods = self.grid_nD()
            sumOver = (-1, -2)
            neighborCt = np.sum(neighborhoods, sumOver) - self.board
            update = np.where(self.board, 
                self.ruleOfLifeAlive[neighborCt], 
                self.ruleOfLifeDead[neighborCt])
            # these indices will potentially change states
            change_idx = np.where(np.ravel(self.board)!=np.ravel(update))
            # print(change_idx)
            # old = update[change_idx]
            # apply the state changes
            folded_idx = np.unravel_index(change_idx, (self.width, self.height))
            self.board[folded_idx] = update[folded_idx]
            # self.board=update


    # def render_surface(self, img_arr:np.ndarray) -> pygame.Surface:
    #     """
    #     Process numpy data into a pygame surface
        
    #     :param im_arr: data as a numpy array
    #     :return: pygame surface
    #     """
    #     # add explicit color axis,
    #     img_rgb = np.reshape(img_arr, newshape=(img_arr.shape[0],img_arr.shape[1],1))
    #     # binary to uint8 greyscale
    #     img_rgb = (img_arr*255).astype(np.uint8)
    #     # and greyscale to RGB
    #     img_rgb = np.repeat(img_rgb,3,axis=2)
    #     img_surface = pygame.surfarray.make_surface(img_rgb)
    #     return img_surface




if __name__=='__main__':

    gol = GOL(8,8)
    gol.board[2:5,2:5] = 1

    print(gol)
    gol.step()
    print(gol)

