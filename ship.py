import pygame


class Ship:
    """Classe para manipular a nave espacial"""

    def __init__(self, ai_game):
        """Inicia a Nave e a coloca na posição inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem e pega o rect da Nave
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nova Nave na parte de baixo da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # controle de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da Nave com base self.moving"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Desenha a Nave na sua atual localização"""
        self.screen.blit(self.image, self.rect)
