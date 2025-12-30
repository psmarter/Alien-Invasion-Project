import pygame.font

class Button:
    """
    按钮类 - 创建游戏UI按钮
    Button class - Creates game UI buttons
    """
    def __init__(self, game, msg):
        """
        初始化按钮属性 | Initialize button attributes
        Args:
            game: Game instance
            msg: Button text message
        """
        self.game = game
        self.font = pygame.font.SysFont(None, self.game.settings.button_font)

        # 设置按钮尺寸和位置 | Set button dimensions and position
        self.rect = pygame.Rect(0, 0, self.game.settings.button_width, self.game.settings.button_height)
        self.rect.center = self.game.screen.get_rect().center

        self._pre_msg(msg)

    def _pre_msg(self, msg):
        """
        将msg渲染为图像 | Render msg as an image
        准备按钮文本图像 | Prepare button text image
        """
        self.msg_image = self.font.render(msg, True, self.game.settings.button_text_color, self.game.settings.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """
        绘制按钮 | Draw the button on screen
        绘制按钮背景和文本 | Draw button background and text
        """
        self.game.screen.fill(self.game.settings.button_color, self.rect)
        self.game.screen.blit(self.msg_image, self.msg_image_rect)
