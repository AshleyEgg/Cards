import random
import os
import sys

import pygame
pygame.init()

screen = pygame.display.set_mode((800, 480))
clock = pygame.time.Clock()


###### SYSTEM FUNCTIONS BEGIN #######
def imageLoad(name, card):
    """ Function for loading an image. Makes sure the game is compatible across multiple OS'es, as it
    uses the os.path.join function to get he full filename. It then tries to load the image,
    and raises an exception if it can't, so the user will know specifically what's going if the image loading
    does not work. """

    if card == 1:
        fullname = os.path.join("images/cards/", name)
    else:
        fullname = os.path.join('images', name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()

    return image, image.get_rect()


def display(font, sentence):
    """ Displays text at the bottom of the screen, informing the player of what is going on."""

    displayFont = pygame.font.Font.render(font, sentence, 1, (255, 255, 255), (0, 0, 0))
    return displayFont
###### SYSTEM FUNCTIONS END #######


def play_go_fish():
    print('Lets play go fish2!')
    pass
