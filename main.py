# main program

import pygame
import sys
import level
import constants
from player import Player


def main():
    """ Main Program """
    # initialize pygame
    pygame.init()
    # initialize the fonts
    try:
        pygame.font.init()
    except:
        print "Fonts unavailable"
        sys.exit()

    # This is a font we use to draw text on the screen (size 36)
    font = pygame.font.Font(None, 36)

    # Set up some values
    instruction_page = 1
    phase = "start"
    done = False

    # make a game screen of screenSize
    screen = pygame.display.set_mode(constants.screenSize)
    # title of window to be displayed
    pygame.display.set_caption("test-run Falcon")
    # make a game clock that we shall use to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Limits to 60 frames per second
    # clock.tick(20)    # to make it easier to play for now
    clock.tick(60)

    # ################## load up all useful graphics, sound, etc here #######################
    #     load up the images
    gameover = pygame.image.load("arts/graphics/gameover.png").convert_alpha()
    welcome = pygame.image.load("arts/graphics/welcome.png").convert_alpha()
    # scale down the images
    gameover = pygame.transform.scale(gameover, constants.screenSize)
    welcome = pygame.transform.scale(welcome, constants.screenSize)

    # load up the sounds
    # score_sound = pygame.mixer.Sound("arts/audio/score.wav")
    die = pygame.mixer.Sound("arts/audio/chip.wav")
    flap_sound = pygame.mixer.Sound("arts/audio/swoosh.wav")
    start_sound = pygame.mixer.Sound("arts/audio/Begin.wav")
    level1sound = pygame.mixer.Sound("arts/audio/MountainSoundTrackV2.wav")

    # play start sound
    start_sound.play(loops=-1, maxtime=0, fade_ms=0)

    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = [level.Level01(player), level.Level02(player), level.Level03(player)]

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    obstacle_speed = 4
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    # set player position on screen
    player.rect.x = (constants.SCREEN_WIDTH * 0.25)
    player.rect.y = constants.SCREEN_HEIGHT/3
    active_sprite_list.add(player)

    # -------- Main Program Loop -----------

    while not done:
        if phase == "start":
            # -------- Instruction Page Loop -----------
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                                 and (event.key == pygame.K_DOWN or event.key == pygame.K_ESCAPE
                                                      or event.key == pygame.K_q)):
                    done = True
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                    instruction_page += 1
                    if instruction_page == 3:
                        # stop start sound and start level 1 music
                        start_sound.stop()
                        level1sound.play(loops=-1, maxtime=0, fade_ms=0)
                        phase = "play"

            # Set the screen background
            screen.fill(constants.black)

            if instruction_page == 1:
                # Draw instructions, page 1
                screen.blit(welcome, [0, 0])
                # This could also load an image created in another program.
                # That could be both easier and more flexible.

            if instruction_page == 2:
                # Draw instructions, page 2
                text = font.render("Page 2 is a storyline picture.", True, constants.white)
                screen.blit(text, [10, 10])
                text = font.render("Also describe controls.", True, constants.white)
                screen.blit(text, [10, 50])
                text = font.render("Can add Page 3 if needed.", True, constants.white)
                screen.blit(text, [10, 90])

            # updates the screen with what we've drawn.
            pygame.display.flip()

        if phase == "play":
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_ESCAPE)
                         or event.key == pygame.K_Q):
                    phase = "end"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        player.flap()
                        flap_sound.play()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        player.release_wing()

            # Update the player.
            active_sprite_list.update()
            # Update items in the level
            current_level.update()
            # constantly shift obstacles to the left
            current_level.shift_obstacles(obstacle_speed)

            # just testing the change in levels
            if current_level.next_level:
                player.rect.y = constants.SCREEN_HEIGHT/3
                if current_level_no < len(level_list)-1:
                    current_level_no += 1
                    current_level = level_list[current_level_no]
                    player.level = current_level
                    obstacle_speed += 1
                    # obstacle_speed += 1.5

                    # do a countdown or something...pause the game to give the player some time
                    pygame.time.wait(2000)
                else:
                    current_level_no -= 1
                    current_level = level_list[current_level_no]
                    player.level = current_level
                    obstacle_speed += 1
                    # obstacle_speed += 1.5

        # HOW TO !!! go to the next level
            # current_position = player.rect.x + current_level.world_shift
            # if current_position < current_level.level_limit:
            #     player.rect.x = 120
            #     if current_level_no < len(level_list)-1:
            #         current_level_no += 1
            #         current_level = level_list[current_level_no]
            #         player.level = current_level
            # if pygame.sprite.collide_mask(player, obstacles.Nest == True:

            # haven't designed a nest yet
            # blit the 1st congratulation page
            # this page should include which button does which detect user action
            # 	if want to continue to the next level:
            # 	current_level += 1
            # 	obstacle_speed += 10
            # 	detect other actions:
            # 	back to the beginning

            # check if the player has collided
            if player.collided:
                level1sound.stop()
                die.play()
                # pause for effect after crashing
                pygame.time.wait(1000)

                # play the end screen sound
                start_sound.play(loops=-1, maxtime=0, fade_ms=0)
                phase = "end"

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

            current_level.draw(screen)
            active_sprite_list.draw(screen)

            # deal with score
            if current_level_no == 0:
                score = current_level.index
            elif current_level_no == 1:
                score = current_level.index + current_level.maximum
            else:
                score = current_level.index + current_level.maximum*2

            screen.blit(font.render("Score : "+str(score), True, constants.red), (15, 10))

    # ################## ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT #####################

            # update the screen with what we've drawn.
            pygame.display.flip()

        if phase == "end":
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                    # this would hopefully make the game more addictive since is hard to just quit

                    # stop the start sound
                    start_sound.stop()
                    # replay the game
                    main()
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                    # stop the start sound
                    start_sound.stop()
                    # replay the game
                    main()

            # clear the screen with white first
            screen.fill((255, 255, 255))
            # draw the game over screen
            screen.blit(gameover, (0, 0))
            # showTheScore(score)

            # updates the screen with what we've drawn.
            pygame.display.flip()

    # to bee IDLE friendly and prevent program hanging on exit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
