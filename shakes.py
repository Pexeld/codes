import pygame
from threading import Thread
from random import randrange


res = 720
size = 20
x, y = randrange(0, res, size), randrange(0, res, size)
apple = randrange(0, res, size), randrange(0, res, size)
dirs = {'W': True,
    'S': True,
    'A': True,
    'D': True,}

lenght = 1
score = 0
snake = [(x, y)]
dx, dy = 0, 0
fps = 10

pygame.init()
sc = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold = True)

def loose(a):
    if a == 1:
        exit()
    if a == 2:
        exit()

while True:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, size, size))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, size, size))
    render_score = font_score.render(f'Score: {score}' , 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))
    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-lenght:]


    if snake[-1] == apple:
        apple = randrange(0, res, size), randrange(0, res, size)
        lenght += 1
        score += 1
        # fps += 1
    if x < 0 or x > res - size or y < 0 or y > res - size:
        loose(1)
    # if len(snake) != len(set(snake)):
    #     loose(2)

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1
    if key[pygame.K_s]:
        dx, dy = 0, 1
    if key[pygame.K_a]:
        dx, dy = -1, 0
    if key[pygame.K_d]:
        dx, dy = 1, 0
    # key = pygame.key.get_pressed()
    # if key[pygame.K_w] and dirs['W']:
    #     dx, dy = 0, -1
    #     dirs['S'] = False
    # if key[pygame.K_s] and dirs['S']:
    #     dx, dy = 0, 1
    #     dirs['W'] = False
    # if key[pygame.K_a] and dirs['A']:
    #     dx, dy = -1, 0
    #     dirs['D'] = False
    # if key[pygame.K_d] and dirs['D']:
    #     dx, dy = 1, 0
    #     dirs['A'] = False
