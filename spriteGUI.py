import pygame
import main
import graphics
import GuiBase
from constants import *
import sys
from pygame.locals import *
import main
from assets import *
import config
import environment


class SpriteGui():

    def __init__(self):
        self.surface = graphics.SCREEN
        self.gui_group = pygame.sprite.Group()
        bckImg = pygame.image.load('map1.png') # loading an image of the map
        player1 = pygame.image.load('player1.png')
        player2 = pygame.image.load('player2.png')
        player3 = pygame.image.load('player3.png')
        config.x = True
        pygame.font.init()   # font initialisation
        myfont = pygame.font.Font('font1.ttf', 65)  # choosing the font
        title = myfont.render("CHOOSE THE MODEL ", 1, (0,0,0))
        choosePlayer1 = myfont.render("[1]", 1, (0,51,0))
        choosePlayer2 = myfont.render("[2]", 1, (0,51,0))
        choosePlayer3 = myfont.render("[3]", 1, (0,51,0))
        self.surface.blit(bckImg, (0,0))  #blitting the background
        self.surface.blit(title, (375,80)) #blitting the title
        self.surface.blit(choosePlayer1, (315, 700))
        self.surface.blit(choosePlayer2, (745, 700))
        self.surface.blit(choosePlayer3,(1165, 700))
        self.surface.blit(player1, (270,400))
        self.surface.blit(player2, (700,400))
        self.surface.blit(player3, (1120, 400))


    #2def process_input(self):
        #for event in pygame.event.get(): # Menu control
            #if event.type == pygame.KEYDOWN:

                #elif (event.key == K_q):
                 #   pygame.display.quit()
                  #  pygame.quit()
                 #   sys.exit()

    def update(self):
        pass
    def render(self):
        self.gui_group.draw(self.surface)
        pygame.display.flip()
