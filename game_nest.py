# PyGame Project: Game Nest

import pygame  # Imports the pygame library
import random  # Used for getting random numbers/integers generated
from pygame.locals import *  # Used with key events

pygame.init()  # Initializing pygame

# Defining general colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (38, 70, 83)
LIGHT_BLUE = (42, 157, 143)
YELLOW = (233, 196, 106)
ORANGE = (244, 162, 97)
RED = (231, 111, 81)
LIGHT_GREEN = (153, 217, 140)
LIGHT_PINK = (255, 214, 186)
PINK = (181, 23, 158)
FAINT_BLUE = (82, 182, 154)
BRIGHT_YELLOW = (255, 183, 3)
GAME_RED = (158, 42, 43)
GAME_BLUE = (51, 92, 103)
GAME_YELLOW = (224, 159, 62)

# Setting up the screen and its dimensions
screen_width = 1000
screen_height = 600
size = (screen_width, screen_height)
x, y = size
screen = pygame.display.set_mode(size)

# Setting up the game caption and icon
pygame.display.set_caption("Mini Games Royale")
icon = pygame.image.load('Clash_of_Games/game_icon.png')
pygame.display.set_icon(icon)

# Setting up fonts and font variables
font_god = pygame.font.Font('Clash_of_Games/god.ttf', 95)
font_god_small = pygame.font.Font('Clash_of_Games/god.ttf', 77)
font_god_extra_small = pygame.font.Font('Clash_of_Games/god.ttf', 55)
font_dash = pygame.font.Font('Clash_of_Games/dash.otf', 77)
font_dash_small = pygame.font.Font('Clash_of_Games/dash.otf', 44)

# Setting up the game loop, frames per second, time, and screen mode
done = False
clock = pygame.time.Clock()
FPS = 60
screen_mode = 'home'

