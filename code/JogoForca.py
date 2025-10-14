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
        cinza = (30, 30, 30)
        amarelo = (255, 255, 0)
        larguraButtom, alturaButtom = 160, 40
        margemButtom = 20
        margemButtom2 = 20
        x = window.get_width() - margemButtom - 2 * larguraButtom - 10
        y = margemButtom2
        pg.draw.rect(window, cinza, (x, y, larguraButtom, alturaButtom), border_radius=8)
        texto = self.font_rb.render('Jogar Novamente', True, amarelo)
        texto_rect = texto.get_rect(center=(x + larguraButtom // 2, y + alturaButtom // 2))
        window.blit(texto, texto_rect)

    def btMenuInicial(self, window):
        cinza = (30, 30, 30)
        amarelo = (255, 255, 0)
        larguraButtom, alturaButtom = 160, 40
        margemButtom = 20
        margemButtom2 = 20
        x = window.get_width() - margemButtom - larguraButtom
        y = margemButtom2
        pg.draw.rect(window, cinza, (x, y, larguraButtom, alturaButtom), border_radius=8)
        texto = self.font_rb.render('Menu Inicial', True, amarelo)
        texto_rect = texto.get_rect(center=(x + larguraButtom // 2, y + alturaButtom // 2))
        window.blit(texto, texto_rect)

    def run(self):
        rodando = True
        qtdeErros = 6
        chances = 0
        ganhou = False
        perdeu = False
        while rodando:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    rodando = False

                if event.type == pg.KEYDOWN:
                    letra = event.unicode.upper()
                    if letra.isalpha() and len(letra) == 1:
                        if letra not in self.letrasClicadas:
                            self.letrasClicadas.append(letra)
                            if letra in self.Palavras.PalavraUsada:
                                pg.mixer_music.load('./sons/correct-6033.mp3')
                                pg.mixer_music.play()
                            else:
                                chances += 1
                                pg.mixer_music.load('./sons/incorrect-293358.mp3')
                                pg.mixer_music.play()

                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    for ret, letra in self.alfabeto.CliqueLetra:
                        if ret.collidepoint(pos):
                            if letra not in self.letrasClicadas:
                                self.letrasClicadas.append(letra)
                                if letra in self.Palavras.PalavraUsada:
                                    pg.mixer_music.load('./sons/correct.mp3')
                                    pg.mixer_music.play()
                                else:
                                    chances += 1
                                    pg.mixer_music.load('./sons/incorrect.mp3')
                                    pg.mixer_music.play()

                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()

            self.window.blit(self.bg_image, self.rect)
            self.alfabeto.letrasAlfabeto(self.letrasClicadas)
            self.Palavras.LinhasDasPalavras(self.letrasClicadas)
            self.DrawForca(chances)
            self.btJogarNovamente(self.window)
            self.btMenuInicial(self.window)

            if not ganhou and all(letra.upper() in self.letrasClicadas or letra == " " for letra in self.Palavras.PalavraUsada):
                ganhou = True
                pg.mixer_music.load('./sons/applause-cheer-236786.mp3')
                pg.mixer_music.play()

            if not perdeu and chances >= qtdeErros:
                perdeu = True
                pg.mixer_music.load('./sons/fiasco-154915.mp3')
                pg.mixer_music.play()

            if ganhou:
                fonte = pg.font.SysFont("Space Mono", 48)
                texto = fonte.render('Você ganhou!', True, (0, 255, 0))
                textoRect = texto.get_rect(center=(self.window.get_width() // 2, 60))
                self.window.blit(texto, textoRect)
            elif perdeu:
                fonte = pg.font.SysFont("Space Mono", 30)
                texto = fonte.render(f'Você perdeu! A palavra era: {self.Palavras.PalavraUsada}', True, (255, 0, 0))
                textoRect = texto.get_rect(center=(self.window.get_width() // 2, 60))
                self.window.blit(texto, textoRect)



            pg.display.flip()
        pg.quit()
