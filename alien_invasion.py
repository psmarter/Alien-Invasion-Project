from time import sleep

import  pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_status import GameStatus
from button import Button
from gamescore import GameScore

class AlienInvasion:
    """
    管理游戏资源和行为的总类 | Overall class to manage game assets and behavior
    """
    def __init__(self):
        """
        初始化游戏并创建游戏资源 | Initialize the game and create game resources
        """
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.TITLE)

        # 游戏状态 | Game state
        self.game_active = False

        # 创建游戏对象 | Create game objects
        self.play_button = Button(self, self.settings.play_button_text)
        self.status = GameStatus(self)

        self.score = GameScore(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()  # 存储子弹的组 | Group to store bullets
        self.aliens = pygame.sprite.Group()  # 存储外星人的组 | Group to store aliens

        self._create_fleet()

    def _ship_hit(self):
        """
        响应飞船被外星人撞击的事件 | Respond to ship being hit by alien
        减少飞船数量并重置游戏 | Decrease ships left and reset game
        """
        if self.status.ships_left > 0:
            # 减少剩余飞船数量 | Decrement ships_left
            self.status.ships_left -= 1
            self.score.prep_ships()
            # 清空子弹和外星人 | Clear bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            # 重新创建外星人舰队 | Create new fleet
            self._create_fleet()
            # 重置飞船位置 | Center the ship
            self.ship.center_ship()
            # 暂停一段时间 | Pause
            sleep(1)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)  # 显示光标 | Show mouse cursor

    def _check_alien_bottom(self):
        """
        检查外星人是否到达屏幕底部 | Check if any aliens have reached the bottom
        """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _update_aliens(self):
        """
        更新外星人位置 | Update alien positions
        检查碰撞 | Check for collisions
        """
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船的碰撞 | Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_alien_bottom()

    def _check_fleet_edges(self):
        """
        检查外星人是否到达屏幕边缘 | Check if any aliens have reached an edge
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """
        改变外星人舰队的方向 | Drop the entire fleet and change direction
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.alien_direction *= -1

    def _create_fleet(self):
        """
        创建外星人舰队 | Create the fleet of aliens
        """
        alinen = Alien(self)
        alien_width = alinen.rect.width
        alien_height = alinen.rect.height

        current_x, current_y = alien_width, alien_height
        # 计算屏幕可以容纳多少个外星人 | Calculate how many aliens fit on screen
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # 重置当前x位置，移动到下一行 | Reset x, move to next row
            current_y += 2 * alien_height
            current_x = alien_width

    def _create_alien(self, current_x, current_y):
        """
        创建一个外星人 | Create an alien and place it in the fleet
        """
        alien = Alien(self)
        alien.x = current_x
        alien.rect.x = current_x
        alien.rect.y = current_y
        self.aliens.add(alien)

    def run_game(self):
        """
        开始游戏的主循环 | Start the main loop for the game
        """
        while True:
            # 监听事件 | Watch for keyboard and mouse events
            self._check_events()

            if self.game_active:
                # 更新飞船位置 | Update ship position
                self.ship.update()
                # 更新子弹位置 | Update bullet positions
                self._update_bullets()
                # 更新外星人位置 | Update alien positions
                self._update_aliens()

            # 更新屏幕 | Update screen
            self._update_screen()
            # 控制游戏帧率 | Control frame rate
            self.clock.tick(self.settings.FPS)

    def _check_events(self):
        """
        响应按键和鼠标事件 | Respond to keypresses and mouse events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP and self.game_active:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """
        响应Play按钮的点击事件 | Start a new game when player clicks Play
        """
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            # 重置游戏设置 | Reset game settings
            self.settings.init_settings()
            self.status.reset_status()
            self.score.prep_score()
            self.score.prep_level()
            self.score.prep_ships()
            self.game_active = True

            # 清空子弹和外星人 | Clear sprites
            self.bullets.empty()
            self.aliens.empty()

            # 创建新的外星人舰队 | Create new fleet
            self._create_fleet()

            # 重置飞船位置 | Center ship
            self.ship.center_ship()

            # 隐藏光标 | Hide mouse cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """
        响应按键按下事件 | Respond to keypresses
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """
        响应按键松开事件 | Respond to key releases
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """
        更新屏幕上的图像并切换到新屏幕 | Update images on screen and flip to new screen
        """
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.draw()
        self.aliens.draw(self.screen)

        self.score.show_score()

        if not self.game_active:
            self.play_button.draw()

        pygame.display.flip()

    def _update_bullets(self):
        """
        更新子弹位置并删除旧子弹 | Update bullet positions and remove old bullets
        """
        self.bullets.update()
        # 删除消失的子弹 | Remove bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """
        检查子弹与外星人碰撞 | Respond to bullet-alien collisions
        """
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,False, True)

        if collisions:
            # 计算分数 | Award points
            for aliens in collisions.values():
                self.status.score +=  self.settings.alien_points * len(aliens)
            self.score.prep_score()
            self.score.check_high_score()

        if not self.aliens:
            # 如果没有外星人了，重新创建外星人舰队 | If fleet destroyed, start new level
            self._create_fleet()
            self.bullets.empty()
            self.settings.increase_speed()

            # 提升关卡 | Increase level
            self.status.level += 1
            self.score.prep_level()

    def _fire_bullet(self):
        """
        发射子弹 | Create a new bullet and add it to the bullets group
        """
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    # 创建游戏实例并运行 | Make a game instance and run the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()