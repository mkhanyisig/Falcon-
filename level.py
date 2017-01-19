"""
For managing levels.
"""

import pygame
import obstacles
import random
import constants


class Level:
    """ This is a generic super-class used to define a level.

        Create a child class for each level with level-specific
        info.
    """
 
    def __init__(self, player):
 
        # Lists of sprites used in all levels.
        self.obstacle_list = None
        # Background image
        self.background = None
 
        # How far the obstacles traveled
        self.obs_shift = 0
        self.obstacle_list = pygame.sprite.Group()
        self.level_limit = -1000
        self.player = player

        # obstacle related
        self.collection = []
        self.choices = []

        # solely for level change tests
        self.index = 0
        self.next_level = False

    # Update everything on this level
    def update(self):
        self.obstacle_list.update()

    # Draw everything on this level. 
    def draw(self, screen):
        # Draw the background
        # we do not move the background
        screen.fill((255, 255, 255))
        screen.blit(self.background, (0, 0))
 
        # Draw the sprite lists
        self.obstacle_list.draw(screen)
 
    def shift_obstacles(self, shift_x):
        # Keep track of the shift amount
        self.obs_shift -= shift_x
        self.obs_shift += shift_x

        # Go through all the sprite lists and shift
        for obstacle in self.obstacle_list:
            obstacle.rect.x -= shift_x

    def get_obstacles(self):
        return self.obstacle_list

    def fill_with_obstacles(self, obstacles_density):
        # List of "fixed" obstacles, and x, y location of the obstacle.
        for i in range(obstacles_density):
            choice = random.choice(self.collection)
            self.choices.append(choice)

        # Go through the list above, add obstacles
        for i in self.choices:
            # should import obstacle class
            block = obstacles.Obstacle(i[0])
            block.rect.x = random.randint(constants.SCREEN_WIDTH, constants.SCREEN_WIDTH*2)
            block.rect.y = random.randint(0, constants.SCREEN_HEIGHT)
            block.player = self.player
            self.obstacle_list.add(block)

    def replace_obstacle(self):
        new_block = obstacles.Obstacle(random.choice(self.choices)[0])
        new_block.rect.x = random.randint(constants.SCREEN_WIDTH, constants.SCREEN_WIDTH*2)
        new_block.rect.y = random.randint(0, constants.SCREEN_HEIGHT)
        new_block.player = self.player
        self.obstacle_list.add(new_block)


# Create obstacles for the level
class Level01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("arts/graphics/level1.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, constants.screenSize)
        self.background.set_colorkey((255, 255, 255))
        self.level_limit = -2000

        # List of "fixed" obstacles, and x, y location of the obstacle.
        self.collection = [[obstacles.BASE_OBS], [obstacles.FIXED_OBS]]  # may have more
        # fill level with obstacles
        self.fill_with_obstacles(2)

    def update(self):

        # get the update function
        # remove any obstacles that are too far left
        # according to the level rules, make new obstacles
        Level.update(self)

        for block in self.obstacle_list:
            if block.rect.x + block.rect.width < 0:
                self.obstacle_list.remove(block)
                # replace the lost block
                self.replace_obstacle()

                # to check for level changes
                self.index += 1
                if self.index == 5:
                    self.next_level = True

        # level rules?
        #  make a new obstacle every 3s (maybe)
        #  make a new obstacle with some probability
        #  change the kind of obstacles based on randomization/choice
        #  change the placement of obstacles (close together/far apart)
        #  set placement based on player position
        #  give obstacles different speeds


# Create obstacles for the level
class Level02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("arts/graphics/Paris.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, constants.screenSize)
        self.background.set_colorkey((255, 255, 255))
        self.level_limit = -2000

        # List of "fixed" obstacles, and x, y location of the obstacle.
        self.collection = [[obstacles.BASE_OBS], [obstacles.FIXED_OBS]]  # may have more
        # fill it up
        self.fill_with_obstacles(3)
        # Add a custom moving obstacle
        block = obstacles.MovingObstacle(obstacles.HORIZONTAL_MOV_OBS)
        block.rect.x = 900
        block.rect.y = 280
        block.boundary_left = 900
        block.boundary_right = 1600
        block.change_x = -5
        block.player = self.player
        block.level = self
        self.obstacle_list.add(block)

    def update(self):

        # get the update function
        # remove any obstacles that are too far left
        # according to the level rules, make new obstacles

        Level.update(self)

        for block in self.obstacle_list:
            if block.rect.x + block.rect.width < 0:
                self.obstacle_list.remove(block)
                # replace the lost block
                self.replace_obstacle()
