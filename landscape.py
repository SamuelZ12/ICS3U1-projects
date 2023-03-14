# Pygame Compund Shapes

from turtle import width
from venv import create
import pygame, math, random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
lightning_x = 0
lightning_y = 0
lightning_flag = True
skyRGB = [135, 206, 235]
sky_flag = True
cloudRGB = [255, 255, 255]
cloud_flag = True
clouds = []
count = 0
grassRGB = [0, 154, 23]
grass_flag = True
time = 0

def create_cloud(x, y):
    pygame.draw.circle(screen, tuple(cloudRGB), (x, y), 25)
    pygame.draw.circle(screen, tuple(cloudRGB), (x + 20, y + 5), 25)
    pygame.draw.circle(screen, tuple(cloudRGB), (x + 20, y - 15), 30)
    pygame.draw.circle(screen, tuple(cloudRGB), (x + 50, y - 10), 25)

def create_house(x, y):
    brick_red = (203, 65, 84)
    black = (0, 0, 0)
    pygame.draw.rect(screen, brick_red, (x, y, 100, 100))
    pygame.draw.rect(screen, black, (x, y, 100, 100), 3)
    pygame.draw.rect(screen, brick_red, (x+10, y-40, 25, 40))
    pygame.draw.rect(screen, black, (x+10, y-40, 25, 40), 3)
    pygame.draw.polygon(screen, brick_red, [[x, y], [x+100, y], [x+50, y-50]])
    pygame.draw.polygon(screen, black, [[x, y], [x+100, y], [x+50, y-50]], 3)
    pygame.draw.rect(screen, (255,248,220), (x+30, y+30, 40, 70))
    pygame.draw.rect(screen, black, (x+30, y+30, 40, 70), 3)

def create_lightning(x, y):
    yellow = (253, 208, 35)
    pygame.draw.polygon(screen, yellow, [[x, y], [x+20, y-75], [x-40, y]])
    pygame.draw.polygon(screen, yellow, [[x-20, y], [x+20, y], [x-40, y+75]])

def create_setting(x, y):
    screen.fill(tuple(skyRGB))
    pygame.draw.rect(screen, tuple(grassRGB), (x, y, WIDTH, 80))
    pygame.draw.polygon(screen, (220,220,220), [[x+WIDTH/2-50, y], [x+WIDTH/2+50, y], [x+WIDTH/2+100, HEIGHT], [x+WIDTH/2-100, HEIGHT]])
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)

    time += 1
    if time > 60:
        # nightRGB (12, 20, 69)
        if 12 < skyRGB[0] and sky_flag:
            skyRGB[0] -= 1.23
            skyRGB[1] -= 1.86
            skyRGB[2] -= 1.66
        else:
            sky_flag = False
        if 99 < grassRGB[1] and grass_flag:
            grassRGB[0] += 0.6
            grassRGB[1] -= 0.54
            grassRGB[2] -= 0.23
        else:
            grass_flag = False
        # nightRGB (83,83,83)
        if 83 < cloudRGB[0] and cloud_flag:
            for i in range(3):
                cloudRGB[i] -= 1.72
        else:
            cloud_flag = False
        for cloud in clouds:
            if cloud[2] == 1:
                cloud[0] += 5
            else: 
                cloud[0] -= 5
            if cloud[0] >= WIDTH:
                cloud[2] = 0
            elif cloud[0] <= 0:
                cloud[2] = 1
        count += 1
        if count == 30 and len(clouds) < 20:
            clouds.append([random.randrange(WIDTH), random.randrange(150), random.randrange(2)])
            count = 0

        if lightning_x == WIDTH:
            lightning_flag = False
        elif lightning_x == 0:
            lightning_flag = True

        if lightning_flag: 
            lightning_x += 10
        else: 
            lightning_x -= 10
    
    # DRAW
    create_setting(0, 400)
    for cloud in clouds:
        create_cloud(cloud[0], cloud[1])
    create_house(WIDTH//2-50, 300)
    lightning_y = HEIGHT/2*math.sin(lightning_x)+HEIGHT/2
    if random.randrange(30) == 0 and (not cloud_flag and not sky_flag):
        screen.fill((0, 0, 0))
        create_lightning(lightning_x, lightning_y)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30) # FPS
    #---------------------------


pygame.quit()