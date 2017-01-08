#Setup
import sys
import pygame

FPS = 30
SCREENWIDTH  = 800
SCREENHEIGHT = 600
# amount by which base can maximum shift to left
GAPSIZE  = 100 # gap between obstacles??

# image, sound and hitmask  dicts
IMAGES, SOUNDS, HITMASKS = {}, {}, {}



def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('FALCON')
    
    # numbers sprites for score display
    IMAGES['numbers'] = (
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
    IMAGES['gameover'] = pygame.image.load('gameover.png').convert_alpha()
    # message sprite for welcome screen
    IMAGES['message'] = pygame.image.load('message.png').convert_alpha()
    # base (ground) sprite
    IMAGES['base'] = pygame.image.load('base.png').convert_alpha()

    # sounds
    if 'win' in sys.platform:
        soundExt = '.wav'
    else:
        soundExt = '.ogg'

    SOUNDS['die']    = pygame.mixer.Sound('die' + soundExt)
    SOUNDS['hit']    = pygame.mixer.Sound('hit' + soundExt)
    SOUNDS['point']  = pygame.mixer.Sound('point' + soundExt)
    SOUNDS['high_score'] = pygame.mixer.Sound('high_score' + soundExt)
    SOUNDS['wing']   = pygame.mixer.Sound('wing' + soundExt)
    SOUNDS['buy']    = pygame.mixer.Sound('buy' + soundExt)

        # hismask for obstacles
        HITMASKS['pipe'] = (
            getHitmask(IMAGES['obs'][0]),
            getHitmask(IMAGES['obs'][1]),
        )

        # hitmask for player
        HITMASKS['player'] = (
            getHitmask(IMAGES['player'][0]),
        )


