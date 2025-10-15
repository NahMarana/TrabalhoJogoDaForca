import random
import pygame

class Palavras:
    def __init__(self, window):
        self.window = window
        self.ListPalavras = ["CARRO", "CACHORRO", "CANECA", "LAPIS DE COR"]
        self.PalavrasUsada = ""

    def PalavrasRandom(self):
        self.PalavraUsada = random.choice(self.ListPalavras) # Faz aparecer aleatoriamente as palavras do ListPalavras criado
        return self.PalavraUsada

    def LinhasDasPalavras(self, letraCorreta):
        # Medidas das linhas para aparição das letras
        linhaX = 150
        linhaY = 650
        EspacosLinhas = 70
        TamanhoDaLinha = 50

        for i, letra in enumerate(self.PalavraUsada): # For que vai percorrer cada letra da palavra começando do 0
            if letra == " ":
                continue # Aqui mostra que se a palavra tiver espaço ele vai pular pra próxima linha
                # Difinição do desenho das linhas e posição
            x = linhaX + i * EspacosLinhas
            pygame.draw.line(self.window, (255, 255, 255), (x, linhaY), (x + TamanhoDaLinha, linhaY), 5)
            if letra.upper() in letraCorreta:
                # Aqui vai mostrar as letras corretas na posição da linha correta
                fonte = pygame.font.SysFont("Space Mono", 48)
                MostrarLetra = fonte.render(letra.upper(), True, (255, 255, 0))
                Letras = x + (TamanhoDaLinha // 2) - (MostrarLetra.get_width() // 2)
                self.window.blit(MostrarLetra, (Letras, linhaY - 55))
