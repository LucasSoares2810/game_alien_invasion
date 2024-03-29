class Setttings:
    """Uma classe para manipular as configurações do jogo"""
    def __init__(self):
        """Inicia as configurações do jogo"""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (100, 230, 220)

        # Configurações da Nave
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Configurações da munição
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configurações das naves aliens
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10

        # fleet_direction onde 1 representa ir para direita e -1 representa ir para esquerda
        self.fleet_direction = 1
