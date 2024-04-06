import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создаем поверхность для мяча
size = width, height = 20, 20  # Размеры изображения
ball_surface = pygame.Surface(size, pygame.SRCALPHA)  # Создаем поверхность с поддержкой прозрачности

# Цвета
white = (255, 255, 255, 255)  # RGBA для белого цвета

# Рисуем мяч
pygame.draw.circle(ball_surface, white, (width // 2, height // 2), 10)

# Сохраняем поверхность в файл
pygame.image.save(ball_surface, "ball.png")

# Завершаем работу Pygame
pygame.quit()
sys.exit()
