import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Essa classe representa uma unica Nave Alienigena de uma frota"""

    def __init__(self, ai_game):
        """ Inicia um Alien e configura sua posição inicial """
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nova nave no canto esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal da nave alien
        self.x = float(self.rect.x)
