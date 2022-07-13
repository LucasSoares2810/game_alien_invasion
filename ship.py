import pygame


class Ship:
    """Classe para manipular a nave espacial"""

    def __init__(self, ai_game):
        """Inicia a Nave e a coloca na posição inicial"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem e pega o rect da Nave
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nova Nave na parte de baixo da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena um valor decimal para o movimento horizontal da nave
        self.x = float(self.rect.x)

        # controle de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da Nave com base self.moving"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Desenha a Nave na sua atual localização"""
        self.screen.blit(self.image, self.rect)
