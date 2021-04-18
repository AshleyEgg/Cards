import pygame
import pygame_menu
import GoFish

pygame.init()
surface = pygame.display.set_mode((600, 400))

# Basic menu to build off of to select the user, game, and difficulty
# TODO: Adapt menu to show game types

# def change_background_color(selected_value, color, **kwargs):
#     value_tuple, index = selected_value
#     print('Change widget color to', value_tuple[0])  # selected_value ('Color', surface, color)
#     if color == (-1, -1, -1):  # Generate a random color
#         color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
#     widget: 'pygame_menu.widgets.Selector' = kwargs.get('widget')
#     widget.update_font({'selected_color': color})
#     widget.get_selection_effect().color = color


def start_the_game(selected_value, game, **kwargs):
    value_tuple, index = selected_value
    print('Step 1')
    if value_tuple[1] == 1:
        print('Lets play go fish1!')
        GoFish.play_go_fish()
    else:
        print('Lets play other!')
        pass


menu = pygame_menu.Menu('Welcome', 500, 400, theme=pygame_menu.themes.THEME_BLUE)

games = [('GoFish', 1),
         ('BlackJack', 2),
         ('BlackJack Training', 3)]

menu.add.text_input('Name :', default='Ashley')
selector_game = menu.add.selector(
    title='Select Game',
    items=games,
    onreturn=start_the_game
)
#menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
