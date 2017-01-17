"""
For managing levels.
"""

import pygame
import obstacles
import random

class Level():
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

   # Update everything on this level
    def update(self):

        self.obstacle_list.update()


    # Draw everything on this level. 
    def draw(self, screen):
 
        # Draw the background
        # we donot move the background
        screen.fill((255,255,255))
        screen.blit(self.background,(0,0))
 
        # Draw the sprite lists
        self.obstacle_list.draw(screen)
 
    def shiftObs(self, shift_x):

        # Keep track of the shift amount
        self.obs_shift += shift_x
 
        # Go through all the sprite lists and shift
        for obstacle in self.obstacle_list:
            obstacle.rect.x -= shift_x


    def getObsList(self):
        return self.obstacle_list

 
# Create obstacles for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("arts/graphics/level1.png").convert()
        self.background.set_colorkey((255,255,255))
        self.level_limit = -2000

        # List of "fixed" obstacles, and x, y location of the obstacle.

        self.collection = [ [obstacles.BASE_OBS ],
                  [obstacles.FIXED_OBS], 
                  # may have more
                  ]

        self.choices = []

        for i in range(1):
            choice = random.choice(self.collection)
            print choice
            self.choices.append(choice)


        # Go through the list above, add obstacles

        for i in self.choices:
            # should import obstacle class
            block = obstacles.Obstacle(i[0])
            block.rect.x = random.randint(400,1000)
            block.rect.y = random.randint(0,500)
            block.player = self.player
            self.obstacle_list.add(block)

 
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
            if self.obs_shift > 1000:
                self.obstacle_list.remove(block)

                # newBlock = obstacles.Obstacle(obstacles.FIXED_OBS)
                # newBlock.rect.x = random.randint(400,1000)
                # newBlock.rect.y = random.randint(0,500)
                # newBlock.player = self.player
                # self.obstacle_list.add(newBlock)

                print self.obstacle_list
                


        # level rules?
        #  make a new obstacle every 3s (maybe)
        #  make a new obstacle with some probability
        #  change the kind of obstacles based on randomization/choice
        #  change the placement of obstacles (close together/far apart)
        #  set placement based on player position
        #  give obstacles different speeds


# Create obstacles for the level
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 2. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("arts/graphics/level1.png").convert()
        self.background.set_colorkey((255,255,255))

 
        # Array with type of obstacles, and x, y location of the obstacle.
        '''
        level = [ [1st obstacle],
        			[],
        			[],
        			[]
                  ]
        '''
        # Go through the array above and add platforms
        #for 
 
        # # Add a custom moving platform
        # block = obstacle.MovingObstacle(obstacle.#something on the sprite sheet)
        # block.rect.x = 1350
        # block.rect.x = 1500
        # block.rect.y = 300
        # block.boundary_top = 100
        # block.boundary_bottom = 550
        # block.change_y = -1
        # block.player = self.player
        # block.level = self
        # self.obstacle_list.add(block)


