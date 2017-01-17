

import pygame
import level
# import platforms 
from spritesheet_functions import SpriteSheet

 
class Player(pygame.sprite.Sprite):
    """ 
        This class represents the bar at the bottom that the player
        controls. 
    """
    state = None
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super(Player,self).__init__()
 
        # -- Attributes
        # Set speed vector of player
        self.change_y = 5
 
        # This holds all the images for the animated flappying of wings 
        self.flying_frames = []
    
 
        # # What direction is the player facing?
        # self.direction = "R"
 
        # List of sprites that will kill the bird
        # (Should these sprites be the floor and ceiling?
        # Then what about the moving obstacles.)

        self.level = None
        #falcon flapping player sheet
        sprite_sheet = SpriteSheet("arts/graphics/falcon_spritesheet.png")

        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 130, 180)
        self.flying_frames.append(image)
        image = sprite_sheet.get_image(130, 0, 110, 180)
        self.flying_frames.append(image)        

    
        # Set the image the player starts with
        self.image = self.flying_frames[1]

 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
 
        # # Move left/right
        # self.rect.x += self.change_x
        # pos = self.rect.x + self.level.world_shift
        # if self.direction == "R":
        #     frame = (pos // 30) % len(self.walking_frames_r)
        #     self.image = self.walking_frames_r[frame]
        # else:
        #     frame = (pos // 30) % len(self.walking_frames_l)
        #     self.image = self.walking_frames_l[frame]

        # # See if we hit anything
        # block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        # for block in block_hit_list:
        #     # If we are moving right,
        #     # set our right side to the left side of the item we hit
        #     if self.change_x > 0:
        #         self.rect.right = block.rect.left
        #     elif self.change_x < 0:
        #         # Otherwise if we are moving left, do the opposite.
        #         self.rect.left = block.rect.right
 
        # Move down
        self.rect.y += self.change_y

        #Iterate through images to show animation
        pos = self.rect.y 
        frame = (pos//300)

        self.image = self.flying_frames[frame]


        # Check and see if we hit obstacles, 
        # if there is a collision

        # if self.rect.y < 0 or self.rect.y > 400:
        #     # gameover page
        #     pygame.quit()
        # for obs in level.Level.obstacle_list:
        #     if pygame.sprite.collide_mask(self, obs) != None:
        #         # gameover page
        #         pygame.quit()


        #     elif pygame.sprite.collide_mask(self, obs) != None:
        #         # want to show congrats page in main.py
        #         state == 'congrats'

        # # If hit the nest, go to the next level
        # elif pygame.sprite.collide_mask(self, platforms.Nest) == True:
        #     self.level




        # controls for when the player hits the up arrow.
    def flap(self):     
        # player moves up a certain amount when up arrow is clicked
        self.change_y = -10



 
        
 
    
 
    
 
    
