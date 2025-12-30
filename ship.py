import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """
    飞船类 - 代表玩家控制的飞船
    Ship class - Represents the player-controlled ship
    """
    def __init__(self, game):
        """初始化飞船及其初始位置 | Initialize ship and its starting position"""
        super().__init__()
        self.game = game

        # 加载图片 | Load the ship image
        self.image = pygame.image.load(self.game.settings.ship_image_path)
        self.rect = self.image.get_rect()

        # 显示图片在底部 | Display image at bottom of screen
        self.rect.midbottom = self.game.screen.get_rect().midbottom

        # 图片当前所在的x轴位置 | Current x-axis position (float for smooth movement)
        self.x = float(self.rect.x)

        # 移动标识 | Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        更新飞船位置 | Update ship position based on movement flags
        """
        # 向右移动，检查是否超出屏幕边界 | Move right, check screen boundary
        if self.moving_right and self.rect.right < self.game.settings.screen_width:
            self.x += self.game.settings.ship_speed
        # 向左移动，检查是否超出屏幕边界 | Move left, check screen boundary
        if self.moving_left and self.rect.left > 0:
            self.x -= self.game.settings.ship_speed

        # 更新rect对象的位置 | Update rect position from float value
        self.rect.x = self.x

    def draw(self):
        """绘制飞船 | Draw the ship on screen"""
        self.game.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将飞船放在屏幕底部中央 | Reset ship to bottom center of screen"""
        self.rect.midbottom = self.game.screen.get_rect().midbottom
        self.x = float(self.rect.x)
