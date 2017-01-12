# Falcon game
# January 2017

import pygame
import sys
from random import randint

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)


def main():

    global screen, clock
    # initialize pygame
    pygame.init()
    # initialize the fonts
    try:
        pygame.font.init()
    except:
        print "Fonts unavailable"
        sys.exit()

    # screenSize (width, height)
    screenSize = (700, 600)
    # make a game screen of screenSize
    screen = pygame.display.set_mode(screenSize)
    # title of window to be displayed
    pygame.display.set_caption("test")
    # make a game clock
    clock = pygame.time.Clock()

# ################## load up all useful graphics, sound, etc here #######################
#     load up the images
    gameover = pygame.image.load("gameover.png").convert_alpha()
    welcome = pygame.image.load("welcome.png").convert_alpha()
    level1 = pygame.image.load("level1.png").convert_alpha()
    # scale down the pictures
    gameover = pygame.transform.scale(gameover, screenSize)
    welcome = pygame.transform.scale(welcome, screenSize)
    level1 = pygame.transform.scale(level1, screenSize)

    x = 350
    y = 250
    # x_speed = 0
    y_speed = 0
    # ground = 477
    xloc = 700
    yloc = 0
    xsize = 70
    ysize = randint(150, 450)
    # space = 150
    obspeed = 2.5
    score = 0

    phase = "start"

    while True:
        # start phase
        if phase == "start":
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                    phase = "play"

                    # content - cut scene (may need additionally phase)

            # clear screen
            screen.fill((255, 255, 255))
            # draw the welcome page
            screen.blit(welcome, (0, 0))

        # play phase
        elif phase == "play":

            # add the background
            screen.blit(level1, (0, 0))

            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        y_speed = -10

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        y_speed = 5

            # this block is redundant since we draw the objects whenever we check for collisions
            # we shall redesign later

            # draw the stuff on the screen
            # obstacle1(xloc, yloc, xsize, ysize)
            # obstacle2(xloc, yloc, xsize, ysize)
            # obstacle3(xloc, yloc, xsize, ysize)
            # bird(x, y)

            # control the bird speed
            y += y_speed
            xloc -= obspeed


            # check for crashes between bird and obstacles
            if bird(x, y).colliderect(obstacle1(xloc, yloc, xsize, ysize)) or bird(x, y).colliderect(obstacle2(xloc, yloc, xsize, ysize))\
                    or bird(x, y).colliderect(obstacle3(xloc, yloc, xsize, ysize)):
                # pause for effect after crashing
                pygame.time.wait(700)
                obspeed = 0
                y_speed = 0

                # go to end phase
                phase = "end"

            # draw next obstacle after one leaves the screen
            if xloc < -80:
                xloc = 700
                ysize = randint(150, 450)

            # check for score based on distance

            showTheScore(score)
            if xloc < x < xloc+3:
                score = (score + 1)

        # end phase
        elif phase == "end":
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                    # replay the game
                    main()
                    # phase = "start"

            # clear the screen with white first
            screen.fill((255, 255, 255))
            # draw the game over screen
            screen.blit(gameover, (0, 0))
            # showTheScore(score)

        pygame.display.update()
        clock.tick(60)


# shows the score
def showTheScore(score):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Distance: "+str(score), True, red)
    screen.blit(text, (10, 10))


# this is the flying bird
def bird(x, y):
    return pygame.draw.rect(screen, black, [x, y, 20, 10])


# obstacle (sky)
def obstacle1(xloc, yloc, xsize, ysize):
    return pygame.draw.rect(screen, black, [0, 0, 700, 0])


# mountain obstacle
def obstacle2(xloc, yloc, xsize, ysize):
    return pygame.draw.rect(screen, green, [xloc, int(yloc+ysize), xsize, ysize+500])


# ground obstacle
def obstacle3(xloc, yloc, xsize, ysize):
    return pygame.draw.rect(screen, black, [0, 499, 700, 1])


if __name__ == '__main__':
    main()

