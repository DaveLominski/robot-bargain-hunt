import pygame
import main
import graphics
from constants import *
import sys
from pygame.locals import *
import main
import spriteGUI
import config


class Environment():

    def __init__(self):
        self.surface = graphics.SCREEN
        self.gui_group = pygame.sprite.Group()
        bckImg = pygame.image.load('map1.png') # loading an image of the map
        pygame.font.init()   # font initialisation
        myfont = pygame.font.Font('font1.ttf', 65)  # choosing the font
        myfont1 = pygame.font.Font('font1.ttf', 40)
        myfont2 = pygame.font.Font('font1.ttf', 30)
        myfont3 = pygame.font.Font('font1.ttf', 32)
        title = myfont.render("IT BELONGS IN THE MUSEUM !", 1, (0,0,0))
        startTheGame = myfont1.render("PRESS 'ENTER' TO START", 1, (0,200,0))
        closeTheMenu = myfont2.render("PRESS 'Q' TO QUIT", 1, (180,0,0))
        chooseTheSprite = myfont3.render("PRESS 'C' TO CHANGE THE AI MODEL", 1, (0,100,0))
        self.surface.blit(bckImg, (0,0))  #blitting the background
        self.surface.blit(title, (375,80)) #blitting the title
        self.surface.blit(startTheGame, ((500),700))
        self.surface.blit(closeTheMenu, ((635),885))
        self.surface.blit(chooseTheSprite, ((450,800)))


    def process_input(self):
        for event in pygame.event.get(): # Menu control
            if event.type == pygame.KEYDOWN: 
                if (event.key == K_RETURN):
                    print("START GAME")
                    main.start()
                elif (event.key == K_c):
                    spriteGUI.SpriteGui()
                if (event.key == K_1) and config.x == True:
                    config.playerCh = 'player1.1.png'
                    main.start()
                elif (event.key == K_2) and config.x == True:
                    config.playerCh = 'player2.1.png'
                    main.start()
                elif (event.key == K_3) and config.x == True:
                    config.playerCh = 'player3.1.png'
                    main.start()

                elif (event.key == K_q): # Quit game
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    
    def update(self):
        pass

    def render(self):
        self.gui_group.draw(self.surface)
        pygame.display.flip()