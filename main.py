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

