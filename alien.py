import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    外星人类 - 代表单个外星敌人
    Alien class - Represents a single alien enemy
    """
    def __init__(self, game):
        """初始化外星人及其初始位置 | Initialize alien and its starting position"""
        super().__init__()
        self.game = game

        # 加载外星人图片 | Load the alien image
        self.image = pygame.image.load('imgs/alien.bmp')
        self.rect = self.image.get_rect()

        # 设置外星人初始位置 | Set alien's initial position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 外星人当前的x轴位置 | Current x-axis position (float for smooth movement)
        self.x = float(self.rect.x)

    def update(self):
        """
        更新外星人位置 | Update alien position
        根据移动方向和速度更新位置 | Updates position based on direction and speed
        """
        self.x += self.game.settings.alien_speed * self.game.settings.alien_direction
        self.rect.x = self.x

    def check_edges(self):
        """
        检查外星人是否到达屏幕边缘 | Check if alien has reached screen edge
        Returns: True if at edge, False otherwise
        """
        screen_rect = self.game.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False
