import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Essa classe representa uma unica Nave Alienigena de uma frota"""

    def __init__(self, ai_game):
        """ Inicia um Alien e configura sua posição inicial """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nova nave no canto esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal da nave alien
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Retorna True se o alien toca a borda da tela"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Movendo as naves alien para direita ou esquerda"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x



