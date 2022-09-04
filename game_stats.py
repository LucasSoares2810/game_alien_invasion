

class GameStats:
    """Rastreia as estáticas do jogo"""

    def __init__(self, ai_games):
        """Inicializa as estatísticas"""
        self.settings = ai_games.settings
        self.reset_stats()
        # Inicia uma invasão Alien no estado ativo
        self.game_active = False

    def reset_stats(self):
        """Inicializa as estatísticas que podem mudar durante o jogo"""
        self.ships_left = self.settings.ship_limit