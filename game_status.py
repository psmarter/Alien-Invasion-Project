class GameStatus:
    def __init__(self, game):
        """初始化游戏状态"""
        self.ships_left = None
        self.game = game
        self.reset_status()
        self.max_score = 0
        
    def reset_status(self):
        """重置游戏状态"""
        self.ships_left = self.game.settings.ship_limit
        self.score = 0
        self.level = 1
