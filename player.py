
"""
For managing the player.
"""
import pygame
import constants
import sys
from spritesheet_functions import SpriteSheet

 
class Player(pygame.sprite.Sprite):

    # -- Methods
    def __init__(self):
 
        # Call the parent's constructor
        super(Player, self).__init__()

        # -- Attributes
        # Set speed of flapping of the player
        self.change_y = 0

        # change of level
        self.level = None

# ########handle the images #####
        # falcon flapping player sheet
        sprite_sheet = SpriteSheet("arts/graphics/falcon_spritesheet.png")
        # Hold images for the animated wings
        self.flying_frames = []

        # Load images for the bird
        falconUp = sprite_sheet.get_image(0, 0, 130, 180)
        self.flying_frames.append(falconUp)
        falconDown = sprite_sheet.get_image(130, 0, 110, 180)
        self.flying_frames.append(falconDown)
    
        # Set the image the player starts with
        self.image = self.flying_frames[1]
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # Move down
        self.rect.y += self.change_y

        # check if the bird touches the screen boundaries  ## needs to be revised
        if self.rect.y < 0 or self.rect.y > constants.SCREEN_HEIGHT:
            # gameover page
            print "gameover"
            pygame.quit()
            sys.exit()

        # check if there is collision with any obstacle
        for obs in self.level.getObsList():
            if pygame.sprite.collide_mask(self, obs) is not None:
                # gameover page
                print "gameover"
                pygame.quit()
                sys.exit() 

            # elif pygame.sprite.collide_mask(self, obs) != None:
                # want to show congrats page in main.py

        # # If hit the nest, go to the next level
        # elif pygame.sprite.collide_mask(self, platforms.Nest) == True:
        #     self.level

    # when the up / spacebar is pressed, move player up and flap
    def flap(self):     
        self.change_y = -10
        self.image = self.flying_frames[1]

    # when the up / spacebar is not pressed, move player down and release
    def releaseWing(self):
        self.change_y = 5
        self.image = self.flying_frames[0]




 
        
 
    
 
    
 
    
