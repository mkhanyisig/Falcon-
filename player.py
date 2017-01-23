
"""
For managing the player.
"""
import pygame
import constants
from spritesheet_functions import SpriteSheet

 
class Player(pygame.sprite.Sprite):

    # -- Methods
    def __init__(self):
 
        # Call the parent's constructor
        super(Player, self).__init__()

        # -- Attributes
        # Set speed of flapping of the player
        self.change_y = 0
        self.rising_rate = -8
        self.falling_rate = 4

        # change of level
        self.level = None
        # collision indicator
        self.collided = False

# ########handle the images #####
        # falcon flapping player sheet
        sprite_sheet = SpriteSheet("arts/graphics/falcon_spritesheet.png")
        # Hold images for the animated wings
        self.flying_frames = []

        # Load images for the bird
        falcon_up = sprite_sheet.get_image(5, 24, 122, 100)
        falcon_down = sprite_sheet.get_image(136, 92, 88, 68)
        # resize them
        falcon_up = pygame.transform.scale(falcon_up, (86, 70))
        falcon_down = pygame.transform.scale(falcon_down, (91, 70))
        # add them to the frames list
        self.flying_frames.append(falcon_up)
        self.flying_frames.append(falcon_down)
    
        # Set the image the player starts with
        self.image = self.flying_frames[1]
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # Move down
        self.rect.y += self.change_y

        # check if the bird touches the screen boundaries
        if self.rect.y < 0 or self.rect.y + self.rect.height > constants.SCREEN_HEIGHT:
            self.collided = True
            self.rect.y = self.rect.y       # freeze

        # check if there is collision with any obstacle
        for obs in self.level.get_obstacles():
            if pygame.sprite.collide_mask(self, obs) is not None:
                self.collided = True
                self.rect.y = self.rect.y  # freeze

    # when the up / spacebar is pressed, move player up and flap
    def flap(self):     
        self.change_y = self.rising_rate
        self.image = self.flying_frames[1]

    # when the up / spacebar is not pressed, move player down and release
    def release_wing(self):
        self.change_y = self.falling_rate
        self.image = self.flying_frames[0]
