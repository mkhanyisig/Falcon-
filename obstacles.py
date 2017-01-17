"""
For managing obstacles.
"""
import pygame
import random
from spritesheet_functions import SpriteSheet



# These constants define our obstacle types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite
#   [info one the sprite sheet]


BASE_OBS     = (432, 720, 70, 40) # mountains
FIXED_OBS    = (504, 576, 70, 70) # clouds, things that are floating
HORIZONTAL_MOV_OBS   = (432, 720, 70, 40) 
# VERTICAL_MOV_OBS    = ()
# NEST         = ()


class Obstacle(pygame.sprite.Sprite):
 
    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super(Obstacle,self).__init__()
    
        sprite_sheet = SpriteSheet("arts/graphics/Obstacles/sprite_sheet_threeobjects.png")
        # sprite_sheet = SpriteSheet("arts/graphics/tiles_spritesheet.png")

        # Grab the image for this obstacle
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

 
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

# ------------------------- Not in use -------------------------
class MovingObstacle(Obstacle):

    # This is a fancier obstacle that can move relatively faster
    # or in different directions. 

    def __init__(self, sprite_sheet_data):
 
        super(MovingObstacle,self).__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0
 
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
 
        self.level = None
        self.player = None
 
    def update(self):

        # Move left/right
        self.rect.x += self.change_x
        # Move up/down
        self.rect.y += self.change_y
        # # Check the boundaries and see if we need to reverse
        # # direction.
        # if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
        #     self.change_y *= -1
 
        # cur_pos = self.rect.x - self.level.world_shift
        # if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
        #     self.change_x *= -1
