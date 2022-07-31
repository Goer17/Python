import pygame

pygame.init();

screen = pygame.display.set_mode((480,700));

bg = pygame.image.load("./images/background.png");
hero = pygame.image.load("./images/me1.png");

screen.blit(bg, (0, 0));
screen.blit(hero, (200, 500));

pygame.display.update();

input("按任意键继续...");

pygame.quit();