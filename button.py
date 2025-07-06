import pygame.font

class Button:
    def __init__(self, game, msg):
        self.game = game
        self.font = pygame.font.SysFont(None, self.game.settings.button_font)

        self.rect = pygame.Rect(0, 0, self.game.settings.button_width, self.game.settings.button_height)
        self.rect.center = self.game.screen.get_rect().center

        self._pre_msg(msg)

    def _pre_msg(self, msg):
        """将msg渲染为图像"""
        self.msg_image = self.font.render(msg, True, self.game.settings.button_text_color, self.game.settings.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """绘制按钮"""
        self.game.screen.fill(self.game.settings.button_color, self.rect)
        self.game.screen.blit(self.msg_image, self.msg_image_rect)