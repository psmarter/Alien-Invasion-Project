import pygame.font
from pygame.sprite import Group
from ship import Ship

class GameScore:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont(None, self.game.settings.score_font)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分渲染为图像"""
        rounded_score = round(self.game.status.score, -1)
        score_str = f"{rounded_score:,}"  # 使用逗号分隔千位
        self.score_image = self.font.render(score_str, True, self.game.settings.score_text_color, self.game.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.game.screen.get_rect().right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.game.screen.blit(self.score_image, self.score_rect)
        self.game.screen.blit(self.high_score_image, self.high_score_rect)
        self.game.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.game.screen)

    def prep_high_score(self):
        """将最高得分渲染为图像"""
        high_score = round(self.game.status.max_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.game.settings.score_text_color, self.game.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.game.screen.get_rect().centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """检查是否达到了新的最高得分"""
        if self.game.status.score > self.game.status.max_score:
            self.game.status.max_score = self.game.status.score
            self.prep_high_score()

    def prep_level(self):
        """将当前关卡渲染为图像"""
        level_str = str(self.game.status.level)
        self.level_image = self.font.render(level_str, True, self.game.settings.score_text_color, self.game.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示剩余飞船数量"""
        self.ships = Group()
        for ship_number in range(self.game.status.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)