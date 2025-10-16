import pygame.image
from pygame import Rect, Surface
from pygame.font import Font

from mycode.Const import MENU_OPTION


class Menu:

    def __init__(self, window):
        self.window = window
        self.images = pygame.image.load('./images/imageInicio.png')
        self.rect = self.images.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./sons/music-for-game-fun-kid-game-163649.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.images, dest=self.rect)
            self.menu_text(140, "Jogo da Forca", (202, 111, 77), ((1136 / 2), 280))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], (202, 111, 77), ((1136 / 2), 500 + i * 60))
                else:
                    self.menu_text(40, MENU_OPTION[i], (137, 137, 137), ((1136 / 2), 510 + i * 40))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Space Mono", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
