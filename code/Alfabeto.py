import pygame as pg


class Alfabeto:
    def __init__(self, window):
        self.window = window

    #
    # def letrasAlfabeto(self, letrasClicadas):
    #     font = pygame.font.SysFont("Space Mono", 30)
    #     alfabeto = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    #
    #     for idx, letra in enumerate(alfabeto):
    #         x = 50 + (idx % 13) * 30
    #         y = 100 + (idx // 13) * 30
    #         color = (150, 150, 150) if letra in letrasClicadas else (70, 70, 255)
    #         mostrarLetra = font.render(letra, True, color)
    #         rect = mostrarLetra.get_rect(topleft=(x, y))
    #         self.window.blit(mostrarLetra, rect)

    def letrasAlfabeto(self, letrasClicadas):
        font = pg.font.SysFont("Space Mono", 30)
        alfabeto = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        QtdePorlinhas = [9, 9, 8]  # letras por linha

        x0, y0 = 450, 160  # ajuste fino de acordo com seu retângulo
        largura, altura = 320, 180
        padding = 3
        altura_botao = (altura - 2 * padding) // 3
        idx = 0

        for linha, num_col in enumerate(QtdePorlinhas):
            largura_botao = (largura - (num_col - 1) * padding) // num_col
            offset_x = x0 + (largura - (num_col * largura_botao + (num_col - 1) * padding)) // 2
            y = y0 + linha * (altura_botao + padding)
            for col in range(num_col):
                x = offset_x + col * (largura_botao + padding)
                cor_fundo = (30, 30, 30)
                cor_texto = (150, 150, 150) if alfabeto[idx] in letrasClicadas else (255, 255, 255)
                ret = pg.Rect(x, y, largura_botao, altura_botao)
                pg.draw.rect(self.window, cor_fundo, ret, border_radius=8)
                letra_img = font.render(alfabeto[idx], True, cor_texto)
                letra_rect = letra_img.get_rect(center=ret.center)
                self.window.blit(letra_img, letra_rect)
                idx += 1