# Setting up home screen text and text borders
game_text = font_god.render("Clash of Games", True, (FAINT_BLUE))
game_rect = game_text.get_rect()
game_rect.center = (screen_width // 2, screen_height // 2 - 175)

play_text = font_dash.render("Play Games", True, (LIGHT_GREEN))
play_rect = play_text.get_rect()
play_rect.center = (screen_width // 2, screen_height // 2 - 20)

set_text = font_dash.render("Settings", True, (LIGHT_GREEN))
set_rect = set_text.get_rect()
set_rect.center = (screen_width // 2, screen_height // 2 + 90)

exit_text = font_dash.render("Exit", True, (LIGHT_GREEN))
exit_rect = exit_text.get_rect()
exit_rect.center = (screen_width // 2, screen_height // 2 + 200)

# Setting / loading up the background and background choices for the settings menu
background_choice = 'blue'
theme_color = LIGHT_BLUE
set_text_color = LIGHT_BLUE

pink_bg = pygame.image.load('Clash_of_Games/pink_bg.jpg')
pink_bg2 = pygame.transform.scale(pink_bg, (300, 169))
pink_rect = pink_bg2.get_rect()

blue_bg = pygame.image.load('Clash_of_Games/blue_bg.jpg')
blue_bg2 = pygame.transform.scale(blue_bg, (300, 169))
blue_rect = blue_bg2.get_rect()

green_bg = pygame.image.load('Clash_of_Games/green_bg.jpg')
green_bg2 = pygame.transform.scale(green_bg, (300, 169))
green_rect = green_bg2.get_rect()

red_bg = pygame.image.load('Clash_of_Games/red_bg.jpg')
red_bg2 = pygame.transform.scale(red_bg, (300, 169))
red_rect = red_bg2.get_rect()

# Text formatting for game menu screen
game_set_text = font_god_small.render("Game Menu", True, (set_text_color))
game_set_text_rect = game_set_text.get_rect()
game_set_text_rect.center = (screen_width // 2, screen_height // 2 - 215)

pong_text = font_dash.render("PONG", True, (BLACK))
pong_text_rect = pong_text.get_rect()
pong_text_rect.center = (275, 270)

catch_text = font_dash.render("CATCH", True, (BLACK))
catch_text_rect = catch_text.get_rect()
catch_text_rect.center = (screen_width - 275, 270)

# Setting up game menu screen images to scale
catch_image = pygame.image.load('Clash_of_Games/catching_preview.jpg')
catch_image = pygame.transform.scale(catch_image, (300, 169))
catch_image_rect = catch_image.get_rect()

pong_image = pygame.image.load('Clash_of_Games/pong_preview.png')
pong_image = pygame.transform.scale(pong_image, (300, 169))
pong_image_rect = pong_image.get_rect()

soon_image = pygame.image.load('Clash_of_Games/coming_soon.jpg')
soon_image = pygame.transform.scale(soon_image, (300, 169))
soon_image_rect = soon_image.get_rect()

# Setting up text and text borders for the settings screen
back_set_text = font_god_small.render("Settings", True, (set_text_color))
back_set_rect = back_set_text.get_rect()
back_set_rect.center = (screen_width // 2 - 42, screen_height // 2 - 215)

blue_text = font_dash.render("BLUE", True, (FAINT_BLUE))
blue_text_rect = blue_text.get_rect()
blue_text_rect.center = (275, 270)

red_text = font_dash.render("RED", True, (RED))
red_text_rect = red_text.get_rect()
red_text_rect.center = (screen_width - 275, 270)

pink_text = font_dash.render("PINK", True, (PINK))
pink_text_rect = pink_text.get_rect()
pink_text_rect.center = (275, screen_height - 115)

green_text = font_dash.render("GREEN", True, (LIGHT_GREEN))
green_text_rect = green_text.get_rect()
green_text_rect.center = (screen_width - 275, screen_height - 115)

# Setting up pong game timer variables
current_ticks = 0
past_ticks = 0
start_time = False
round_time = 0
round_start_time = 0

# Setting up pong game conditions and lives
pong_game_over = False
run_pong = False
get_ticks = False
p1_won = False
p2_won = False
p1_lives = 5
p2_lives = 5

# Setting up pong game ball variables
ball_radius = 8
ball_x = round(screen_width / 2)
ball_y = round(screen_height / 2) + 55
ball_xspeed = 4
ball_yspeed = 3
ball_colour = BRIGHT_YELLOW

# Setting up pong game paddle variables
pad_w = 10
pad_h = 70
pad1_x = 110
pad2_x = screen_width - pad_w - 110
pad1_y = 355 - (pad_h // 2)
pad2_y = 355 - (pad_h // 2)
pad1_speed = 5
pad2_speed = 5

# Loading pong game images
pong_bg = pygame.image.load("Clash_of_Games/pong_bg.png")
pong_bg = pygame.transform.scale(pong_bg, (800, 480))
pong_bg_rect = pong_bg.get_rect()

pong_heart = pygame.image.load("Clash_of_Games/heart_image.png")
pong_heart = pygame.transform.scale(pong_heart, (55, 60))

# Setting up pong game text headers
pong_title_text = font_god_extra_small.render("Pong Game", True, (GAME_YELLOW))
pong_title_text_rect = pong_title_text.get_rect()
pong_title_text_rect.center = (screen_width // 2, 50)

pong_p1_text = font_dash_small.render("Player 1", True, (GAME_BLUE))
pong_p2_text = font_dash_small.render("Player 2", True, (GAME_RED))

# Setting up game over text for pong game
pong_game_over_text = font_god.render("GAME  OVER", True, (BLACK))
pong_game_over_text_rect = pong_game_over_text.get_rect()
pong_game_over_text_rect.center = (screen_width // 2, screen_height // 2)

pong_p1_win_text = font_god.render("Player 1 Won", True, (BLACK))
pong_p1_win_text_rect = pong_p1_win_text.get_rect()
pong_p1_win_text_rect.center = (screen_width // 2, screen_height // 2 + 100)

pong_p2_win_text = font_god.render("Player 2 Won", True, (BLACK))
pong_p2_win_text_rect = pong_p2_win_text.get_rect()
pong_p2_win_text_rect.center = (screen_width // 2, screen_height // 2 + 100)

restart_text = font_dash_small.render("Please SPACE To Restart", True, (BLACK))
restart_text_rect = restart_text.get_rect()
restart_text_rect.center = (screen_width // 2, screen_height // 2 + 200)

# Setting up catch game scores and point variables
winning_score = 50
p1_score = 0
p2_score = 0

apple_score = 1
orange_score = 2
pear_score = 3
peach_score = 4
plum_score = 5

# Setting up catch game conditions
catch_game_over = False
catch_p1_winner = False
catch_p2_winner = False
start_catch = False
run_catch = False
catch_round_start = False
catch_round_start_time = 0
catch_round_current_time = 0

# Setting up catch basket(s) positions
bask1_x = 345
bask1_y = 500
bask2_x = 745
bask2_y = 500

# Setting up fruit spawning timers, fruit positioning, and fruit storaging lists
catch_spawn_start_time = 0
catch_spawn_current_time = 0
catch_spawn_start = False
fruit_num = 0
fruitX = 0
fruitY = 0
apples = []
oranges = []
pears = []
peaches = []
plums = []

# Loading and resizing catch game images
catch_bg = pygame.image.load('Clash_of_Games/catch_tree_bg.png')
banner_img = pygame.image.load("Clash_of_Games/banner.png")
basket_img = pygame.image.load("Clash_of_Games/basket.png")

apple_img = pygame.image.load("Clash_of_Games/apple.png")
orange_img = pygame.image.load("Clash_of_Games/orange.png")
peach_img = pygame.image.load("Clash_of_Games/peach.png")
pear_img = pygame.image.load("Clash_of_Games/pear.png")
plum_img = pygame.image.load("Clash_of_Games/plum.png")

catch_bg = pygame.transform.scale(catch_bg, (800, 427))
banner_img = pygame.transform.scale(banner_img, (145, 427))
basket_img = pygame.transform.scale(basket_img, (70, 50))

apple_img = pygame.transform.scale(apple_img, (40, 50))
orange_img = pygame.transform.scale(orange_img, (50, 50))
peach_img = pygame.transform.scale(peach_img, (50, 50))
pear_img = pygame.transform.scale(pear_img, (40, 50))
plum_img = pygame.transform.scale(plum_img, (50, 50))

apple_fall = pygame.transform.scale(apple_img, (20, 25))
orange_fall = pygame.transform.scale(orange_img, (25, 25))
peach_fall = pygame.transform.scale(peach_img, (25, 25))
pear_fall = pygame.transform.scale(pear_img, (20, 25))
plum_fall = pygame.transform.scale(plum_img, (25, 25))

# Setting up catch game text header
catch_title_text = font_god_extra_small.render("Catch Game", True, (GAME_YELLOW))
catch_title_text_rect = catch_title_text.get_rect()
catch_title_text_rect.center = (screen_width // 2, 50)

# Setting up catch game score objective header
winning_score_text = font_dash_small.render(f"REACH {winning_score}!", True, (GAME_YELLOW))

# Setting up catch game fruit ranking point text
apple_text = font_god_extra_small.render("1", True, (LIGHT_GREEN))
orange_text = font_god_extra_small.render("2", True, (LIGHT_GREEN))
pear_text = font_god_extra_small.render("3", True, (LIGHT_GREEN))
peach_text = font_god_extra_small.render("4", True, (LIGHT_GREEN))
plum_text = font_god_extra_small.render("5", True, (LIGHT_GREEN))

# Setting up game over text for catch game
catch_game_over_text = font_god.render("GAME  OVER", True, (BLACK))
catch_game_over_text_rect = catch_game_over_text.get_rect()
catch_game_over_text_rect.center = (580, screen_height // 2 - 50)

catch_p1_win_text = font_god.render("Player 1 Won", True, (BLACK))
catch_p1_win_text_rect = catch_p1_win_text.get_rect()
catch_p1_win_text_rect.center = (580, screen_height // 2 + 50)

catch_p2_win_text = font_god.render("Player 2 Won", True, (BLACK))
catch_p2_win_text_rect = catch_p2_win_text.get_rect()
catch_p2_win_text_rect.center = (580, screen_height // 2 + 50)

catch_restart_text = font_dash_small.render("Please SPACE To Restart", True, (BLACK))
catch_restart_text_rect = catch_restart_text.get_rect()
catch_restart_text_rect.center = (580, screen_height // 2 + 150)

# Setting up or loading game home and exit icons
home_icon = pygame.image.load("Clash_of_Games/home_icon.png")
home_icon_rect = home_icon.get_rect()
home_icon2 = pygame.transform.scale(home_icon, (134, 44))
home_icon2_rect = home_icon2.get_rect()

exit_icon = pygame.image.load("Clash_of_Games/exit_icon.png")
exit_icon_rect = home_icon.get_rect()
exit_icon2 = pygame.transform.scale(exit_icon, (134, 44))
exit_icon2_rect = home_icon2.get_rect()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        # If user chooses to quit program, the loop and game ends
        if event.type == pygame.QUIT:
            done = True

        # If key is pressed down
        if event.type == KEYDOWN:
            # If pong game is over and user wants to restart, game variables get reset
            if event.key == K_SPACE and pong_game_over:
                # Resetting pong game timer variables
                start_time = False
                current_ticks = 0
                past_ticks = 0
                round_time = 0
                round_start_time = 0
                # Resetting pong game conditions and lives
                pong_game_over = False
                run_pong = False
                get_ticks = True
                p1_won = False
                p2_won = False
                p1_lives = 5
                p2_lives = 5
                # Resetting pong game ball position
                ball_x = round(screen_width / 2)
                ball_y = round(screen_height / 2) + 55
                # Setting up pong game paddle position
                pad1_y = 355 - (pad_h // 2)
                pad2_y = 355 - (pad_h // 2)

            # If catch game is over and user wants to restart, game variables get reset
            if event.key == K_SPACE and catch_game_over:
                # Resetting catch game scores
                p1_score = 0
                p2_score = 0
                # Resetting catch game conditions
                catch_game_over = False
                catch_p1_winner = False
                catch_p2_winner = False
                start_catch = True
                run_catch = False
                # Resetting catch game timer variables
                catch_round_start = False
                catch_round_start_time = 0
                catch_round_current_time = 0
                # Resetting catch basket(s) position
                bask1_x = 345
                bask1_y = 500
                bask2_x = 745
                bask2_y = 500
                # Resetting fruit spawning timers and fruit positioning
                catch_spawn_start_time = 0
                catch_spawn_current_time = 0
                catch_spawn_start = False
                fruit_num = 0
                fruitX = 0
                fruitY = 0
                # Clearing fruit(s) storage
                apples.clear()
                oranges.clear()
                pears.clear()
                peaches.clear()
                plums.clear()

        # If mouse is released, it checks for where mouse was clicked
        if event.type == MOUSEBUTTONUP:
            # If left mouse button was clicked/released
            if event.button == 1:

                # If user is on home screen
                if screen_mode == 'home':
                    # If the user wants to exit they quit the screen
                    if exit_rect.collidepoint(mouse_XY):
                        done = True
                    # Changes screen mode if settings text is clicked
                    elif set_rect.collidepoint(mouse_XY):
                        screen_mode = 'settings'
                    # Changes screen mode if play games text is clicked
                    elif play_rect.collidepoint(mouse_XY):
                        screen_mode = 'game_screen'

                # If user is on settings screen
                elif screen_mode == 'settings':
                    # Changes screen mode if home icon is clicked
                    if home_icon_rect.collidepoint(mouse_XY):
                        screen_mode = 'home'
                    # If the user wants to exit they quit the screen
                    elif exit_icon_rect.collidepoint(mouse_XY):
                        done = True

                    # Changes background if blue background image is clicked
                    elif blue_border_rect.collidepoint(mouse_XY):
                        background_choice = 'blue'
                        theme_color = LIGHT_BLUE
                        set_text_color = LIGHT_BLUE
                    # Changes background if pink background image is clicked
                    elif pink_border_rect.collidepoint(mouse_XY):
                        background_choice = 'pink'
                        theme_color = PINK
                        set_text_color = PINK
                    # Changes background if red background image is clicked
                    elif red_border_rect.collidepoint(mouse_XY):
                        background_choice = 'red'
                        theme_color = RED
                        set_text_color = RED
                    # Changes background if green background image is clicked
                    elif green_border_rect.collidepoint(mouse_XY):
                        background_choice = 'green'
                        theme_color = LIGHT_GREEN
                        set_text_color = LIGHT_GREEN

                # If user is on game screen
                elif screen_mode == 'game_screen':
                    # Changes background if home icon is clicked
                    if home_icon_rect.collidepoint(mouse_XY):
                        screen_mode = 'home'
                    # If the user wants to exit they quit the screen
                    elif exit_icon_rect.collidepoint(mouse_XY):
                        done = True

                    # Changes to pong if pong game is selected
                    elif pong_border_rect.collidepoint(mouse_XY):
                        # Resetting pong game timer variables
                        start_time = False
                        current_ticks = 0
                        past_ticks = 0
                        round_time = 0
                        round_start_time = 0
                        # Resetting pong game conditions and lives
                        pong_game_over = False
                        run_pong = False
                        get_ticks = True
                        p1_won = False
                        p2_won = False
                        p1_lives = 5
                        p2_lives = 5
                        # Resetting pong game ball position
                        ball_x = round(screen_width / 2)
                        ball_y = round(screen_height / 2) + 55
                        # Setting up pong game paddle position
                        pad1_y = 355 - (pad_h // 2)
                        pad2_y = 355 - (pad_h // 2)

                        # Sets screen mode to pong game
                        screen_mode = 'pong'

                    # Changes to catch if catch game is selected
                    elif catch_border_rect.collidepoint(mouse_XY):
                        # Resetting catch game scores
                        p1_score = 0
                        p2_score = 0
                        # Resetting catch game conditions
                        catch_game_over = False
                        catch_p1_winner = False
                        catch_p2_winner = False
                        start_catch = True
                        run_catch = False
                        # Resetting catch game timer variables
                        catch_round_start = False
                        catch_round_start_time = 0
                        catch_round_current_time = 0
                        # Resetting catch basket(s) position
                        bask1_x = 345
                        bask1_y = 500
                        bask2_x = 745
                        bask2_y = 500
                        # Resetting fruit spawning timers and fruit positioning
                        catch_spawn_start_time = 0
                        catch_spawn_current_time = 0
                        catch_spawn_start = False
                        fruit_num = 0
                        fruitX = 0
                        fruitY = 0
                        # Clearing fruit(s) storage
                        apples.clear()
                        oranges.clear()
                        pears.clear()
                        peaches.clear()
                        plums.clear()

                        # Sets screen mode to catch game
                        screen_mode = 'catch'

                # If user is on pong game screen
                elif screen_mode == 'pong':
                    # Goes to game screen if home icon is clicked
                    if home_icon2_rect.collidepoint(mouse_XY):
                        FPS = 60
                        pong_game_over = False
                        screen_mode = 'game_screen'
                    # If the user wants to exit they quit the screen
                    elif exit_icon2_rect.collidepoint(mouse_XY):
                        done = True

                # If user is on catch game screen
                elif screen_mode == 'catch':
                    # Goes to game screen if home icon is clicked
                    if home_icon2_rect.collidepoint(mouse_XY):
                        catch_game_over = False
                        screen_mode = 'game_screen'
                    # If the user wants to exit they quit the screen
                    elif exit_icon2_rect.collidepoint(mouse_XY):
                        done = True

    # Controlling keyboard and mouse controls/presses
    keys = pygame.key.get_pressed()
    mouse_click = pygame.mouse.get_pressed()
    mouse_XY = pygame.mouse.get_pos()

    # Updating the screen background
    if background_choice == 'red':
        menu_bg = pygame.transform.scale(red_bg, (screen_width, screen_height))
    elif background_choice == 'blue':
        menu_bg = pygame.transform.scale(blue_bg, (screen_width, screen_height))
    elif background_choice == 'pink':
        menu_bg = pygame.transform.scale(pink_bg, (screen_width, screen_height))
    elif background_choice == 'green':
        menu_bg = pygame.transform.scale(green_bg, (screen_width, screen_height))
    screen.blit(menu_bg, (0, 0))

    # Checks to see if user is on game screen
    if screen_mode == 'home':
        # Displays a highlighted border if user hovers over text
        if exit_rect.collidepoint(mouse_XY):
            border = exit_rect.inflate(80, 30)
            border.x = screen_width // 2 - 100
            border.y = screen_height - 157
            pygame.draw.ellipse(screen, (DARK_BLUE), border)
        elif set_rect.collidepoint(mouse_XY):
            border = set_rect.inflate(100, 40)
            pygame.draw.ellipse(screen, (DARK_BLUE), border)
        elif play_rect.collidepoint(mouse_XY):
            border = play_rect.inflate(100, 50)
            pygame.draw.ellipse(screen, (DARK_BLUE), border)

        # Displays game screen text
        screen.blit(game_text, game_rect)
        screen.blit(play_text, play_rect)
        screen.blit(set_text, set_rect)
        screen.blit(exit_text, exit_rect)

    # Checks if user is on settings screen
    if screen_mode == 'settings':
        # Sets up screen header and displays home and exit icons
        back_set_text = font_god.render("Settings", True, (set_text_color))
        screen.blit(back_set_text, back_set_rect)
        home_icon_rect.x = 44
        home_icon_rect.y = 60
        exit_icon_rect.x = screen_width - 220
        exit_icon_rect.y = 60
        screen.blit(home_icon, home_icon_rect)
        screen.blit(exit_icon, exit_icon_rect)

        # Displays blue background image and 'blue' text if user hovers over background
        blue_border_rect = blue_rect.inflate(14, 14)
        blue_border_rect.x = 115
        blue_border_rect.y = 165
        pygame.draw.rect(screen, LIGHT_BLUE, blue_border_rect, 7, 7)
        blue_border_rect.x += 7
        blue_border_rect.y += 7
        screen.blit(blue_bg2, blue_border_rect)
        if blue_border_rect.collidepoint(mouse_XY):
            screen.blit(blue_text, blue_text_rect)

        # Displays pink background image and 'pink' text if user hovers over background
        pink_border_rect = pink_rect.inflate(14, 14)
        pink_border_rect.x = 115
        pink_border_rect.y = screen_height - 220
        pygame.draw.rect(screen, PINK, pink_border_rect, 7, 7)
        pink_border_rect.x += 7
        pink_border_rect.y += 7
        screen.blit(pink_bg2, pink_border_rect)
        if pink_border_rect.collidepoint(mouse_XY):
            screen.blit(pink_text, pink_text_rect)

        # Displays red background image and 'red' text if user hovers over background
        red_border_rect = red_rect.inflate(14, 14)
        red_border_rect.x = screen_width - 435
        red_border_rect.y = 165
        pygame.draw.rect(screen, RED, red_border_rect, 7, 7)
        red_border_rect.x += 7
        red_border_rect.y += 7
        screen.blit(red_bg2, red_border_rect)
        if red_border_rect.collidepoint(mouse_XY):
            screen.blit(red_text, red_text_rect)

        # Displays green background image and 'green' text if user hovers over background
        green_border_rect = green_rect.inflate(14, 14)
        green_border_rect.x = screen_width - 435
        green_border_rect.y = screen_height - 220
        pygame.draw.rect(screen, LIGHT_GREEN, green_border_rect, 7, 7)
        green_border_rect.x += 7
        green_border_rect.y += 7
        screen.blit(green_bg2, green_border_rect)
        if green_border_rect.collidepoint(mouse_XY):
            screen.blit(green_text, green_text_rect)

    # Checks to see if user is on game menu screen
    if screen_mode == "game_screen":
        # Displays screen header and also home and exit icons
        screen.blit(game_set_text, game_set_text_rect)
        home_icon_rect.x = 44
        home_icon_rect.y = 60
        exit_icon_rect.x = screen_width - 220
        exit_icon_rect.y = 60
        screen.blit(home_icon, home_icon_rect)
        screen.blit(exit_icon, exit_icon_rect)

        # Sets up pong game slection image, border, and text if hovered over image
        pong_border_rect = pong_image_rect.inflate(14, 14)
        pong_border_rect.x = 115
        pong_border_rect.y = 165
        pygame.draw.rect(screen, theme_color, pong_border_rect, 7, 7)
        pong_border_rect.x += 7
        pong_border_rect.y += 7
        screen.blit(pong_image, pong_border_rect)
        if pong_border_rect.collidepoint(mouse_XY):
            screen.blit(pong_text, pong_text_rect)

        # Sets up catch game slection image, border, and text if hovered over image
        catch_border_rect = catch_image_rect.inflate(14, 14)
        catch_border_rect.x = screen_width - 435
        catch_border_rect.y = 165
        pygame.draw.rect(screen, theme_color, catch_border_rect, 7, 7)
        catch_border_rect.x += 7
        catch_border_rect.y += 7
        screen.blit(catch_image, catch_border_rect)
        if catch_border_rect.collidepoint(mouse_XY):
            screen.blit(catch_text, catch_text_rect)

        # Sets up open game slection spot with an image and border
        soon_border_rect = soon_image_rect.inflate(14, 14)
        soon_border_rect.x = screen_width - 435
        soon_border_rect.y = screen_height - 220
        pygame.draw.rect(screen, theme_color, soon_border_rect, 7, 7)
        soon_border_rect.x += 7
        soon_border_rect.y += 7
        screen.blit(soon_image, soon_border_rect)

        # Sets up open game slection spot with an image and border
        soon2_border_rect = soon_image_rect.inflate(14, 14)
        soon2_border_rect.x = 115
        soon2_border_rect.y = screen_height - 220
        pygame.draw.rect(screen, theme_color, soon2_border_rect, 7, 7)
        soon2_border_rect.x += 7
        soon2_border_rect.y += 7
        screen.blit(soon_image, soon2_border_rect)

    # Checks to see if user is playing pong
    if screen_mode == "pong":
        # Displays pong game headers
        screen.blit(pong_title_text, pong_title_text_rect)
        screen.blit(pong_p1_text, (130, 100))
        screen.blit(pong_p2_text, (screen_width - 260, 100))

        # Displays home and exit icons
        home_icon2_rect.x = 44
        home_icon2_rect.y = 30
        exit_icon2_rect.x = screen_width - 178
        exit_icon2_rect.y = 30
        screen.blit(home_icon2, home_icon2_rect)
        screen.blit(exit_icon2, exit_icon2_rect)
        pong_bg_rect.x = 100
        pong_bg_rect.y = 115
        screen.blit(pong_bg, pong_bg_rect)

        # Updating hearts shown on screen for player 1
        if p1_lives == 0:
            # If player is out of lives, game is over, conditions are changed
            pong_game_over = True
            run_pong = False
            p2_won = True
        if p1_lives >= 1:
            screen.blit(pong_heart, (25, 145))
            if p1_lives >= 2:
                screen.blit(pong_heart, (25, 235))
                if p1_lives >= 3:
                    screen.blit(pong_heart, (25, 325))
                    if p1_lives >= 4:
                        screen.blit(pong_heart, (25, 415))
                        if p1_lives == 5:
                            screen.blit(pong_heart, (25, 505))

        # Updating hearts shown on screen for player 2
        if p2_lives == 0:
            # If player is out of lives, game is over, conditions are changed
            pong_game_over = True
            run_pong = False
            p1_won = True
        if p2_lives >= 1:
            screen.blit(pong_heart, (screen_width - 80, 145))
            if p2_lives >= 2:
                screen.blit(pong_heart, (screen_width - 80, 235))
                if p2_lives >= 3:
                    screen.blit(pong_heart, (screen_width - 80, 325))
                    if p2_lives >= 4:
                        screen.blit(pong_heart, (screen_width - 80, 415))
                        if p2_lives == 5:
                            screen.blit(pong_heart, (screen_width - 80, 505))

        # Checks to see if the pong game is not running
        if not run_pong:
            # If the game should be run, we get the present time
            if get_ticks:
                past_ticks = pygame.time.get_ticks()
                get_ticks = False

            # Gets the current time
            current_ticks = pygame.time.get_ticks()

            # Checks to see if it has been more than 1.5 seconds since the user selected to play pong
            if current_ticks > past_ticks + 1500:
                # If it has been 1.5 seconds, the gme starts and conditions are changed
                run_pong = True
                start_time = True
                FPS = 60

        # If the round has started, it gets the round's start time
        if start_time:
            round_start_time = pygame.time.get_ticks()  # Round's start time
            start_time = False

        # Gets the round's current time
        round_time = pygame.time.get_ticks()

        # If the round has lasted for 4 seconds or more, the frames per second increase to increase game difficultly
        if round_time > start_time + 4000:
            # Every 4 seconds game speeds up and round timer gets reset
            FPS += 10  # Game speeds up
            start_time = pygame.time.get_ticks()  # Resets round timer

        # Checks if no player has won yet
        if not p1_won and not p2_won:
            # Checks if the game is running
            if run_pong:
                # Changes the ball's position
                ball_x += ball_xspeed
                ball_y += ball_yspeed

            # Adjusting horizontal movement/direction
            if ball_x + ball_radius >= 895:
                # If ball touched right wall, player 2 loses a life and round/variables gets reset
                p2_lives -= 1
                ball_xspeed *= -1
                ball_x = round(screen_width / 2)
                ball_y = round(screen_height / 2) + 55
                FPS = 60
                get_ticks = True
                run_pong = False
            elif ball_x - ball_radius <= 105:
                # If ball touched left wall, player 1 loses a life and round/variables gets reset
                p1_lives -= 1
                ball_xspeed *= -1
                FPS = 60
                ball_x = round(screen_width / 2)
                ball_y = round(screen_height / 2) + 55
                get_ticks = True
                run_pong = False

            # If the ball interacts with a paddle, ball horizontal direction is changed
            if (ball_x - ball_radius <= pad1_x + pad_w) and (
                    ball_x - ball_radius >= pad1_x + pad_w - 5) and (
                        ball_y - ball_radius > pad1_y - (2 * ball_radius)
                        and ball_y - ball_radius < pad1_y + pad_h):
                ball_xspeed *= -1
            if (ball_x + ball_radius >=
                    pad2_x) and (ball_x + ball_radius <= pad2_x + 5) and (
                        ball_y - ball_radius > pad2_y - (2 * ball_radius)
                        and ball_y - ball_radius < pad2_y + pad_h):
                ball_xspeed *= -1

            # If the ball touches the top or bottom wall, ball vertical direction is changed
            if ball_y + ball_radius >= 565:
                ball_yspeed *= -1
            elif ball_y - ball_radius <= 146:
                ball_yspeed *= -1

            # If player 1 uses w or s keys, paddle 1's position is adjusted if possible
            if keys[K_w] and pad1_y > 148:
                pad1_y -= pad1_speed
            if keys[K_s] and pad1_y < 569 - pad_h - 5:
                pad1_y += pad1_speed

            # If player 2 uses arrow keys, paddle 2's position is adjusted if possible
            if keys[K_UP] and pad2_y > 148:
                pad2_y -= pad2_speed
            if keys[K_DOWN] and pad2_y < 569 - pad_h - 5:
                pad2_y += pad2_speed

            # Drawing the paddles and ball on the screen
            pygame.draw.rect(screen, GAME_BLUE, pygame.Rect(pad1_x, pad1_y, pad_w, pad_h))
            pygame.draw.rect(screen, GAME_RED, pygame.Rect(pad2_x, pad2_y, pad_w, pad_h))
            pygame.draw.circle(screen, ball_colour, (ball_x, ball_y), ball_radius)

        # Checks to see if the pong game is over
        if pong_game_over:
            # Frames per second get reset to defult frames
            FPS = 60
            # Displays game over and restart text
            screen.blit(pong_game_over_text, pong_game_over_text_rect)
            screen.blit(restart_text, restart_text_rect)

            # Depending on who won, winning player's text is displayed on screen
            if p1_won:
                screen.blit(pong_p1_win_text, pong_p1_win_text_rect)
            elif p2_won:
                screen.blit(pong_p2_win_text, pong_p2_win_text_rect)

    # Checks to see if user is playing catch
    if screen_mode == "catch":
        # Displays header, game background, and game information banner
        screen.blit(catch_title_text, catch_title_text_rect)
        screen.blit(catch_bg, (180, 150))
        screen.blit(banner_img, (20, 150))

        # Displays home and exit icons
        home_icon2_rect.x = 44
        home_icon2_rect.y = 30
        exit_icon2_rect.x = screen_width - 178
        exit_icon2_rect.y = 30
        screen.blit(home_icon2, home_icon2_rect)
        screen.blit(exit_icon2, exit_icon2_rect)

        # Shows player score text headers
        p1_score_text = font_dash_small.render(f"Player 1 Score: {p1_score}", True, (GAME_BLUE))
        p2_score_text = font_dash_small.render(f"Player 2 Score: {p2_score}", True, (GAME_RED))

        # Displays fruit points text on banner
        screen.blit(apple_text, (45, 170))
        screen.blit(orange_text, (45, 245))
        screen.blit(pear_text, (45, 320))
        screen.blit(peach_text, (45, 395))
        screen.blit(plum_text, (45, 470))

        # Shows fruits on the banner beside their point value
        screen.blit(apple_img, (100, 170))
        screen.blit(orange_img, (100, 245))
        screen.blit(pear_img, (100, 320))
        screen.blit(peach_img, (100, 395))
        screen.blit(plum_img, (100, 470))

        # Displays the winning score objective and the individual scores for each player
        screen.blit(winning_score_text, (30, 100))
        screen.blit(p1_score_text, (275, 100))
        screen.blit(p2_score_text, (600, 100))

        # Checks to see if the catch game should be started
        if start_catch:
            # Checks if the round/game hasn't started yet
            if not catch_round_start:
                # Gets the present time for a delay in the catch game starting
                catch_round_start_time = pygame.time.get_ticks()
                catch_round_start = True

            # Gets the current game time
            catch_round_current_time = pygame.time.get_ticks()

            # Checks to see if it has been 2 seconds since the game should have been started
            if catch_round_current_time > catch_round_start_time + 2000:
                # Starts catch game and changes conditions
                run_catch = True
                start_catch = False

        # Checks to see if the catch game has begin
        if run_catch:
            # Displays the two player baskets
            screen.blit(basket_img, (bask1_x, bask1_y))
            screen.blit(basket_img, (bask2_x, bask2_y))

            # If fruit spawning hasn't begin, begins fruit spawning
            if not catch_spawn_start:
                catch_spawn_start_time = pygame.time.get_ticks(
                )  # Get present game time
                catch_spawn_start = True

            # Gets the current game time
            catch_spawn_current_time = pygame.time.get_ticks()

            # Checks to see if it has been more than 0.5 seconds since the last fruit spawn
            if catch_spawn_current_time > catch_spawn_start_time + 500:
                fruit_num = random.randint(
                    1, 15
                )  # Depending on the integer, a fruit will spawn accordingly
                catch_spawn_start_time = pygame.time.get_ticks(
                )  # Changes last spawn time

        # If player 1 presses keys a or d, basket moves if possible
        if keys[K_a] and bask1_x > 185:
            bask1_x -= 4
        if keys[K_d] and bask1_x < 905:
            bask1_x += 4

        # If player 2 pressed arrow keys, basket moves if possible
        if keys[K_LEFT] and bask2_x > 185:
            bask2_x -= 4
        if keys[K_RIGHT] and bask2_x < 905:
            bask2_x += 4

        # If an apple should spawn
        if fruit_num >= 1 and fruit_num <= 5:
            # Apple's position is picked and apple is added to apple list
            fruitX = random.randint(200, 935)
            fruitY = 160
            apples.append([fruitX, fruitY])
            fruit_num = 0  # Resets fruit choice

        # Loops through each fruit in fruit storage
        for apple in apples:
            # Single fruit is selected, and has it's y-position changed
            current_apple = apple
            current_apple[1] += 2

            # Checks for fruit collisions with baskets, if both baskets touch the fruit no player gets the points
            if (current_apple[1] >= 499 and current_apple[1] <= 500) and (
                    current_apple[0] + 10 >= bask1_x
                    and current_apple[0] + 10 <= bask1_x + 70) and (
                        current_apple[0] + 10 >= bask2_x
                        and current_apple[0] + 10 <= bask2_x + 70):
                apples.remove(current_apple)
            elif (current_apple[1] >= 499 and current_apple[1] <= 500) and (
                    current_apple[0] + 10 >= bask1_x
                    and current_apple[0] + 10 <= bask1_x + 70):
                p1_score += 1
                apples.remove(current_apple)
            elif (current_apple[1] >= 499 and current_apple[1] <= 500) and (
                    current_apple[0] + 10 >= bask2_x
                    and current_apple[0] + 10 <= bask2_x + 70):
                p2_score += 1
                apples.remove(current_apple)

            # If fruit hits ground it should be removed
            if current_apple[1] > 520:
                apples.remove(current_apple)

        # Loops through each fruit in fruit storage
        for apple in apples:
            # Displays each apple on the screen
            current_apple = apple
            screen.blit(apple_fall, (current_apple[0], current_apple[1]))

        # If an orange should spawn
        if fruit_num >= 6 and fruit_num <= 9:
            # Orange's position is picked and orange is added to orange list
            fruitX = random.randint(200, 935)
            fruitY = 160
            oranges.append([fruitX, fruitY])
            fruit_num = 0  # Resets fruit choice

        # Loops through each fruit in fruit storage
        for orange in oranges:
            # Single fruit is selected, and has it's y-position changed
            current_orange = orange
            current_orange[1] += 3

            # Checks for fruit collisions with baskets, if both baskets touch the fruit no player gets the points
            if (current_orange[1] >= 499 and current_orange[1] <= 500) and (
                    current_orange[0] + 12 >= bask1_x
                    and current_orange[0] + 12 <= bask1_x + 70) and (
                        current_orange[0] + 12 >= bask2_x
                        and current_orange[0] + 12 <= bask2_x + 70):
                oranges.remove(current_orange)
            elif (current_orange[1] >= 499 and current_orange[1] <= 501) and (
                    current_orange[0] + 12 >= bask1_x
                    and current_orange[0] + 12 <= bask1_x + 70):
                p1_score += 2
                oranges.remove(current_orange)
            elif (current_orange[1] >= 499 and current_orange[1] <= 501) and (
                    current_orange[0] + 12 >= bask2_x
                    and current_orange[0] + 12 <= bask2_x + 70):
                p2_score += 2
                oranges.remove(current_orange)

            # If fruit hits ground it should be removed
            if current_orange[1] > 520:
                oranges.remove(current_orange)

        # Loops through each fruit in fruit storage
        for orange in oranges:
            # Displays each orange on the screen
            current_orange = orange
            screen.blit(orange_fall, (current_orange[0], current_orange[1]))

        # If a pear should spawn
        if fruit_num >= 10 and fruit_num <= 12:
            # Pear's position is picked and pear is added to pear list
            fruitX = random.randint(200, 935)
            fruitY = 160
            pears.append([fruitX, fruitY])
            fruit_num = 0  # Resets fruit choice

        # Loops through each fruit in fruit storage
        for pear in pears:
            # Single fruit is selected, and has it's y-position changed
            current_pear = pear
            current_pear[1] += 4

            # Checks for fruit collisions with baskets, if both baskets touch the fruit no player gets the points
            if (current_pear[1] >= 499 and current_pear[1] <= 500) and (
                    current_pear[0] + 10 >= bask1_x
                    and current_pear[0] + 10 <= bask1_x + 70) and (
                        current_pear[0] + 10 >= bask2_x
                        and current_pear[0] + 10 <= bask2_x + 70):
                pears.remove(current_pear)
            elif (current_pear[1] >= 499 and current_pear[1] <= 502) and (
                    current_pear[0] + 10 >= bask1_x
                    and current_pear[0] + 10 <= bask1_x + 70):
                p1_score += 3
                pears.remove(current_pear)
            elif (current_pear[1] >= 499 and current_pear[1] <= 502) and (
                    current_pear[0] + 10 >= bask2_x
                    and current_pear[0] + 10 <= bask2_x + 70):
                p2_score += 3
                pears.remove(current_pear)

            # If fruit hits ground it should be removed
            if current_pear[1] > 520:
                pears.remove(current_pear)

        # Loops through each fruit in fruit storage
        for pear in pears:
            # Displays each pear on the screen
            current_pear = pear
            screen.blit(pear_fall, (current_pear[0], current_pear[1]))

        # If a peach should spawn
        if fruit_num >= 13 and fruit_num <= 14:
            # Peach's position is picked and peach is added to peach list
            fruitX = random.randint(200, 935)
            fruitY = 160
            peaches.append([fruitX, fruitY])
            fruit_num = 0  # Resets fruit choice

        # Loops through each fruit in fruit storage
        for peach in peaches:
            # Single fruit is selected, and has it's y-position changed
            current_peach = peach
            current_peach[1] += 5

            # Checks for fruit collisions with baskets, if both baskets touch the fruit no player gets the points
            if (current_peach[1] >= 499 and current_peach[1] <= 500) and (
                    current_peach[0] + 12 >= bask1_x
                    and current_peach[0] + 12 <= bask1_x + 70) and (
                        current_peach[0] + 12 >= bask2_x
                        and current_peach[0] + 12 <= bask2_x + 70):
                peaches.remove(current_peach)
            elif (current_peach[1] >= 499 and current_peach[1] <= 503) and (
                    current_peach[0] + 12 >= bask1_x
                    and current_peach[0] + 12 <= bask1_x + 70):
                p1_score += 4
                peaches.remove(current_peach)
            elif (current_peach[1] >= 499 and current_peach[1] <= 503) and (
                    current_peach[0] + 12 >= bask2_x
                    and current_peach[0] + 12 <= bask2_x + 70):
                p2_score += 4
                peaches.remove(current_peach)

            # If fruit hits ground it should be removed
            if current_peach[1] > 520:
                peaches.remove(current_peach)

        # Loops through each fruit in fruit storage
        for peach in peaches:
            # Displays each peach on the screen
            current_peach = peach
            screen.blit(peach_fall, (current_peach[0], current_peach[1]))

        # If a plum should spawn
        if fruit_num == 15:
            # Plum's position is picked and plum is added to plum list
            fruitX = random.randint(200, 935)
            fruitY = 160
            plums.append([fruitX, fruitY])
            fruit_num = 0  # Resets fruit choice

        # Loops through each fruit in fruit storage
        for plum in plums:
            # Single fruit is selected, and has it's y-position changed
            current_plum = plum
            current_plum[1] += 7

            # Checks for fruit collisions with baskets, if both baskets touch the fruit no player gets the points
            if (current_plum[1] >= 499 and current_plum[1] <= 500) and (
                    current_plum[0] + 12 >= bask1_x
                    and current_plum[0] + 12 <= bask1_x + 70) and (
                        current_plum[0] + 12 >= bask2_x
                        and current_plum[0] + 12 <= bask2_x + 70):
                plums.remove(current_plum)
            elif (current_plum[1] >= 499 and current_plum[1] <= 504) and (
                    current_plum[0] + 12 >= bask1_x
                    and current_plum[0] + 12 <= bask1_x + 70):
                p1_score += 4
                plums.remove(current_plum)
            elif (current_plum[1] >= 499 and current_plum[1] <= 504) and (
                    current_plum[0] + 12 >= bask2_x
                    and current_plum[0] + 12 <= bask2_x + 70):
                p2_score += 4
                plums.remove(current_plum)

            # If fruit hits ground it should be removed
            if current_plum[1] > 520:
                plums.remove(current_plum)

        # Loops through each fruit in fruit storage
        for plum in plums:
            # Displays each plum on the screen
            current_plum = plum
            screen.blit(plum_fall, (current_plum[0], current_plum[1]))

        # Checks to see if any player has reached the winning score goal
        if winning_score <= p1_score:
            # If player 1 won, conditions are adjusted accordingly
            run_catch = False
            catch_p1_winner = True
            catch_game_over = True
        elif winning_score <= p2_score:
            # If player 2 won, conditions are adjusted accordingly
            run_catch = False
            catch_p2_winner = True
            catch_game_over = True

        # Checks if catch game is over
        if catch_game_over:
            # Displays game over and restart text
            screen.blit(catch_game_over_text, catch_game_over_text_rect)
            screen.blit(catch_restart_text, catch_restart_text_rect)

            # Depending on the winner, winning player text is displayed
            if catch_p1_winner:
                screen.blit(catch_p1_win_text, catch_p1_win_text_rect)
            elif catch_p2_winner:
                screen.blit(catch_p2_win_text, catch_p2_win_text_rect)

    # Updates the screen with what has been drawn
    pygame.display.flip()

    # Limits the game to a certain integer for frames per second
    clock.tick(FPS)

# Closes the window and quits the pygame program
pygame.quit()
