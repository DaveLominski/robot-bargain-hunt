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
    """Main Menu class, all of the key events and screen outputs are here"""
    def __init__(self):
        self.surface = graphics.SCREEN
        self.gui_group = pygame.sprite.Group()
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.load("bgmusic.mp3")
        pygame.mixer.music.play()
        bckImg = pygame.image.load('map1.png') # loading an image of the map
        pygame.font.init()   # font initialisation
        myfont = pygame.font.Font('font1.ttf', 65)  # different font sizes to choose from
        myfont1 = pygame.font.Font('font1.ttf', 40)
        myfont2 = pygame.font.Font('font1.ttf', 30)
        myfont3 = pygame.font.Font('font1.ttf', 32)
        title = myfont.render("IT BELONGS IN THE MUSEUM !", 1, (0,0,0)) #Rendering all of the titles in the main menu
        startTheGame = myfont1.render("PRESS 'ENTER' TO START", 1, (0,200,0))
        closeTheMenu = myfont2.render("PRESS 'Q' TO QUIT", 1, (180,0,0))
        chooseTheSprite = myfont3.render("PRESS 'C' TO CHANGE THE AI MODEL", 1, (0,100,0))
        ascending = myfont2.render("'A' for Ascending order ", 1, (0,0,0))
        descending = myfont2.render("'D' for Descending order", 1, (0,0,0))

        self.surface.blit(bckImg, (0,0))  #blitting the background
        self.surface.blit(title, (375,80)) #blitting the title
        self.surface.blit(startTheGame, ((500),700)) #blitting the titles in the main menu
        self.surface.blit(closeTheMenu, ((635),885))
        self.surface.blit(chooseTheSprite, ((450,800)))
        self.surface.blit(ascending, (940,400))
        self.surface.blit(descending, (930, 450))



    def process_input(self):
        for event in pygame.event.get(): # Menu control
            if event.type == pygame.KEYDOWN: 
                if (event.key == K_RETURN): #'Enter' starts the game
                    print("START GAME")
                    main.start()
                elif (event.key == K_c): #'c' transfers to menu to choose a sprite
                    spriteGUI.SpriteGui()
                elif (event.key == K_a):
                    config.ASCENDING = True
                elif (event.key == K_d):
                    config.ASCENDING = False
                elif (event.key == K_1) and config.x == True:
                    config.playerCh = 'player1.1.png' # 1, 2 or 3 chooses the sprite
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