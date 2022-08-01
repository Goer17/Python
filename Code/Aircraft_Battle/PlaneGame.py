import pygame
from plane_sprite import *

SCREEN_RECT = pygame.Rect(0, 0, 480, 700);
FREQUENCY = 60;

class PlaneGame(object):

    def __init__(self):
        print("游戏初始化...");

        self.screen = pygame.display.set_mode(SCREEN_RECT.size);
        self.bg = pygame.image.load("./images/background.png");
        self.timer = pygame.time.Clock();

    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over();
            pass;

    def __check_collide(self):
        pass;
    
    def __update_sprites(self):
        pass;

    @staticmethod
    def __game_over():
        print("游戏结束...");

        pygame.quit();
        exit();

    def play(self):
        print("游戏开始...");

        pygame.init();

        while True:
            # 按照固定帧率刷新
            self.timer.tick(FREQUENCY);

            # 事件监听
            self.__event_handler();

            # 碰撞检测
            self.__check_collide();

            # 更新精灵组
            self.__update_sprites();

            # 更新绘图
            self.screen.blit(self.bg, (0, 0));
            pygame.display.update();