import pygame as pg


class Alfabeto:
    def __init__(self, window):
        self.window = window
        self.CliqueLetra = []

    def letrasAlfabeto(self, letrasClicadas):
        self.CliqueLetra = []
        font = pg.font.SysFont("Space Mono", 30)
        alfabeto = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        QtdePorlinhas = [9, 9, 8]  # letras por linha

        x0, y0 = 450, 160
        largura, altura = 320, 180
        padding = 3
        Buttom = (altura - 2 * padding) // 3
        idx = 0

        for NumLinha, numCol in enumerate(QtdePorlinhas):
            larguraBotao = (largura - (numCol - 1) * padding) // numCol
            offset_x = x0 + (largura - (numCol * larguraBotao + (numCol - 1) * padding)) // 2
            y = y0 + NumLinha * (Buttom + padding)
            for col in range(numCol):
                x = offset_x + col * (larguraBotao + padding)
                CorDoFundo = (30, 30, 30)
                CorDoTexto = (150, 150, 150) if alfabeto[idx] in letrasClicadas else (255, 255, 255)
                ret = pg.Rect(x, y, larguraBotao, Buttom)
                pg.draw.rect(self.window, CorDoFundo, ret, border_radius=8)
                LetraImg = font.render(alfabeto[idx], True, CorDoTexto)
                letra_rect = LetraImg.get_rect(center=ret.center)
                self.window.blit(LetraImg, letra_rect)
                self.CliqueLetra.append((ret, alfabeto[idx]))
                idx += 1
