import pygame
import time
import random
 
pygame.init()
 
display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
Bright_green = (0,255,0)
 
block_color = (53,115,255)
 
car_width = 73
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('THE GAME NAME')
clock = pygame.time.Clock()
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("THE GAME NAME", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        if 350+100 > mouse[0] > 350 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, Bright_green,(350,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, green,(350,450,100,50))
            
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Start!", smallText)
        textRect.center = ( (350+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
        pygame.display.update()
        clock.tick(15)
        
game_intro()
pygame.quit()
quit()
