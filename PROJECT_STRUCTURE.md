# Alien Invasion Project Structure | 项目结构

This document explains the structure and organization of the Alien Invasion game project.

## 📂 File Organization | 文件组织

```
Alien-Invasion-Project/
│
├── alien_invasion.py    # Main game file | 主游戏文件
│   └── AlienInvasion class - Main game controller
│       管理游戏资源和行为的总类
│
├── ship.py              # Player ship module | 玩家飞船模块
│   └── Ship class - Player-controlled spaceship
│       管理玩家飞船的移动和绘制
│
├── alien.py             # Enemy alien module | 外星敌人模块
│   └── Alien class - Enemy spaceships
│       管理外星人的移动和边缘检测
│
├── bullet.py            # Projectile module | 子弹模块
│   └── Bullet class - Bullets fired by the ship
│       管理飞船发射的子弹
│
├── button.py            # UI button module | UI按钮模块
│   └── Button class - Game UI buttons
│       创建和管理游戏界面按钮
│
├── settings.py          # Game configuration | 游戏配置
│   └── Settings class - All game settings
│       存储所有游戏设置和参数
│
├── game_status.py       # Game state module | 游戏状态模块
│   └── GameStatus class - Tracks game statistics
│       跟踪游戏统计信息（生命、分数、关卡）
│
├── gamescore.py         # Scoreboard module | 计分板模块
│   └── GameScore class - Displays scoring information
│       显示得分、最高分、关卡和剩余生命
│
├── imgs/                # Image assets | 图像资源
│   ├── ship.bmp        # Player ship sprite | 玩家飞船精灵
│   └── alien.bmp       # Alien enemy sprite | 外星敌人精灵
│
├── README.md            # Project documentation | 项目文档
├── CONTRIBUTING.md      # Contribution guidelines | 贡献指南
├── LICENSE              # MIT License | MIT许可证
├── requirements.txt     # Python dependencies | Python依赖
└── .gitignore          # Git ignore rules | Git忽略规则
```

## 🔄 Game Flow | 游戏流程

### 1. Initialization | 初始化

```
AlienInvasion.__init__()
├── Initialize Pygame
├── Create Settings
├── Create Screen
├── Create Game Objects
│   ├── Ship
│   ├── Bullets (Group)
│   ├── Aliens (Fleet)
│   ├── GameStatus
│   ├── GameScore
│   └── Play Button
└── Start Main Loop
```

### 2. Main Game Loop | 主游戏循环

```
run_game()
├── Check Events
│   ├── Keyboard Input
│   └── Mouse Click
├── Update Game Objects (if active)
│   ├── Ship Position
│   ├── Bullet Positions
│   └── Alien Positions
└── Render Screen
    ├── Draw Background
    ├── Draw Bullets
    ├── Draw Ship
    ├── Draw Aliens
    ├── Draw Scoreboard
    └── Draw Button (if inactive)
```

### 3. Collision Detection | 碰撞检测

```
Collision Checks:
├── Bullet-Alien Collisions
│   ├── Remove hit aliens
│   ├── Award points
│   └── Check for fleet destruction
├── Ship-Alien Collisions
│   ├── Decrease lives
│   ├── Reset positions
│   └── Check game over
└── Alien-Bottom Collisions
    └── Treat as ship hit
```

## 🎯 Key Classes | 核心类

### AlienInvasion

**Purpose**: Main game controller  
**用途**: 主游戏控制器

**Key Methods**:

- `run_game()` - Main game loop | 主游戏循环
- `_check_events()` - Event handling | 事件处理
- `_update_screen()` - Render graphics | 渲染图形
- `_create_fleet()` - Create alien fleet | 创建外星人舰队
- `_ship_hit()` - Handle ship collision | 处理飞船碰撞

### Ship

**Purpose**: Player's spaceship  
**用途**: 玩家的飞船

**Key Methods**:

- `update()` - Move ship | 移动飞船
- `draw()` - Render ship | 绘制飞船
- `center_ship()` - Reset position | 重置位置

### Alien

**Purpose**: Enemy spaceship  
**用途**: 敌人飞船

**Key Methods**:

- `update()` - Move alien | 移动外星人
- `check_edges()` - Detect screen edges | 检测屏幕边缘

### Bullet

**Purpose**: Projectile fired by ship  
**用途**: 飞船发射的子弹

**Key Methods**:

- `update()` - Move bullet upward | 向上移动子弹
- `draw()` - Render bullet | 绘制子弹

### Settings

**Purpose**: Game configuration  
**用途**: 游戏配置

**Key Methods**:

- `init_settings()` - Reset dynamic settings | 重置动态设置
- `increase_speed()` - Increase difficulty | 提升难度

### GameStatus

**Purpose**: Track game statistics  
**用途**: 跟踪游戏统计

**Attributes**:

- `ships_left` - Remaining lives | 剩余生命
- `score` - Current score | 当前分数
- `level` - Current level | 当前关卡
- `max_score` - High score | 最高分

### GameScore

**Purpose**: Display scoreboard  
**用途**: 显示计分板

**Key Methods**:

- `prep_score()` - Render score | 渲染分数
- `prep_high_score()` - Render high score | 渲染最高分
- `prep_level()` - Render level | 渲染关卡
- `prep_ships()` - Render remaining lives | 渲染剩余生命

## 🎮 Game Mechanics | 游戏机制

### Difficulty Progression | 难度递增

- Speed increases by 10% per level | 每关速度提升10%
- Alien points increase by 150% per level | 每关分数提升150%
- Fleet descends faster each level | 外星人每关下降更快

### Scoring System | 计分系统

- Base points per alien: 50 | 每个外星人基础分: 50
- Points scale with level | 分数随关卡递增
- High score tracking | 最高分追踪
- Score display formatting (comma separators) | 分数格式化显示

### Lives System | 生命系统

- Start with 2 ships | 开局2条生命
- Lose life when hit by alien | 被外星人撞击时失去生命
- Lose life when aliens reach bottom | 外星人到达底部时失去生命
- Game over when no ships remain | 无生命时游戏结束

## 🔧 Configuration | 配置

All game parameters can be adjusted in `settings.py`:

### Screen Settings | 屏幕设置

- Width: 1600px
- Height: 600px  
- FPS: 90

### Ship Settings | 飞船设置

- Speed: 30 (increases with levels)
- Lives: 2

### Bullet Settings | 子弹设置

- Speed: 10 (increases with levels)
- Limit: 10 simultaneous bullets
- Color: Dark gray (60, 60, 60)

### Alien Settings | 外星人设置

- Speed: 10 (increases with levels)
- Drop speed: 10 (increases with levels)
- Points: 50 (increases with levels)

## 📝 Code Style | 代码风格

All Python files follow these conventions:

1. **Bilingual Comments** | 双语注释
   - Chinese followed by English
   - Format: `# 中文说明 | English explanation`

2. **Docstrings** | 文档字符串
   - Class docstrings explain purpose
   - Method docstrings explain behavior
   - Bilingual where appropriate

3. **PEP 8 Compliance** | PEP 8 规范
   - 4-space indentation
   - Descriptive variable names
   - Proper spacing

## 🚀 Getting Started | 开始使用

1. **Install Python 3.7+**
2. **Install Pygame**: `pip install -r requirements.txt`
3. **Run Game**: `python alien_invasion.py`
4. **Play**: Click "Play" button to start

## 🤝 Contributing | 参与贡献

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

---

**Created with ❤️ for the Python gaming community**  
**为Python游戏社区用心打造**
