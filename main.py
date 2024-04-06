import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Создаём прямоугольник
rect = pygame.Rect(100, 100, 50, 50)

# Отрисовываем прямоугольник
pygame.draw.rect(screen, (255, 0, 0), rect)

pygame.display.flip()

# Ждём закрытия окна
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
