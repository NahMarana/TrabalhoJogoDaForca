import random
import pygame


class Palavras:
    def __init__(self, window):
        self.window = window
        self.ListPalavras = ["CARRO", "CACHORRO", "CANECA", "LAPIS DE COR"]
        self.PalavrasUsada = ""  # Palavra sorteada atual

    def PalavrasRandom(self):
        self.PalavraUsada = random.choice(self.ListPalavras)
        return self.PalavraUsada

    def LinhasDasPalavras(self, letraCorreta):
        linhaX = 150
        linhaY = 650
        EspacosLinhas = 70
        TamanhoDaLinha = 50

        for i, letra in enumerate(self.PalavraUsada):
            if letra == " ":
                continue
            x = linhaX + i * EspacosLinhas
            pygame.draw.line(self.window, (255, 255, 255), (x, linhaY), (x + TamanhoDaLinha, linhaY), 5)
            if letra.upper() in letraCorreta:
                fonte = pygame.font.SysFont("Space Mono", 48)
                MostrarLetra = fonte.render(letra.upper(), True, (255, 255, 0))
                Letras = x + (TamanhoDaLinha // 2) - (MostrarLetra.get_width() // 2)
                self.window.blit(MostrarLetra, (Letras, linhaY - 55))
