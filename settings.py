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

        # 按钮设置
        self.button_color = (0, 255, 0)
        self.button_width = 200
        self.button_height = 50
        self.button_text_color = (255, 255, 255)
        self.button_font = 48
        self.play_button_text = "Play"

        # 游戏速度设置
        self.speed_scale = 1.1
        self.init_settings()

        # 游戏分数设置
        self.score_text_color = (30, 30, 30)
        self.score_font = 48
        self.score_scale = 1.5

    def init_settings(self):
        """初始化游戏的动态设置"""
        self.ship_speed = 30
        self.bullet_speed = 10
        self.alien_speed = 10
        self.alien_drop_speed = 10
        self.alien_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """提高游戏速度设置"""
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale
        self.alien_drop_speed *= self.speed_scale
        self.alien_points = int(self.alien_points * self.score_scale)