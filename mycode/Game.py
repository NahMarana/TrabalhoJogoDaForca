import pygame

from mycode.Const import MENU_OPTION
from mycode.Menu import Menu
from mycode.JogoForca import JogoForca


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(1136, 768))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                forca = JogoForca(self.window, 'level1', menu_return)
                forca_return = forca.run()
            else:
                pygame.quit()
                quit()
