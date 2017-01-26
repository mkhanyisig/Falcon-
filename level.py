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
		self.player = player

		# obstacle related
		self.collection = []
		self.obstacle_options = []
		self.obstacle_type = None

		# solely for level change tests
		self.index = 0
		self.next_level = False
		self.maximum = 10

		# sounds
		self.score_sound = pygame.mixer.Sound("arts/audio/score.wav")
		self.level_soundtrack = None

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
		# Go through all the sprite lists and shift
		for obstacle in self.obstacle_list:
			obstacle.rect.x -= shift_x

	def get_obstacles(self):
		return self.obstacle_list

	def fill_with_flying_obstacles(self, obstacles_density):
		# List of "fixed" obstacles, and x, y location of the obstacle.
		for i in range(obstacles_density):
			choice = random.choice(self.collection)
			self.obstacle_options.append(choice)

		# Go through the list above, add obstacles
		for i in self.obstacle_options:
			# should import obstacle class
			obstacle = obstacles.Obstacle(i[0])
			obstacle.rect.x = random.randint(constants.SCREEN_WIDTH, constants.SCREEN_WIDTH*2)
			obstacle.rect.y = random.randint(0, constants.SCREEN_HEIGHT/2)
			obstacle.player = self.player
			self.obstacle_list.add(obstacle)

	def make_flying_obstacle(self):
		obstacle = obstacles.Obstacle(random.choice(self.obstacle_options)[0])
		obstacle.rect.x = random.randint(constants.SCREEN_WIDTH, constants.SCREEN_WIDTH*2)
		obstacle.rect.y = random.randint(0, constants.SCREEN_HEIGHT/2)
		obstacle.player = self.player
		self.obstacle_list.add(obstacle)

	def make_ground_obstacle(self, obstacle_type):
		obstacle = obstacle_type
		obstacle.rect.x = random.randint(constants.SCREEN_WIDTH, constants.SCREEN_WIDTH*2)
		obstacle.rect.y = constants.SCREEN_HEIGHT-225  # subtract some more to account for the base (river, road etc)
		obstacle.player = self.player
		self.obstacle_list.add(obstacle)

	# Make a horizontally or vertically moving obstacle
	# name should be 'obstacles.***'
	# pos_x and pos_y : initial position for the obstacle
	# change_x should be negative to move faster to the left
	# change_y should be positive to move downward

	def make_special_obstacle(self, name, change_x, change_y):
		obstacle = obstacles.MovingObstacle(name)
		obstacle.rect.x = random.randint(constants.SCREEN_WIDTH*1.5, constants.SCREEN_WIDTH*5)
		obstacle.rect.y = random.randint(constants.SCREEN_HEIGHT/4, 3*constants.SCREEN_HEIGHT / 4)
		obstacle.boundary_top = 0
		obstacle.boundary_bottom = 300
		obstacle.boundary_left = 0
		obstacle.boundary_right = None
		obstacle.change_x = change_x
		obstacle.change_y = change_y
		obstacle.player = self.player
		obstacle.level = self
		self.obstacle_list.add(obstacle)


