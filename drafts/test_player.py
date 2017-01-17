# main program


import pygame
import sys
from random import randint

from player import Player

# Set up some values
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
# make a game screen of screenSize
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# title of window to be displayed
pygame.display.set_caption("test-run Falcon with sprite sheets")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def main():
    """ Main Program """
    pygame.init()
    done = False
    # Create the player
    player = Player()

    player.rect.x = 100
    player.rect.y = 250

    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(player)

 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
 
            if event.type == pygame.KEYDOWN:
            	if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                	player.flap()
            if event.type == pygame.KEYUP:
            	if event.key == pygame.K_UP or event.key == pygame.K_SPACE:

            		player.change_y = 5

					

 
        # Update the player.
        active_sprite_list.update()
		


 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        screen.fill(WHITE)
        active_sprite_list.draw(screen)



 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
