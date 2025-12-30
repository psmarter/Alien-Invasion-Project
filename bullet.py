import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    子弹类 - 管理飞船发射的子弹
    Bullet class - Manages bullets fired from the ship
    """
    def __init__(self, game):
        """创建一个子弹对象 | Create a bullet object at ship's current position"""
        super().__init__()
        self.game = game

        # 设置子弹的属性 | Set bullet properties
        self.color = self.game.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.game.settings.bullet_width, self.game.settings.bullet_height)

        # 将子弹放在飞船的顶部 | Position bullet at ship's top
        self.rect.midtop = self.game.ship.rect.midtop

        # 存储子弹位置为浮点数 | Store bullet position as float for smooth movement
        self.y = float(self.rect.y)

    def update(self):
        """
        更新子弹位置 | Update bullet position
        向上移动子弹 | Move bullet upward on screen
        """
        self.y -= self.game.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        """绘制子弹 | Draw the bullet on screen"""
        pygame.draw.rect(self.game.screen, self.color, self.rect)
