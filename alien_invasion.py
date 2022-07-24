import sys
import pygame
from settings import Setttings
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

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Inicia o looping principal do jogo"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        numbers_aliens_x = available_space_x // (2 * alien_width)

        # Criando a primeira fila de aliens
        for alien_number in range(numbers_aliens_x):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        """ Criando um alien e inserindo na fila"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_screen(self):
        """Carrega as imagens e mostra a tela mais recente"""
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        pygame.display.flip()

    def _update_bullets(self):
        """Atualiza a posição do projétil e se livra dos projéteis que estão alem da tela"""

        # Atualiza a posição
        self.bullets.update()

        # Se livrando das Munições que estão alem da tela
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)




if __name__ == '__main__':
    # Cria um instancia do jogo e inicia ele
    ai = AlienInvasion()
    ai.run_game()
