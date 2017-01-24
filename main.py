# #main program

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
    clock.tick(30)    # to make it easier to play for now
    # clock.tick(60)

    # ################## load up all useful graphics, sound, etc here #######################

    #     load up the images
    gameover = pygame.image.load("arts/graphics/gameover.png").convert_alpha()
    welcome = pygame.image.load("arts/graphics/welcome.png").convert_alpha()
    instruction_page_one = pygame.image.load("arts/graphics/nest.png").convert_alpha()
    instruction_page_two = pygame.image.load("arts/graphics/falcon_in_sky.png").convert_alpha()
    success = pygame.image.load("arts/graphics/success.png").convert_alpha()
    score_text = pygame.image.load("arts/graphics/score.png").convert_alpha()
    congratulations_text = pygame.image.load("arts/graphics/congratulations_text.png").convert_alpha()
    digits = [pygame.image.load('arts/graphics/0.png').convert_alpha(),
              pygame.image.load('arts/graphics/1.png').convert_alpha(),
              pygame.image.load('arts/graphics/2.png').convert_alpha(),
              pygame.image.load('arts/graphics/3.png').convert_alpha(),
              pygame.image.load('arts/graphics/4.png').convert_alpha(),
              pygame.image.load('arts/graphics/5.png').convert_alpha(),
              pygame.image.load('arts/graphics/6.png').convert_alpha(),
              pygame.image.load('arts/graphics/7.png').convert_alpha(),
              pygame.image.load('arts/graphics/8.png').convert_alpha(),
              pygame.image.load('arts/graphics/9.png').convert_alpha()
              ]

    # scale down the images
    gameover = pygame.transform.scale(gameover, constants.screenSize)
    welcome = pygame.transform.scale(welcome, constants.screenSize)
    instruction_page_one = pygame.transform.scale(instruction_page_one, constants.screenSize)
    instruction_page_two = pygame.transform.scale(instruction_page_two, constants.screenSize)
    success = pygame.transform.scale(success, constants.screenSize)

    # for digit in digits:
    for i in xrange(len(digits)):
        digits[i] = pygame.transform.scale(digits[i], (42, 64))

    # load up the sounds
    die = pygame.mixer.Sound("arts/audio/chip.wav")
    flap_sound = pygame.mixer.Sound("arts/audio/swoosh.wav")
    start_sound = pygame.mixer.Sound("arts/audio/start_screen.wav")
    level_up_sound = pygame.mixer.Sound("arts/audio/level_up.wav")
    game_over_sound = pygame.mixer.Sound("arts/audio/game_over.wav")

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
    player.rect.x = (constants.SCREEN_WIDTH * 0.2)-30
    player.rect.y = constants.SCREEN_HEIGHT/3
    active_sprite_list.add(player)

    # deal with score
    def show_the_score():
        if current_level_no == 0:
            score = current_level.index
        elif current_level_no == 1:
            score = current_level.index + current_level.maximum
        else:
            score = current_level.index + current_level.maximum*2

        score_digits = [int(x) for x in list(str(score))]
        total_width = 0  # total width of all numbers to be printed

        for digit in score_digits:
            total_width += digits[digit].get_width()

        x_offset = (constants.SCREEN_WIDTH - total_width) / 2

        for digit in score_digits:
            screen.blit(digits[digit], (x_offset, constants.SCREEN_HEIGHT * 0.05))
            x_offset += digits[digit].get_width()

            # screen.blit(font.render("Score : "+str(score), True, constants.red), (15, 10))

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
                    if instruction_page == 4:
                        # stop start sound and start level 1 music
                        start_sound.stop()
                        current_level.level_soundtrack.play(loops=-1, maxtime=0, fade_ms=0)
                        phase = "play"

            if instruction_page == 1:
                # Draw instructions, page 1
                screen.blit(welcome, [0, 0])
                # This could also load an image created in another program.
                # That could be both easier and more flexible.

            if instruction_page == 2:                
                # Draw instructions, page 2
                screen.blit(instruction_page_one, [0, 0])

            if instruction_page == 3:
                screen.blit(instruction_page_two, [0, 0])

            # updates the screen with what we've drawn.
            pygame.display.flip()

        if phase == "play":
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_ESCAPE
                         or event.key == pygame.K_q)):
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

            # check for level changes
            if current_level.next_level:
                current_level.level_soundtrack.stop()
                pygame.time.wait(1000)
                level_up_sound.play()
                phase = "success"

            # check if the player has collided
            if player.collided:
                current_level.level_soundtrack.stop()
                die.play()
                # pause for effect after crashing
                pygame.time.wait(1000)
                game_over_sound.play(loops=-1, maxtime=0, fade_ms=0)
                phase = "end"

# ################## ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT ########################

            current_level.draw(screen)
            active_sprite_list.draw(screen)
            show_the_score()

# ################## ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT #####################

            # update the screen with what we've drawn.
            pygame.display.flip()

        if phase == "success":
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                    player.rect.y = constants.SCREEN_HEIGHT/3
                    if current_level_no < len(level_list)-1:
                        current_level_no += 1
                        current_level = level_list[current_level_no]
                        player.level = current_level

                        # vary speeds
                        obstacle_speed *= 1.2
                        player.falling_rate *= 1.3
                        player.rising_rate *= 1.3

                    current_level.level_soundtrack.play(loops=-1, maxtime=0, fade_ms=0)
                    phase = "play"
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()

            # draw the success screen and show score
            screen.blit(success, (0, 0))
            screen.blit(score_text, (25, 45))

            screen.blit(congratulations_text, (50, 400))
            show_the_score()

            # updates the screen with what we've drawn.
            pygame.display.flip()

        if phase == "end":
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                    # this would hopefully make the game more addictive since is hard to just quit
                    # stop the game over sound
                    game_over_sound.stop()
                    main()
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                    # stop the start sound
                    game_over_sound.stop()
                    main()

            # draw the game over screen
            screen.blit(gameover, (0, 0))
            screen.blit(score_text, (25, 45))
            show_the_score()

            # updates the screen with what we've drawn.
            pygame.display.flip()

    # to bee IDLE friendly and prevent program hanging on exit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