# mountains level
class Level01(Level):
	""" Definition for level 1. """
 
	def __init__(self, player):
		""" Create level 1. """
 
		# Call the parent constructor
		Level.__init__(self, player)
 
		self.background = pygame.image.load("arts/graphics/level1.png").convert_alpha()
		self.background = pygame.transform.scale(self.background, constants.screenSize)
		self.background.set_colorkey((255, 255, 255))

		self.level_soundtrack = pygame.mixer.Sound("arts/audio/level_one.wav")

		# List of "fixed" obstacles, and x, y location of the obstacle.
		self.collection = [[obstacles.CLOUD]]
		self.obstacle_type = obstacles.Obstacle([obstacles.MOUNTAIN][0])
		# fill level with obstacles and add the ground obstacle
		self.fill_with_flying_obstacles(1)
		self.maximum = 5

	def update(self):
		Level.update(self)

		for obstacle in self.obstacle_list:
			if obstacle.rect.x + obstacle.rect.width < 0:
				self.obstacle_list.remove(obstacle)
				# replace the lost obstacle with either flying or ground obstacle
				if random.random() < 0.5:
					self.make_flying_obstacle()
				else:
					self.make_ground_obstacle(self.obstacle_type)

				# to check for level changes
				self.index += 1
				self.score_sound.play()
				if self.index == self.maximum:
					self.next_level = True

		# level rules?
		#  make a new obstacle every 3s (maybe) 
		#  make a new obstacle with some probability
		#  change the kind of obstacles based on randomization/choice
		#  change the placement of obstacles (close together/far apart)
		#  set placement based on player position
		#  give obstacles different speeds

		#			  suggestion by MK
		# increase the obstacles generated at certain score points, to incorporate level
		# difficulties. In that way, game is more fun take into consideration player position
		# at higher scores(higher difficulty), so that it becomes harder avoiding the obstacles
		# with obstacles, top half obstacle might cloud/plane, and then bottom its a different
		# obstacle type, eg, the rocks/others. (in that way it's a more realistic flying simulation of the bird)


# egypt level
class Level02(Level):
	""" Definition for level 2. """
 
	def __init__(self, player):
		""" Create level 2. """

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("arts/graphics/egypt.png").convert_alpha()
		self.background = pygame.transform.scale(self.background, constants.screenSize)
		self.background.set_colorkey((255, 255, 255))

		self.level_soundtrack = pygame.mixer.Sound("arts/audio/egypt.wav")

		# List of "fixed" obstacles, and x, y location of the obstacle.
		self.collection = [[obstacles.HEAD], [obstacles.PYRAMID]]
		self.obstacle_type = obstacles.Obstacle([obstacles.MONUMENT][0])

		# fill it up
		self.fill_with_flying_obstacles(1)
		self.make_ground_obstacle(self.obstacle_type)
		# to make this level challenging
		self.make_special_obstacle(obstacles.PLANE, -3, 0)
		self.maximum = 15

	def update(self):
		Level.update(self)

		for obstacle in self.obstacle_list:
			if obstacle.rect.x + obstacle.rect.width < 0:
				self.obstacle_list.remove(obstacle)

				# replace the lost obstacle with either flying or ground obstacle
				if random.random() < 0.4:
					self.make_flying_obstacle()
				elif 0.4 < random.random() < 0.8:
					self.make_ground_obstacle(self.obstacle_type)
				else:
					self.make_special_obstacle(obstacles.PLANE, random.randint(-1, 1), random.randint(-1, 1))

				# check for level changes
				self.index += 1
				self.score_sound.play()

			if self.index == self.maximum:
					self.next_level = True


# paris level
class Level03(Level):
	""" Definition for level 3. """

	def __init__(self, player):
		""" Create level 3. """

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("arts/graphics/Paris.png").convert_alpha()
		self.background = pygame.transform.scale(self.background, constants.screenSize)
		self.background.set_colorkey((255, 255, 255))

		self.level_soundtrack = pygame.mixer.Sound("arts/audio/paris.wav")

		# List of "fixed" obstacles, and x, y location of the obstacle.

		self.collection = [[obstacles.CLOUD], [obstacles.CHEESE2], [obstacles.CROISSANT], [obstacles.BOTTLE],
						   [obstacles.BREAD]]

		self.obstacle_type = obstacles.Obstacle([obstacles.TOWER][0])

		# fill it up
		self.fill_with_flying_obstacles(2)

		# to make this level challenging
		self.make_special_obstacle(obstacles.PLANE, -3, -1)
		self.maximum = 20

	def update(self):
		Level.update(self)

		for obstacle in self.obstacle_list:
			if obstacle.rect.x + obstacle.rect.width < 0:
				self.obstacle_list.remove(obstacle)

				# replace the lost obstacle with either flying or ground obstacle
				if random.random() < 0.4:
					self.make_flying_obstacle()
				elif 0.4 < random.random() < 0.8:
					self.make_ground_obstacle(self.obstacle_type)
				else:
					self.make_special_obstacle(obstacles.BOTTLE, random.randint(-3, -1), random.randint(-1,1))

				# check for level changes
				self.index += 1
				self.score_sound.play()

			if self.index == self.maximum:
					self.next_level = True


