import sys
import pygame
from settings import Setttings
from ship import Ship


class AlienInvasion:
    """Classe geral para gerenciar Assets e comportamentos"""

    def __init__(self):
        """Inicializa o jogo e cria os recursos"""
        self.settings = Setttings()
        pygame.init()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_hidth))
        pygame.display.set_caption("Invasão Alien")

        self.ship = Ship(self)

    def run_game(self):
        """Inicia o looping principal do jogo"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Verifica o teclado e o mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move a nave para direta
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # move a anve para direita
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Carrega as imagens e mostra a tela mais recente"""
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Cria um instancia do jogo e inicia ele
    ai = AlienInvasion()
    ai.run_game()
