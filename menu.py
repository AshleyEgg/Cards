import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))

# Basic menu to build off of to select the user, game, and difficulty
# TODO: Adapt menu to show game types


def start_the_game():
    # Do the job here !
    pass


menu = pygame_menu.Menu(400, 500, 'Welcome', theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Ashley')
menu.add.dropselect(
    title='Select Game',
    items=[('GoFish', 1), ('BlackJack', 2), ('BlackJack Training', 3)]
)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
