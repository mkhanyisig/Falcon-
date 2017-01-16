"""
Module for managing obstacles.
"""
import pygame
import random
from spritesheet_functions import SpriteSheet

choose = random.randint(300,700)

# These constants define our obstacle types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite
#   [info one the sprite sheet]

BOTTOM       = (0,600,700,1) 
TOP          = (0,600,700,1)
BASE_OBS     = ()
FIXED_OBS    = ()
HORIZONTAL_MOV_OBS   = ()
VERTICAL_MOV_OBS    = ()
NEST         = ()


class Obstacle(pygame.sprite.Sprite):
 
    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super(Obstacle,self).__init__()
    
        sprite_sheet = SpriteSheet("arts/graphics/obstacle_sheet.png")

        # Grab the image for this obstacle
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
 
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class MovingPlatform(Obstacle):
    """ This is a fancier platform that can actually move. """
 
    def __init__(self, sprite_sheet_data):
 
        super().__init__(sprite_sheet_data)

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
 
        # # See if we hit the player
        # hit = pygame.sprite.collide_rect(self, self.player)
        # if hit:
        #     # We did hit the player. Shove the player around and
        #     # assume he/she won't hit anything else.
 
        #     # If we are moving right, set our right side
        #     # to the left side of the item we hit
        #     if self.change_x < 0:
        #         self.player.rect.right = self.rect.left
        #     else:
        #         # Otherwise if we are moving left, do the opposite.
        #         self.player.rect.left = self.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # # Check and see if we the player
        # hit = pygame.sprite.collide_rect(self, self.player)
        # if hit:
        #     # We did hit the player. Shove the player around and
        #     # assume he/she won't hit anything else.
 
        #     # Reset our position based on the top/bottom of the object.
        #     if self.change_y < 0:
        #         self.player.rect.bottom = self.rect.top
        #     else:
        #         self.player.rect.top = self.rect.bottom
 
        # # Check the boundaries and see if we need to reverse
        # # direction.
        # if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
        #     self.change_y *= -1
 
        # cur_pos = self.rect.x - self.level.world_shift
        # if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
        #     self.change_x *= -1


# class Nest(Platform):