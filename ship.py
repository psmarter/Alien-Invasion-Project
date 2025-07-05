import pygame

class Ship:
    def __init__(self, game):
        self.game = game

        # 加载图片
        self.image = pygame.image.load(self.game.settings.ship_image_path)
        self.rect = self.image.get_rect()

        # 显示图片在底部
        self.rect.midbottom = self.game.screen.get_rect().midbottom

        # 图片当前所在的x轴位置
        self.x = float(self.rect.x)

        # 移动标识
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """更新飞船位置"""
        if self.moving_right and self.rect.right < self.game.settings.screen_width:
            self.x += self.game.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.game.settings.ship_speed

        # 更新rect对象的位置
        self.rect.x = self.x

    def draw(self):
        """绘制飞船"""
        self.game.screen.blit(self.image, self.rect)