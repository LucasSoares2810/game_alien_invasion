import sys
import pygame
from settings import Setttings


class AlienInvasion:
    """Classe geral para gerenciar Assets e comportamentos"""

    def __init__(self):
        """Inicializa o jogo e cria os recursos"""
        self.settings = Setttings()
        pygame.init()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_hidth))
        pygame.display.set_caption("Invasão Alien")

    def run_game(self):
        """Inicia o looping principal do jogo"""
        while True:
            """Verifica o teclado e o mouse"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # preenche a cor de fundo a cada passagem pelo Loop
            self.screen.fill(self.settings.bg_color)

            # sempre mostra a tela mais recente
            pygame.display.flip()


if __name__ == '__main__':
    # Cria um instancia do jogo e inicia ele
    ai = AlienInvasion()
    ai.run_game()
