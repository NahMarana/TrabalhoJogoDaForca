import random
import pygame as pg
from code.Alfabeto import Alfabeto
from code.Palavras import Palavras


class JogoForca:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.bg_images = ['./images/image1.png', './images/image2.png', './images/image3.png', './images/image4.png',
                          './images/image5.png', './images/image6.png']
        self.bg_image = pg.image.load(random.choice(self.bg_images))
        self.rect = self.bg_image.get_rect(left=0, top=0)
        self.menu_option = menu_option
        self.alfabeto = Alfabeto(window)
        self.Palavras = Palavras(window)
        self.letrasClicadas = []
        self.Palavras.PalavrasRandom()
        self.font_rb = pg.font.SysFont("Space Mono", 25)

    def DrawForca(self, qtdeErros):
        branco = (255, 255, 255)
        pg.draw.line(self.window, branco, (100, 500), (100, 100), 10)
        pg.draw.line(self.window, branco, (50, 500), (150, 500), 10)
        pg.draw.line(self.window, branco, (100, 100), (300, 100), 10)
        pg.draw.line(self.window, branco, (300, 100), (300, 150), 10)

        if qtdeErros >= 1: pg.draw.circle(self.window, branco, (300, 200), 50, 10)  # Cabeça
        if qtdeErros >= 2: pg.draw.line(self.window, branco, (300, 250), (300, 350), 10)  # Tronco
        if qtdeErros >= 3: pg.draw.line(self.window, branco, (300, 260), (225, 350), 10)  # Braço esq
        if qtdeErros >= 4: pg.draw.line(self.window, branco, (300, 260), (375, 350), 10)  # Braço dir
        if qtdeErros >= 5: pg.draw.line(self.window, branco, (300, 350), (375, 450), 10)  # Perna esq
        if qtdeErros >= 6: pg.draw.line(self.window, branco, (300, 350), (225, 450), 10)  # Perna dir

    def btJogarNovamente(self, window):
        branco = (255, 255, 255)
        Amarelo = (255, 255, 0)
        larguraButtom, alturaButtom = 160, 40
        btX, btY = 600, 80
        pg.draw.rect(window, branco, (btX, btY, larguraButtom, alturaButtom), border_radius=8)
        texto = self.font_rb.render('Jogar Novamente', True, Amarelo)
        window.blit(texto, (600, 120))

    def btMenuInicial(self, window):
        branco = (255, 255, 255)
        Amarelo = (255, 255, 0)
        larguraButtom, alturaButtom = 160, 40
        btX, btY = 500, 80
        pg.draw.rect(window, branco, (btX, btY, larguraButtom, alturaButtom), border_radius=8)
        texto = self.font_rb.render('Menu Inicial', True, Amarelo)
        window.blit(texto, (600, 120))

    def run(self):
        rodando = True
        qtdeErros = 6
        chances = 0
        while rodando:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    rodando = False

                if event.type == pg.KEYDOWN:
                    letra = event.unicode.upper()
                    if letra.isalpha() and len(letra) == 1:
                        if letra not in self.letrasClicadas:
                            self.letrasClicadas.append(letra)
                            if letra not in self.Palavras.PalavraUsada:
                                chances += 1

                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    for ret, letra in self.alfabeto.CliqueLetra:
                        if ret.collidepoint(pos):
                            if letra not in self.letrasClicadas:
                                self.letrasClicadas.append(letra)
                                if letra not in self.Palavras.PalavraUsada:
                                    chances += 1

            self.window.blit(self.bg_image, self.rect)
            self.alfabeto.letrasAlfabeto(self.letrasClicadas)
            self.Palavras.LinhasDasPalavras(self.letrasClicadas)
            self.DrawForca(chances)
            self.btJogarNovamente(self.window)
            self.btMenuInicial(self.window)

            if chances >= qtdeErros:
                rodando = False
            if all(letra.upper() in self.letrasClicadas or letra == " " for letra in self.Palavras.PalavraUsada):
                rodando = False

            pg.display.flip()
        pg.quit()


