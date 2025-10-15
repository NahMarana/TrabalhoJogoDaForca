import pygame as pg


class Alfabeto:
    def __init__(self, window):
        self.window = window
        self.CliqueLetra = []

    def letrasAlfabeto(self, letrasClicadas):
        self.CliqueLetra = []
        font = pg.font.SysFont("Space Mono", 30)
        alfabeto = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        QtdePorlinhas = [9, 9, 8]  # Para separar as letras do alfabeto em três linhas

        # Medidas para posição dos botões
        x0, y0 = 450, 160
        largura, altura = 320, 180
        padding = 3
        Buttom = (altura - 2 * padding) // 3
        idAlfabeto = 0

        for NumLinha, numCol in enumerate(QtdePorlinhas): # O primeiro for define as linhas e a quantidade de coluna
            # Definições com as medidas de onde cada letra fica dentro do botão
            larguraBotao = (largura - (numCol - 1) * padding) // numCol
            x1 = x0 + (largura - (numCol * larguraBotao + (numCol - 1) * padding)) // 2
            y1 = y0 + NumLinha * (Buttom + padding)
            for col in range(numCol): # Segundo for define cada coluna da linha
                # Criação do formato do botão, cores e medidas de onde vai ficar no jogo
                x = x1 + col * (larguraBotao + padding)
                CorDoFundo = (30, 30, 30)
                CorDoTexto = (150, 150, 150) if alfabeto[idAlfabeto] in letrasClicadas else (255, 255, 255)
                ret = pg.Rect(x, y1, larguraBotao, Buttom)
                pg.draw.rect(self.window, CorDoFundo, ret, border_radius=8)
                LetraImg = font.render(alfabeto[idAlfabeto], True, CorDoTexto)
                letra_rect = LetraImg.get_rect(center=ret.center)
                self.window.blit(LetraImg, letra_rect)
                self.CliqueLetra.append((ret, alfabeto[idAlfabeto]))
                idAlfabeto += 1
