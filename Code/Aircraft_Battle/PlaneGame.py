import pygame
from plane_sprite import *

FREQUENCY = 60;

class PlaneGame(object):

    def __init__(self):
        print("游戏初始化...");

        self.screen = pygame.display.set_mode(SCREEN_RECT.size);
        self.timer = pygame.time.Clock();
        self.__create_sprites();
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000);

    def __create_sprites(self):

        bg_1 = Background();
        bg_2 = Background(is_alt = True);

        self.back_group = pygame.sprite.Group(bg_1, bg_2);
        self.enemy_group = pygame.sprite.Group();

    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                PlaneGame.__game_over();

            elif event.type == CREATE_ENEMY_EVENT:

                enemy = Enemy();
                self.enemy_group.add(enemy);

    def __check_collide(self):
        pass;
    
    def __update_sprites(self):

        self.back_group.update();
        self.back_group.draw(self.screen);
        self.enemy_group.update();
        self.enemy_group.draw(self.screen);


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
            pygame.display.update();