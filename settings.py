class Settings:
    """
    游戏设置类 - 存储游戏的所有设置
    Settings class - Stores all settings for the game
    """
    def __init__(self):
        """
        初始化游戏的静态设置 | Initialize game's static settings
        这些设置在游戏运行期间不会改变 | These settings don't change during gameplay
        """
        # 屏幕设置 | Screen settings
        self.screen_width = 1600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.FPS = 90
        self.TITLE = "外星人来喽"

        # 飞船设置 | Ship settings
        self.ship_image_path = 'imgs/ship.bmp'
        self.ship_speed = 30
        self.ship_limit = 2  # 玩家拥有的飞船数量 | Number of ships player has

        # 子弹设置 | Bullet settings
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 10
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_limit = 10  # 屏幕上允许同时存在的子弹数 | Max bullets allowed on screen

        # 外星人设置 | Alien settings
        self.alien_speed = 10
        self.alien_drop_speed = 10  # 外星人向下移动的速度 | Speed aliens drop down
        self.alien_direction = 1  # 1表示向右移动，-1表示向左移动 | 1=right, -1=left

        # 按钮设置 | Button settings
        self.button_color = (0, 255, 0)
        self.button_width = 200
        self.button_height = 50
        self.button_text_color = (255, 255, 255)
        self.button_font = 48
        self.play_button_text = "Play"

        # 游戏速度设置 | Game speed settings
        self.speed_scale = 1.1  # 每关难度提升比例 | Difficulty increase per level
        self.init_settings()

        # 游戏分数设置 | Score settings
        self.score_text_color = (30, 30, 30)
        self.score_font = 48
        self.score_scale = 1.5  # 每关分数提升比例 | Score increase per level

    def init_settings(self):
        """
        初始化游戏的动态设置 | Initialize dynamic game settings
        这些设置会随着游戏进行而改变 | These settings change as game progresses
        """
        self.ship_speed = 30
        self.bullet_speed = 10
        self.alien_speed = 10
        self.alien_drop_speed = 10
        self.alien_direction = 1
        self.alien_points = 50  # 击毁一个外星人的分数 | Points for destroying one alien

    def increase_speed(self):
        """
        提高游戏速度设置 | Increase game speed
        每通过一关调用一次 | Called once per level completion
        """
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale
        self.alien_drop_speed *= self.speed_scale
        self.alien_points = int(self.alien_points * self.score_scale)