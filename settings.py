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
        self.ship_speed = 3

        # 子弹设置
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_limit = 10