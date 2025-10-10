import random
import pygame as pg
from code.Alfabeto import Alfabeto


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
        self.letrasClicadas = []

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


    def run(self, ):
        rodando = True
        while rodando:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    rodando = False
            self.window.blit(self.bg_image, self.rect)
            self.DrawForca(0)
            self.alfabeto.letrasAlfabeto(self.letrasClicadas)
            pg.display.flip()
        pg.quit()
