
"""
For managing obstacles.
"""
import pygame
from spritesheet_functions import SpriteSheet


# These constants define our obstacle types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite
#   [info on the sprite sheet]

# MOUNTAIN LEVEL
PLANE = (162, 0, 126, 60)
CLOUD = (288.5, 0, 87, 60)

MOUNTAIN = (0, 75, 160, 225)

# PARIS 
CROISSANT = (0, 0, 40, 60)
CHEESE2 = (41.5, 0, 57.5, 60)
CHEESE = (99, 0, 62, 60)
BREAD = (35, 306, 50, 75)
BOTTLE = (0, 305, 35, 75)

TOWER = (160, 75, 160, 225)

# NEW YORK
APPLE = (375, 0, 50, 55)
TAXI = (0, 380, 60, 50)
HAT = (430,0,70,55)
BURGER = (500,0,55,55)
FRIES =  (560,0,43,55)

STATUE_OF_LIBERTY = (745,70,85,225)
EMPIRE_STATE_BUILDING = (317.5, 75, 142.5, 225)

# EGYPT

HEAD = (85,305,60,75)
PYRAMID = (145,306,55,65)

MONUMENT =(460,70,285,295)

# BEIJING

MASK1 = (200,310,70,80)
MASK2 = (270,310,70,80)
MASK3 = (340,310,70,80)
BOOK = (675,0,70,55)
LUCKY_BAG = (605,0,70,55)
KNOT = (410,310,50,80)

TV_TOWER = (830,70,150,225)


class Obstacle(pygame.sprite.Sprite):
 
    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super(Obstacle, self).__init__()
    
        # sprite_sheet = SpriteSheet("arts/graphics/Obstacles/sprite_sheet_threeobjects.png")

        # temporary obstacles
        sprite_sheet = SpriteSheet("arts/graphics/obstacles_sprite_sheet.png")

        # Grab the image for this obstacle
        self.image = sprite_sheet.get_image(sprite_sheet_data[0], 
                                            sprite_sheet_data[1], 
                                            sprite_sheet_data[2], 
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class MovingObstacle(Obstacle):

    # This is a fancier obstacle that can move relatively faster
    # or in different directions. 

    def __init__(self, sprite_sheet_data):
 
        super(MovingObstacle, self).__init__(sprite_sheet_data)

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
