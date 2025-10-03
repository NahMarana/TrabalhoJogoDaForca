import pygame.image


class Menu:

    def __init__(self, window):
        self.window = window
        self.images = pygame.image.load('./images/imageInicio.png')
        self.rect = self.images.get_rect(left=0, top=0)

    def run(self, ):
        self.window.blit(source=self.images, dest=self.rect)
        pygame.display.flip()
        pass