import random
import pygame as pg
from mycode.Alfabeto import Alfabeto
from mycode.Palavras import Palavras
from unidecode import unidecode


class JogoForca:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.bgImages = ['./images/image1.png', './images/image2.png', './images/image3.png', './images/image4.png',
                         './images/image5.png', './images/image6.png']
        self.bgImage = pg.image.load(random.choice(self.bgImages))  # Muda aleatoriamente as imagens de fundo cada vez que vai jogar
        self.rect = self.bgImage.get_rect(left=0, top=0)
        self.menu_option = menu_option
        self.alfabeto = Alfabeto(window)
        self.Palavras = Palavras(window)
        self.letrasClicadas = []  # Armazena as letras clicadas pelo usuário
        self.Palavras.PalavrasRandom()  # Escolhe aleatoriamente cada palavra do jogo
        self.font_rb = pg.font.SysFont("Space Mono", 25)

    def DrawForca(self, qtdeErros):
        # Desenho da forca
        branco = (255, 255, 255)
        pg.draw.line(self.window, branco, (100, 500), (100, 100), 10)
        pg.draw.line(self.window, branco, (50, 500), (150, 500), 10)
        pg.draw.line(self.window, branco, (100, 100), (300, 100), 10)
        pg.draw.line(self.window, branco, (300, 100), (300, 150), 10)

        # Desenha cada membro do boneco na forca toda vez que clica em uma letra errada
        if qtdeErros >= 1: pg.draw.circle(self.window, branco, (300, 200), 50, 10)
        if qtdeErros >= 2: pg.draw.line(self.window, branco, (300, 250), (300, 350), 10)
        if qtdeErros >= 3: pg.draw.line(self.window, branco, (300, 260), (225, 350), 10)
        if qtdeErros >= 4: pg.draw.line(self.window, branco, (300, 260), (375, 350), 10)
        if qtdeErros >= 5: pg.draw.line(self.window, branco, (300, 350), (375, 450), 10)
        if qtdeErros >= 6: pg.draw.line(self.window, branco, (300, 350), (225, 450), 10)

    def btJogarNovamente(self, window):  # Criação do botão Jogar novamente
        # Definições do tamanho do botão, cores e onde vai ficar posicionado dentro do jogo
        cinza = (30, 30, 30)
        amarelo = (255, 255, 0),
        larguraButtom, alturaButtom = 160, 40
        margemButtom = 20
        margemButtom2 = 20
        x = window.get_width() - margemButtom - 2 * larguraButtom - 10
        y = margemButtom2
        rect = pg.Rect(x, y, larguraButtom, alturaButtom)
        pg.draw.rect(window, cinza, (x, y, larguraButtom, alturaButtom), border_radius=8)
        texto = self.font_rb.render('Jogar Novamente', True, amarelo)
        textoRect = texto.get_rect(center=(x + larguraButtom // 2, y + alturaButtom // 2))
        window.blit(texto, textoRect)
        return rect

    def btMenuInicial(self, window):  # Criação do botão Menu Inicial
        # Definições do tamanho do botão, cores e onde vai ficar posicionado dentro do jogo
        cinza = (30, 30, 30)
        amarelo = (255, 255, 0)
        larguraButtom, alturaButtom = 160, 40
        margemButtom = 20
        margemButtom2 = 20
        x = window.get_width() - margemButtom - larguraButtom
        y = margemButtom2
        rect = pg.Rect(x, y, larguraButtom, alturaButtom)
        pg.draw.rect(window, cinza, (x, y, larguraButtom, alturaButtom), border_radius=8)
        texto = self.font_rb.render('Menu Inicial', True, amarelo)
        textoRect = texto.get_rect(center=(x + larguraButtom // 2, y + alturaButtom // 2))
        window.blit(texto, textoRect)
        return rect

    def run(self):
        rodandoJogo = True
        qtdeErros = 6
        chances = 0
        ganhou = False
        perdeu = False

        while rodandoJogo:  # Loop que inicia o jogo
            # Faz aparecer na tela os elementos criados
            self.window.blit(self.bgImage, self.rect)
            self.alfabeto.letrasAlfabeto(self.letrasClicadas)
            self.Palavras.LinhasDasPalavras(self.letrasClicadas)
            self.DrawForca(chances)
            btJogarNovamente_rect = self.btJogarNovamente(self.window)
            btMenuInicial_rect = self.btMenuInicial(self.window)

            for event in pg.event.get():  #
                if event.type == pg.QUIT:
                    rodandoJogo = False

                if event.type == pg.KEYDOWN:  # Evento para clicar nas letras pelo teclado
                    letra = event.unicode.upper()
                    if letra.isalpha() and len(letra) == 1:
                        if letra not in self.letrasClicadas:
                            self.letrasClicadas.append(letra)  # Adição das letras que já foram clicadas
                            # Se a letra está correta vai tocar uma musica de acerto
                            if letra in unidecode(self.Palavras.PalavraUsada["palavra"]).upper(): # acrescentei a unidecode para
                                    # transformar as letras que continham acentuação
                                pg.mixer_music.load('./sons/correct-6033.mp3')
                                pg.mixer_music.play()
                            # Se a letra está incorreta vai tocar uma musica de erro
                            else:
                                chances += 1
                                pg.mixer_music.load('./sons/incorrect-293358.mp3')
                                pg.mixer_music.play()

                if event.type == pg.MOUSEBUTTONDOWN:  # Evento para clicar nas letras pelo mouse
                    pos = pg.mouse.get_pos()
                    for ret, letra in self.alfabeto.CliqueLetra:
                        if ret.collidepoint(pos):  # Verificar se clicou dentro do botão
                            if letra not in self.letrasClicadas:
                                self.letrasClicadas.append(letra)  # Adição das letras que já foram clicadas
                                # Se a letra está correta vai tocar uma musica de acerto
                                if letra in unidecode(self.Palavras.PalavraUsada["palavra"]).upper(): # acrescentei a unidecode para
                                    # transformar as letras que continham acentuação
                                    pg.mixer_music.load('./sons/correct-6033.mp3')
                                    pg.mixer_music.play()
                                # Se a letra está incorreta vai tocar uma musica de erro
                                else:
                                    chances += 1
                                    pg.mixer_music.load('./sons/incorrect-293358.mp3')
                                    pg.mixer_music.play()

                    if btMenuInicial_rect.collidepoint(pos):  # Clicando no botão Menu Inicial ele retorna para a tela de Menu
                        return 'Menu'
                    if btJogarNovamente_rect.collidepoint(pos):  # Clicando em Jogar novamente, vai resetar tudo: Letras, texto,
                        # chances e mudar novamente o plano de fundo
                        self.letrasClicadas = []
                        self.Palavras.PalavrasRandom()
                        chances = 0
                        ganhou = False
                        perdeu = False
                        self.bgImage = pg.image.load(random.choice(self.bgImages))

            # Vai checar se ganhou, olhando todas as letras e espaços
            if not ganhou and all(letra.upper() in self.letrasClicadas or letra == " " for letra in self.Palavras.PalavraUsada["palavra"].upper()):
                ganhou = True
                pg.mixer_music.load('./sons/applause-cheer-236786.mp3')  # Se ganhar o jogo vai tocar uma música de vitória
                pg.mixer_music.play()

            # Vai checar se perdeu, se usou todas as quantidades de erros
            if not perdeu and chances >= qtdeErros:
                perdeu = True
                pg.mixer_music.load('./sons/fiasco-154915.mp3')  # Se perder o jogo vai tocar uma música de derrota
                pg.mixer_music.play()

            # Aqui assim que houver uma vitória vai aparecer um texto na tela dizendo que Ganhou o Jogo
            if ganhou:
                fonte = pg.font.SysFont("Space Mono", 48)
                texto = fonte.render('Você ganhou!', True, (0, 255, 0))
                textoRect = texto.get_rect(center=(self.window.get_width() // 2, 60))
                self.window.blit(texto, textoRect)
            # Aqui assim que houver uma derrota vai aparecer um texto na tela dizendo que perdeu e qual era a palavra correta
            elif perdeu:
                fonte = pg.font.SysFont("Space Mono", 30)
                texto = fonte.render(f'Você perdeu! A palavra era: {self.Palavras.PalavraUsada["palavra"]}', True, (255, 0, 0))
                textoRect = texto.get_rect(center=(self.window.get_width() // 2, 60))
                self.window.blit(texto, textoRect)

            pg.display.flip()
        pg.quit()
