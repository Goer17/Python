import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700);
CREATE_ENEMY_EVENT = pygame.USEREVENT;

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed = 1):
        
        # 调用父类初始化方法
        super().__init__();

        # 定义对象属性
        self.image = pygame.image.load(image_name);
        self.rect = self.image.get_rect();
        self.speed = speed;

    def update(self):

        # 在屏幕的垂直方向移动
        self.rect.y += self.speed;

class Background(GameSprite):
    """游戏背景类"""

    def __init__(self, is_alt = False):

        super().__init__("./images/background.png");

        if is_alt:
            self.rect.y = -self.rect.height;

    def update(self):
        
        super().update();

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height;

class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        super().__init__("./images/enemy1.png");

        self.speed = random.randint(1, 3);
        self.rect.y = -self.rect.height;
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width);

    def update(self):

        super().update();
        if self.rect.y >= SCREEN_RECT.height:
            
            self.kill();