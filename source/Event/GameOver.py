import sys
import pygame

from Process import HighScore
from Setup import GlobalVars


def _quit_all():
    HighScore.add_new_score()
    print(GlobalVars.game_board)
    print("Score:", GlobalVars.score)

    GlobalVars.game_running = False
    pygame.quit()
    sys.exit()


# Checks if the window's red x button has been pressed
def quit_pressed(events):
    for event in events:
        if event.type == pygame.QUIT:
            _quit_all()


def top_out():
    print("Topped out!")
    _quit_all()
