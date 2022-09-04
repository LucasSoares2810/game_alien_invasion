import sys
from time import sleep
import pygame
from settings import Setttings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Classe geral para gerenciar Assets e comportamentos"""

    def __init__(self):
        """Inicializa o jogo e cria os recursos"""
        pygame.init()
        self.settings = Setttings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_hidth = self.screen.get_rect().height
        pygame.display.set_caption("Invasão Alien")

        # Cria uma instãncia para armazenar as estatísticas do jogo
        self.stats = Ship(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Fazendo um botão de Play
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Inicia o looping principal do jogo"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Verifica o teclado e o mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Renponde a ação de apetar as teclas"""
        if event.key == pygame.K_RIGHT:
            # Move a nave para direta
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move a anve para direita
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a ação de soltar as teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Cria uma nova munição e adiciona ela no grupo"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Criando uma frota de naves aliens"""
        # Criando um alien e encontrando quantos aliens cabem na tela
        # O espaço entre os alien é igual a um alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        numbers_aliens_x = available_space_x // (2 * alien_width)

        # Determinando o numero de filas de naves que cabem na tela
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Criando uma frota completa de aliens
        for row_number in range(number_rows):
            for alien_number in range(numbers_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """ Criando um alien e inserindo na fila"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Responde se o alien alcançou a borda da tela"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
            break

    def _change_fleet_direction(self):
        """Faz a fronta inteira descer e muda a direção"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Carrega as imagens e mostra a tela mais recente"""
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Desenha o botão de Play quando jogo esta inativo
        if not self.stats.game_active:
            self.play_button.draw_botton()

        pygame.display.flip()

    def _update_aliens(self):
        """ Checa de se frota atingiu a borda e então atualiza a posição de todos os aliens da frota"""
        self._check_fleet_edges()
        self.aliens.update()

        # Monitora a colisão entre alien e nave
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Checa os alien atingindo a parte de baixo da tela
        self._check_aliens_bottom()

    def _update_bullets(self):
        """Atualiza a posição do projétil e se livra dos projéteis que estão alem da tela"""

        # Atualiza a posição
        self.bullets.update()

        # Se livrando das Munições que estão alem da tela
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respondendo as colisões entre projétil e alien"""
        # Removendo projétil e nave que colidiram
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destruindo os projéteis e criando uma nova frota
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        """Respondendo a colisão entre alien e nave"""
        if self.stats.ships_left > 0:
            # Diminuindo ship_left
            self.stats.ships_left -= 1

            # Se livrando das alien e projéteis remanescentes
            self.aliens.empty()
            self.bullets.empty()

            # Criando a nova frota e centralizando a nave
            self._create_fleet()
            self.ship.center_ship()

            # Pausa
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """Checando quando um Alien alcança a parte de baixo da tela"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Trata do mesmo jeito se a Nave divesse sido acertada
                self._ship_hit()
                break


if __name__ == '__main__':
    # Cria um instancia do jogo e inicia ele
    ai = AlienInvasion()
    ai.run_game()
