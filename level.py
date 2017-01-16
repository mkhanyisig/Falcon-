import pygame
import obstacles

class Level():
    """ This is a generic super-class used to define a level.
    	Create a child class for each level with level-specific
    	info. 
    """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. 
        	Needed for when moving platforms
            collide with the player. 
        """
 
        # Lists of sprites used in all levels.

        self.obstacle_list = None
        # Background image
        self.background = None
 
        # How far this world has been scrolled left/right
        self.obs_shift = 0
        self.level_limit = -1000
        self.obstacle_list = pygame.sprite.Group()
        self.player = player
 
    # Update everything on this level
    def update(self):
        """ Update everything in this level."""

        self.obstacle_list.update()

 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill((255,255,255))
        screen.blit(self.background)
 
        # Draw all the sprite lists that we have
        self.obstacle_list.draw(screen,(0,0))
 
    def shiftObs(self, shift_x):

        # Keep track of the shift amount
        self.obs_shift -= shift_x
 
        # Go through all the sprite lists and shift
        for obstacle in self.obstacle_list:
            obstacle.rect.x -= shift_x
 
# Create obstacles for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("arts/graphics/level1.png").convert()
        self.background.set_colorkey((255,255,255))
        self.level_limit = -2500
 
        # Array with type of obstacles, and x, y location of the obstacle.
        
        level = [ [obstacles.BOTTOM, 0,500],
        		  [obstacles.TOP,0,0 ],
                  ]
        
 
 
        # Go through the array above and add obstacles
        for obstacle in level:
        	# should import obstacle class
            block = obstacle.Obstacle(obstacle[0])
            block.rect.x = obstacle[1]
            block.rect.y = obstacle[2]
            block.player = self.player
            self.obstacle_list.add(block)
 
        # Add a custom moving obstacle
        # block = obstacle.MovingObstacle(obstacle)#something on the sprite sheet)
        # block.rect.x = 1350
        # block.rect.y = 280
        # block.boundary_left = 1350
        # block.boundary_right = 1600
        # block.change_x = 1
        # block.player = self.player
        # block.level = self
        # self.obstalce_list.add(block)
 
 
# Create obstacles for the level
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 2. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("#name").convert()
        self.background.set_colorkey((255,255,255))
        self.level_limit = -1000
 
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


