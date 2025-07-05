class Settings:
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.FPS = 90
        self.TITLE = "外星人来喽"

        # 飞船设置
        self.ship_image_path = 'imgs/ship.bmp'
        self.ship_speed = 30
        self.ship_limit = 2

        # 子弹设置
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 10
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_limit = 10

        # 外星人设置
        self.alien_speed = 10
        self.alien_drop_speed = 10
        self.alien_direction = 1  # 1表示向右移动，-1表示向左移动