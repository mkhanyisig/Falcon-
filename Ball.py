import pygame
from random import randint

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)


# #def obstacle(xloc, yloc, xsize, ysize):
#     # above the screen
#     sky = pygame.draw.rect(screen, black, [0, 0, 700, 0])
#     # Mountain
#     mountain = pygame.draw.rect(screen, green, [xloc, int(yloc+ysize), xsize,ysize+500])
#     # the ground
#     ground = pygame.draw.rect(screen, black, [0, 499, 700, 1])


def Score(score):
    font = pygame.font.SysFont(None, 75)
    text = font.render("Distance: "+str(score), True, red)
    screen.blit(text, [0,0])






def main():

    global screen, clock
    pygame.init()

    size = 700,500
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()


    pygame.display.set_caption("test")


    x = 350
    y = 250
    x_speed = 0
    y_speed = 0
    # ground = 477
    xloc = 700
    yloc = 0
    xsize = 70
    ysize = randint(150,450)
    space = 150
    obspeed = 2.5
    score = 0


    done = False
    phase = "start"

    while not done:
        if phase == "start":
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    done = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    phase = "play"
                    # clear screen
                    # content - cut scene (may need additionally phase)


            

        elif phase == "play":
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_speed = -10

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        y_speed = 5

        elif phase == "end":
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    done = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    phase = "play"


            screen.fill(white)
            obstacle1(xloc, yloc, xsize, ysize)
            obstacle2(xloc, yloc, xsize, ysize)
            obstacle3(xloc, yloc, xsize, ysize)
            bird(x,y)
            Score(score)

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

            if bird(x,y).colliderect(obstacle1(xloc,yloc,xsize,ysize)) or bird(x,y).colliderect(obstacle2(xloc,yloc,xsize,ysize)) or bird(x,y).colliderect(obstacle3(xloc,yloc,xsize,ysize)) :
                gameover()
                obspeed = 0
                y_speed = 0

            if xloc < -80:
                xloc = 700
                ysize = randint(150,450)

            if x > xloc and x < xloc+3:
                score = (score + 1)

        pygame.display.update()
        clock.tick(60)

def bird(x,y):
        pygame.draw.rect(screen,black,[x,y, 20,10])
        return pygame.draw.rect(screen,black,[x,y, 20,10])
        

def gameover():
    font = pygame.font.SysFont(None, 75)
    text = font.render("Game over", True, red)
    screen.blit(text, [150, 250])
    phase = "end"
    pygame.display.update()


#This obstacle is our sky
def obstacle1(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen, black, [0, 0, 700, 0])
    return pygame.draw.rect(screen, black, [0, 0, 700, 0])

#this obstacle is our moutain
def obstacle2(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen, green, [xloc, int(yloc+ysize), xsize,ysize+500])
    return pygame.draw.rect(screen, green, [xloc, int(yloc+ysize), xsize,ysize+500])

#this obstacle is our ground
def obstacle3(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen, black, [0, 499, 700, 1])
    return pygame.draw.rect(screen, black, [0, 499, 700, 1])

if __name__ == '__main__':
    main()

