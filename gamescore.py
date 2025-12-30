import pygame.font
from pygame.sprite import Group
from ship import Ship

class GameScore:
    """
    游戏计分板类 - 显示得分、最高分、关卡和剩余飞船
    GameScore class - Displays score, high score, level, and remaining ships
    """
    def __init__(self, game):
        """初始化计分属性 | Initialize scoring attributes"""
        self.game = game
        self.font = pygame.font.SysFont(None, self.game.settings.score_font)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """
        将得分渲染为图像 | Render score as an image
        将得分转换为易读的格式并渲染 | Convert score to readable format and render
        """
        rounded_score = round(self.game.status.score, -1)
        score_str = f"{rounded_score:,}"  # 使用逗号分隔千位 | Use comma to separate thousands
        self.score_image = self.font.render(score_str, True, self.game.settings.score_text_color, self.game.settings.bg_color)

        # 将得分放在屏幕右上角 | Position score at top-right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.game.screen.get_rect().right - 20
        self.score_rect.top = 20

    def show_score(self):
        """
        在屏幕上显示得分 | Display score on screen
        绘制所有计分板元素 | Draw all scoreboard elements
        """
        self.game.screen.blit(self.score_image, self.score_rect)
        self.game.screen.blit(self.high_score_image, self.high_score_rect)
        self.game.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.game.screen)

    def prep_high_score(self):
        """
        将最高得分渲染为图像 | Render high score as an image
        显示历史最高分 | Display all-time high score
        """
        high_score = round(self.game.status.max_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.game.settings.score_text_color, self.game.settings.bg_color)

        # 将最高分放在屏幕顶部中央 | Position high score at top-center of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.game.screen.get_rect().centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """
        检查是否达到了新的最高得分 | Check if new high score is reached
        更新最高分记录 | Update high score record
        """
        if self.game.status.score > self.game.status.max_score:
            self.game.status.max_score = self.game.status.score
            self.prep_high_score()

    def prep_level(self):
        """
        将当前关卡渲染为图像 | Render current level as an image
        显示玩家所在的关卡 | Display current game level
        """
        level_str = str(self.game.status.level)
        self.level_image = self.font.render(level_str, True, self.game.settings.score_text_color, self.game.settings.bg_color)

        # 将关卡显示在得分下方 | Position level below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """
        显示剩余飞船数量 | Display number of ships left
        绘制小飞船图标表示剩余生命 | Draw small ship icons to represent remaining lives
        """
        self.ships = Group()
        for ship_number in range(self.game.status.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
