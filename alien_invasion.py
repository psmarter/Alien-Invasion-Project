from time import sleep

import  pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_status import GameStatus

class AlienInvasion:
    # 初始化界面
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.TITLE)

        self.game_active = True
        self.status = GameStatus(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _ship_hit(self):
        """响应飞船被外星人撞击的事件"""
        if self.status.ships_left > 0:
            # 减少剩余飞船数量
            self.status.ships_left -= 1
            # 清空子弹和外星人
            self.bullets.empty()
            self.aliens.empty()
            # 重新创建外星人舰队
            self._create_fleet()
            # 重置飞船位置
            self.ship.center_ship()
            # 暂停一段时间
            sleep(1)
        else:
            self.game_active = False

    def _check_alien_bottom(self):
        """检查外星人是否到达屏幕底部"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _update_aliens(self):
        """更新外星人位置"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_alien_bottom()

    def _check_fleet_edges(self):
        """检查外星人是否到达屏幕边缘"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """改变外星人舰队的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.alien_direction *= -1

    def _create_fleet(self):
        """创建外星人舰队"""
        alinen = Alien(self)
        alien_width = alinen.rect.width
        alien_height = alinen.rect.height

        current_x, current_y = alien_width, alien_height
        # 计算屏幕可以容纳多少个外星人
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # 重置当前x位置，移动到下一行
            current_y += 2 * alien_height
            current_x = alien_width

    def _create_alien(self, current_x, current_y):
        """创建一个外星人"""
        alien = Alien(self)
        alien.x = current_x
        alien.rect.x = current_x
        alien.rect.y = current_y
        self.aliens.add(alien)

    def run_game(self):
        # 游戏主循环
        while True:
            # 监听事件
            self._check_events()

            if self.game_active:
                # 更新飞船位置
                self.ship.update()
                # 更新子弹位置
                self._update_bullets()
                # 更新外星人位置
                self._update_aliens()

            # 更新屏幕
            self._update_screen()
            # 控制游戏帧率
            self.clock.tick(self.settings.FPS)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键按下事件"""
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
        """响应按键松开事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.draw()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _update_bullets(self):
        """更新子弹位置"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """检查子弹与外星人碰撞"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,False, True)
        if not self.aliens:
            # 如果没有外星人了，重新创建外星人舰队
            self._create_fleet()
            self.bullets.empty()



    def _fire_bullet(self):
        """发射子弹"""
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    # 实例化AlienInvasion类并运行游戏
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()