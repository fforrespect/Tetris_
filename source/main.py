import pygame

from Display import Window, Numbers, Overlays
from Event import GameOver
from Game import Board, Tetromino
from Setup import Constants, GlobalVars

# Set up pygame
pygame.init()
screen: pygame.Surface = pygame.display.set_mode(Constants.SCREEN_SIZE)
clock: pygame.time.Clock = pygame.time.Clock()

# Set up game
Overlays.init()
GlobalVars.game_board = Board.Board()
Numbers.init()

Tetromino.generate_new()

while GlobalVars.game_running:
    # Loop processing #
    clock.tick(Constants.FPS)

    GlobalVars.elapsed_frames += 1

    # Checks if the red x has been pressed, and quits the game if so
    GameOver.quit_pressed(pygame.event.get())
    # End processing #

    keys: tuple[bool] = pygame.key.get_pressed()

    if GlobalVars.active_tetromino is not None:
        GlobalVars.active_tetromino.move(keys)

    # Finally, draw everything to the screen
    Window.display(screen)
