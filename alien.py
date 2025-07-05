import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        # 加载外星人图片
        self.image = pygame.image.load('imgs/alien.bmp')
        self.rect = self.image.get_rect()

        # 设置外星人初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 外星人当前的x轴位置
        self.x = float(self.rect.x)

    def update(self):
        """更新外星人位置"""
        self.x += self.game.settings.alien_speed * self.game.settings.alien_direction
        self.rect.x = self.x

    def check_edges(self):
        """检查外星人是否到达屏幕边缘"""
        screen_rect = self.game.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False