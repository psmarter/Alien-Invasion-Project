import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        # 设置子弹的属性
        self.color = self.game.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.game.settings.bullet_width, self.game.settings.bullet_height)

        # 将子弹放在飞船的顶部
        self.rect.midtop = self.game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """更新子弹位置"""
        self.y -= self.game.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        """绘制子弹"""
        pygame.draw.rect(self.game.screen, self.color, self.rect)