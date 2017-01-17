
"""
For managing the player.
"""
import pygame
import level
import obstacles
from spritesheet_functions import SpriteSheet

 
class Player(pygame.sprite.Sprite):

    # -- Methods
    def __init__(self):
 
        # Call the parent's constructor
        super(Player,self).__init__()
 
        # -- Attributes
        # Set speed of flappying of the player
        self.change_y = 0
 
        # Hold images for the animated wings
        self.flying_frames = []

        # change of level
        self.level = None

        #falcon flapping player sheet
        sprite_sheet = SpriteSheet("arts/graphics/falcon_spritesheet.png")

        # Load 
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



 
        
 
    
 
    
 
    
