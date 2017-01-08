# Falcon
# january 2017

# ################################# Setup ###################################

# useful imports
import sys
import pygame

# initialize pygame
pygame.init()

# initialize the fonts
try:
    pygame.font.init()
except:
    print "Fonts unavailable"
    sys.exit()

# global variables
ScrWidth = 800
ScrHeight = 600
FPS = 30
Gap = 100   # gap between obstacles?? Fixed, or not??


# ###################### Making Content #########################

# image, sound and hitmask  dicts
Images, Sounds, Hitmasks = {}, {}, {}

# player pic (may be a list)
Player = 'player.png'

# background (may be a list)
Background = 'bg.png'

# obstacle (may be a list)
Obstacle = 'obs.png'


def main():

    global Scr, FPSClock

    # create game clock
    FPSClock = pygame.time.Clock()
    # create a screen (width, height)
    Scr = pygame.display.set_mode((ScrWidth, ScrHeight))
    # set screen title
    pygame.display.set_caption('FALCON')

# #### Images ####
    # numbers sprites for score display
    Images['numbers'] = (
        pygame.image.load('pic.png').convert_alpha(),
        pygame.image.load('pic.png').convert_alpha(),
        pygame.image.load('pic.png').convert_alpha(),
        pygame.image.load('pic.png').convert_alpha(),
        pygame.image.load('pic.png').convert_alpha(),
        pygame.image.load('pic.png').convert_alpha(),
        pygame.image.load('pic.png').convert_alpha(),
        pygame.image.load('pic.png').convert_alpha(),
        pygame.image.load('pic.png').convert_alpha(),
        pygame.image.load('pic.png').convert_alpha()
    )

    # game over sprite
    Images['gameover'] = pygame.image.load('gameover.png').convert_alpha()
    # message sprite for welcome screen
    Images['message'] = pygame.image.load('message.png').convert_alpha()
    # base (ground) sprite
    Images['base'] = pygame.image.load('base.png').convert_alpha()

# ###### Sounds ######
    if 'win' in sys.platform:
        soundExt = '.wav'
    else:
        soundExt = '.ogg'

    Sounds['die'] = pygame.mixer.Sound('die' + soundExt)
    Sounds['hit'] = pygame.mixer.Sound('hit' + soundExt)
    Sounds['point'] = pygame.mixer.Sound('point' + soundExt)
    Sounds['high_score'] = pygame.mixer.Sound('high_score' + soundExt)
    Sounds['wing'] = pygame.mixer.Sound('wing' + soundExt)
    Sounds['buy'] = pygame.mixer.Sound('buy' + soundExt)

# ##########################

    # hitmask for obstacles
    # Sorry I don't know what to name the pictures in the dictionary
    Hitmasks['obs'] = (
        getHitmask(Images['obs'][0]),
        getHitmask(Images['obs'][1]),  # etc
        )

    # hitmask for player
    Hitmasks['player'] = (
        getHitmask(Images['player'][0]),
        )


def showScore(score):
    # displays score on the upper right corner
    # scoreDigits =
    return

        
def getHitmask(image):
    # returns a hitmask using an image's alpha
    mask = []
    for x in range(image.get_width()):
        mask.append([])
        for y in range(image.get_height()):
            mask[x].append(y) #or something else

    return mask

print "Terminating"
