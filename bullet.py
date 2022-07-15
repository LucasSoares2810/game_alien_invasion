import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Uma classe para manipular a municão atirada pela Nave"""

    def __init__(self, ai_game):
        """Cria a munição na mesma posição da Nave"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Cria um rect para munição e então configura uma posição
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Armazena a posição das munições num valor decimal
        self.y = float(self.rect.y)

    def update(self):
        """Faz a munição se movimentar na tela"""

        # Atualiza a posição deciaml da munição
        self.y -= self.settings.bullet_speed

        # Atualiza a posição do rect da munição
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenah a munição na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)
