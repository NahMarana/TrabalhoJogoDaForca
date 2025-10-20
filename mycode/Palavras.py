import random
import pygame
from unidecode import unidecode


class Palavras:
    def __init__(self, window):
        self.window = window
        self.ListPalavras = [
            {"palavra": "ampulheta", "dica": "Objeto que mede o tempo com areia"},
            {"palavra": "bumerangue", "dica": "Objeto que retorna quando lançado"},
            {"palavra": "candelabro", "dica": "Suporte para velas"},
            {"palavra": "crânio", "dica": "Parte óssea que protege o cérebro"},
            {"palavra": "diplomata", "dica": "Profissional que representa seu país"},
            {"palavra": "enigma", "dica": "Mistério ou problema a ser resolvido"},
            {"palavra": "fósforo", "dica": "Objeto usado para acender fogo"},
            {"palavra": "galáxia", "dica": "Sistema de estrelas, planetas e poeira"},
            {"palavra": "helicóptero", "dica": "Aeronave que pode pairar"},
            {"palavra": "ignorar", "dica": "Deixar de prestar atenção"},
            {"palavra": "janela", "dica": "Abertura em uma parede para entrada de luz"},
            {"palavra": "kiwi", "dica": "Fruta pequena e verde com sabor ácido"},
            {"palavra": "lagarto", "dica": "Réptil comum em regiões quentes"},
            {"palavra": "madrasta", "dica": "Mulher que é esposa do pai"},
            {"palavra": "nuvem", "dica": "Massa de vapor no céu"},
            {"palavra": "ódio", "dica": "Sentimento contrário ao amor"},
            {"palavra": "pneumonia", "dica": "Doença que afeta os pulmões"},
            {"palavra": "quimera", "dica": "Criatura mitológica ou ilusão"},
            {"palavra": "ranzinza", "dica": "Pessoa mal-humorada"},
            {"palavra": "safári", "dica": "Expedição para observar animais selvagens"},
            {"palavra": "tangente", "dica": "Linha que toca uma curva em um ponto"},
            {"palavra": "urânio", "dica": "Elemento químico radioativo"},
            {"palavra": "vagabundo", "dica": "Pessoa sem ocupação fixa"},
            {"palavra": "xadrez", "dica": "Jogo de tabuleiro com peças"},
            {"palavra": "zelador", "dica": "Responsável pela manutenção de um prédio"},
            {"palavra": "álbum", "dica": "Coleção de fotos ou músicas"},
            {"palavra": "bactéria", "dica": "Microorganismo invisível a olho nu"},
            {"palavra": "crescente", "dica": "Fase da lua depois da nova"},
            {"palavra": "diploma", "dica": "Certificado de conclusão de curso"},
            {"palavra": "estádio", "dica": "Local para grandes eventos esportivos"}
        ]

        self.PalavrasUsada = ""

    def PalavrasRandom(self):
        self.PalavraUsada = random.choice(self.ListPalavras)  # Faz aparecer aleatoriamente as palavras do ListPalavras criado
        return self.PalavraUsada

    def LinhasDasPalavras(self, letraCorreta):
        # Medidas das linhas para aparição das letras
        linhaX = 150
        linhaY = 600
        EspacosLinhas = 70
        TamanhoDaLinha = 50

        for i, letra in enumerate(self.PalavraUsada["palavra"]):  # For que vai percorrer cada letra da palavra começando do 0
            if letra == " ":
                continue  # Aqui mostra que se a palavra tiver espaço ele vai pular pra próxima linha
                # Difinição do desenho das linhas e posição
            x = linhaX + i * EspacosLinhas
            pygame.draw.line(self.window, (255, 255, 255), (x, linhaY), (x + TamanhoDaLinha, linhaY), 5)
            if unidecode(letra).upper() in letraCorreta:
                # Aqui vai mostrar as letras corretas na posição da linha correta
                fonte = pygame.font.SysFont("Space Mono", 48)
                MostrarLetra = fonte.render(letra.upper(), True, (255, 255, 0))
                Letras = x + (TamanhoDaLinha // 2) - (MostrarLetra.get_width() // 2)
                self.window.blit(MostrarLetra, (Letras, linhaY - 55))

        fonte = pygame.font.SysFont("Space Mono", 36)
        texto = fonte.render(f'Dica: {self.PalavraUsada["dica"]}', True, (255, 255, 0))
        textoRect = texto.get_rect(center=(680 // 2, 680))
        self.window.blit(texto, textoRect)
