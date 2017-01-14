
import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the height and width of the screen
screenSize = [700, 500]
screen = pygame.display.set_mode(screenSize)
 
pygame.display.set_caption("Instruction Screen")


# -------- Load Up Files -----------

#     load up the images
gameover = pygame.image.load("gameover.png").convert_alpha()
welcome = pygame.image.load("welcome.png").convert_alpha()
level1 = pygame.image.load("level1.png").convert_alpha()

# scale down the pictures
gameover = pygame.transform.scale(gameover, screenSize)
welcome = pygame.transform.scale(welcome, screenSize)
level1 = pygame.transform.scale(level1, screenSize)

# Define the sounds
flapSound = pygame.mixer.Sound("swoosh.wav")
scoreSound = pygame.mixer.Sound("score.wav")
startSound = pygame.mixer.Sound("Begin.wav")
L1Sound = pygame.mixer.Sound("MountainSoundTrackV2.wav")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Starting position of the rectangle
rect_x = 50
rect_y = 50
 
# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
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
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
 
    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y
 
    # Bounce the ball if needed
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()