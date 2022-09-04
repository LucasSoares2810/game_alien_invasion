import pygame.font


class Button:

    def __int__(self, ai_game, msg):
        """Inicia os atributos dos botões"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Configura as dimensões a propriedades dos botões
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Contruindo o rect dos botões e centralizando isso
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # O botão de mensagem so precisa ser preparado uma vez
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Reindenizando a mensagem e centralizando o texto"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_botton(self):
        # Desenha um botão em branco e inseri a mensagem
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