# new york level
class Level04(Level):
	""" Definition for level 4. """

	def __init__(self, player):
		""" Create level 4. """

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("arts/graphics/newyork.png").convert_alpha()
		self.background = pygame.transform.scale(self.background, constants.screenSize)
		self.background.set_colorkey((255, 255, 255))

		self.level_soundtrack = pygame.mixer.Sound("arts/audio/new_york.wav")

		# List of "fixed" obstacles, and x, y location of the obstacle.
		self.collection = [[obstacles.TAXI], [obstacles.APPLE], [obstacles.HAT], [obstacles.BURGER], [obstacles.FRIES]]
		self.obstacle_type = obstacles.Obstacle([obstacles.STATUE_OF_LIBERTY][0])
		# fill it up
		self.fill_with_flying_obstacles(2)

		# to make this level challenging
		self.make_special_obstacle(obstacles.PLANE, -3, -1)
		self.make_ground_obstacle(self.obstacle_type)
		self.maximum = 30


	def update(self):
		Level.update(self)

		for obstacle in self.obstacle_list:
			if obstacle.rect.x + obstacle.rect.width < 0:
				self.obstacle_list.remove(obstacle)
				# replace the lost obstacle with either flying or ground obstacle
				if random.random() < 0.33:
					self.make_flying_obstacle()
				elif 0.33 < random.random() < 0.66:
					self.make_ground_obstacle(self.obstacle_type)
				else:
					self.make_special_obstacle(obstacles.PLANE, random.randint(-4, -2), random.randint(-1, 1))

				# check for level changes
				self.index += 1
				self.score_sound.play()

			if self.index == self.maximum:
					self.next_level = True


# beijing level -- i dare you
class Level05(Level):
	""" Definition for level 5. """

	def __init__(self, player):
		""" Create level 5. """

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("arts/graphics/beijing.png").convert_alpha()
		self.background = pygame.transform.scale(self.background, constants.screenSize)
		self.background.set_colorkey((255, 255, 255))

		self.level_soundtrack = pygame.mixer.Sound("arts/audio/beijing.wav")

		# List of "fixed" obstacles, and x, y location of the obstacle.
		self.collection = [[obstacles.MASK1], [obstacles.MASK2], [obstacles.MASK3], [obstacles.BOOK],
						   [obstacles.LUCKY_BAG], [obstacles.KNOT]]
		# Add the empire state building
		self.obstacle_type = obstacles.Obstacle([obstacles.TV_TOWER][0])
		# fill it up
		self.fill_with_flying_obstacles(3)
		# Add a horizontally moving obstacle
		self.make_special_obstacle(obstacles.PLANE, -4, 0)
		# self.maximum = 5
		self.maximum = 40

	def update(self):
		Level.update(self)

		for obstacle in self.obstacle_list:
			if obstacle.rect.x + obstacle.rect.width < 0:
				self.obstacle_list.remove(obstacle)
				# replace the lost obstacle with either flying or ground obstacle
				if random.random() < 0.3:
					self.make_flying_obstacle()
				elif 0.3 < random.random() < 0.65:
					self.make_ground_obstacle(self.obstacle_type)
				else:
					self.make_special_obstacle(obstacles.PLANE, random.randint(-4, -2), random.randint(-1,1))

				# to check for level changes
				self.index += 1
				self.score_sound.play()

				if self.index == self.maximum:
					self.next_level = True
