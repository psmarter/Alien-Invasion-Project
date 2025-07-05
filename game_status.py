class GameStatus:
    def __init__(self, game):
        """初始化游戏状态"""
        self.ships_left = None
        self.game = game
        self.reset_status()
        
    def reset_status(self):
        """重置游戏状态"""
        self.ships_left = self.game.settings.ship_limit
