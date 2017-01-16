# main program


import pygame
import sys
from random import randint
import level
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
# make a game clock
clock = pygame.time.Clock()
#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Load Up Files -----------

#     load up the images
gameover = pygame.image.load("arts/graphics/gameover.png").convert_alpha()
welcome = pygame.image.load("arts/graphics/welcome.png").convert_alpha()
level1 = pygame.image.load("arts/graphics/level1.png").convert_alpha()

# scale down the pictures
gameover = pygame.transform.scale(gameover, screenSize)
welcome = pygame.transform.scale(welcome, screenSize)
level1 = pygame.transform.scale(level1, screenSize)

# Define the sounds
flapSound = pygame.mixer.Sound("arts/audio/swoosh.wav")
scoreSound = pygame.mixer.Sound("arts/audio/score.wav")
startSound = pygame.mixer.Sound("arts/audio/Begin.wav")
L1Sound = pygame.mixer.Sound("arts/audio/MountainSoundTrackV2.wav")
#L2Sound = ...


display_instructions = True
instruction_page = 1
 
# Play Music "Begin.wav"
startSound.play(loops=-1, maxtime=0, fade_ms=0)


# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
        (event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_ESCAPE)):
            done = True
        if event.type ==  pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False
                startSound.stop()
                L1Sound.play(loops=-1, maxtime=0, fade_ms=0)


 
    # Set the screen background
    screen.fill(BLACK)
 
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.

        screen.blit(welcome, [0,0])
 
 
    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render("Page 2 is a storyline picture.",True, WHITE)
        screen.blit(text, [10, 10])
        text = font.render("Also describe controls.", True, WHITE)
        screen.blit(text, [10, 50])
        text = font.render("Can add Page 3 if needed.", True, WHITE)
        screen.blit(text, [10, 90])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


def main():
    """ Main Program """
    pygame.init()

    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 

 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
 
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    player.flap()
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
  
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
 
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

       
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
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