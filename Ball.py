import pygame
from random import randint

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)


# #def obstacle(xloc, yloc, xsize, ysize):
#     # above the screen
#     sky = pygame.draw.rect(screen, black, [0, 0, 700, 0])
#     # Mountain
#     mountain = pygame.draw.rect(screen, green, [xloc, int(yloc+ysize), xsize, ysize+500])
#     # the ground
#     ground = pygame.draw.rect(screen, black, [0, 499, 700, 1])

def main():

    global screen, clock
    pygame.init()

    size = (700, 600)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # load up all useful graphics, sound, etc here
    gameover = pygame.image.load("gameover.png").convert_alpha()
    welcome = pygame.image.load("welcome.png").convert_alpha()
    # scale down the pictures
    gameover = pygame.transform.scale(gameover, size)
    welcome = pygame.transform.scale(welcome, size)
    # title of window to be displayed
    pygame.display.set_caption("test")

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_speed = -10

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        y_speed = 5

            # draw the stuff on the screen
            screen.fill(white)
            obstacle1(xloc, yloc, xsize, ysize)
            obstacle2(xloc, yloc, xsize, ysize)
            obstacle3(xloc, yloc, xsize, ysize)
            bird(x, y)
            showTheScore(score)

            y += y_speed
            xloc -= obspeed

            # if y > ground:
            #     gameover()
            #     y_speed = 0
            #     obspeed = 0


            # if x+20 > xloc and x-20 < xsize+xloc or y+20 > ysize+space:
            #     gameover()
            #     obspeed = 0
            #     y_speed = 0

            # check for crashes
            if bird(x, y).colliderect(obstacle1(xloc, yloc, xsize, ysize)) or bird(x, y).colliderect(obstacle2(xloc, yloc, xsize, ysize)) or bird(x, y).colliderect(obstacle3(xloc, yloc, xsize, ysize)) :
                # gameover()
                # go to end phase instead
                phase = "end"
                obspeed = 0
                y_speed = 0

            if xloc < -80:
                xloc = 700
                ysize = randint(150, 450)

            # check for score based on distance
            if xloc < x < xloc+3:
                score = (score + 1)

        # end phase
        elif phase == "end":
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                    phase = "start"
            # draw the game over screen
            # clear the screen with white first
            screen.fill((255, 255, 255))
            screen.blit(gameover, (0, 0))

        pygame.display.update()
        clock.tick(60)


# shows the score
def showTheScore(score):
    font = pygame.font.SysFont(None, 75)
    text = font.render("Distance: "+str(score), True, red)
    screen.blit(text, [0, 0])


# this is the flying bird
def bird(x, y):
        pygame.draw.rect(screen, black, [x, y, 20, 10])
        return pygame.draw.rect(screen, black, [x, y, 20, 10])


# obstacle (sky)
def obstacle1(xloc, yloc, xsize, ysize):
    pygame.draw.rect(screen, black, [0, 0, 700, 0])
    return pygame.draw.rect(screen, black, [0, 0, 700, 0])


# mountain obstacle
def obstacle2(xloc, yloc, xsize, ysize):
    pygame.draw.rect(screen, green, [xloc, int(yloc+ysize), xsize, ysize+500])
    return pygame.draw.rect(screen, green, [xloc, int(yloc+ysize), xsize, ysize+500])


# ground obstacle
def obstacle3(xloc, yloc, xsize, ysize):
    pygame.draw.rect(screen, black, [0, 499, 700, 1])
    return pygame.draw.rect(screen, black, [0, 499, 700, 1])


if __name__ == '__main__':
    main()

