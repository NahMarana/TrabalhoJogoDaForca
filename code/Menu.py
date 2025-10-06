import pygame.image
from pygame import Rect, Surface
from pygame.font import Font


class Menu:

    def __init__(self, window):
        self.window = window
        self.images = pygame.image.load('./images/imageInicio.png')
        self.rect = self.images.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./sons/music-for-game-fun-kid-game-163649.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.images, dest=self.rect)
            self.menu_text(140, "Jogo da Forca", (202, 111, 77), ((1136 / 2), 280))

            self.menu_text(50, "Iniciar Jogo", (137, 137, 137), ((1136 / 2), 500))
            self.menu_text(50, "Fechar", (137, 137, 137), ((1136 / 2), 540))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Space Mono", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
