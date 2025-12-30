class GameStatus:
    """
    游戏状态类 - 跟踪游戏的统计信息
    GameStatus class - Tracks game statistics
    """
    def __init__(self, game):
        """
        初始化游戏状态 | Initialize game statistics
        包括剩余飞船数、分数、关卡等 | Includes ships left, score, level, etc.
        """
        self.ships_left = None
        self.game = game
        self.reset_status()
        # 最高分数 | High score tracking
        self.max_score = 0
        
    def reset_status(self):
        """
        重置游戏状态 | Reset game statistics
        在游戏开始时重置所有动态统计数据 | Reset all dynamic stats at game start
        """
        self.ships_left = self.game.settings.ship_limit
        self.score = 0
        self.level = 1
