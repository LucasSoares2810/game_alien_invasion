class Setttings:
    """Uma classe para manipular as configurações do jogo"""
    def __init__(self):
        """Inicia as configurações do jogo"""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (100, 230, 220)
        self.ship_speed = 1.5

        # Configurações da munição
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
