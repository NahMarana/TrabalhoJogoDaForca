import pygame

from code.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(1136, 768))

    def run(self):
        pygame.mixer_music.load('./sons/music-for-game-fun-kid-game-163649.mp3')
        pygame.mixer_music.play(-1)

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()  # Close Window
            #        quit()  # end pygame
