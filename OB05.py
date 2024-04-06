import random

import pygame
import sys

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
def rand_c():
    return (random.randint(1, 255),random.randint(1,255),random.randint(1,255) )

color_ball = white
#print(rand_c())

size = width, height = 800, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Одиночный Пинг-Понг")

# Ракетка
paddle_width, paddle_height = 10, 60
paddle_speed = 10
paddle = pygame.Rect(20, height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Мяч
ball_size = 20
ball_speed = [3, 3]
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)


def reset_ball():
    pygame.time.delay(200)
    ball.center = (width // 2, height // 2)
    ball_speed[0] = random.randint(2,6)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle.top > 0:
        paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN] and paddle.bottom < height:
        paddle.move_ip(0, paddle_speed)

    ball.move_ip(ball_speed)

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] = -ball_speed[1]

    if ball.right >= width:
        ball_speed[0] = -ball_speed[0]

    if ball.colliderect(paddle):
        ball_speed[0] = -ball_speed[0]

    if ball.left <= -100:
        reset_ball()
        color_ball = rand_c()

    screen.fill(black)
    pygame.draw.rect(screen, white, paddle)  # Ракетка
    pygame.draw.ellipse(screen, color_ball, ball)  # Мяч

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
sys.exit()