import pygame
import random
import math
import time

pygame.init()

tlo = pygame.image.load('tlo.png')
heart = pygame.image.load('heart.png')
# gracz
playerImg = pygame.image.load('player.png')
playerX = 100
playerY = 450
playerY_move = 0
playerX_move = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_move = []
enemyY_move = []
fire = []
num_of_enemies = 12
ile = 1
plus = True
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(1210, 1400))
    enemyY.append(random.randint(20, 1100))
    enemyX_move.append(random.random() + random.randint(1, 2))
    fire.append(False)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def live(n):
    for i in range(n):
        x = 100 + (i * 115)
        screen.blit(heart, (x, 20))


# stworzenie ekranu
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("ROAD")

# przegrana
lose = False
start = False
lives = 3
end_font = pygame.font.Font('BabyDoll.ttf', 124)
note_font = pygame.font.Font('BabyDoll.ttf', 32)
won = False

def game_over_text():
    end_text = end_font.render("GAME OVER", True, (0, 0, 0))
    note_text = note_font.render("PRESS SPACE TO REPLAY", True, (0, 0, 0))
    screen.blit(end_text, (300, 400))
    screen.blit(note_text, (465, 750))


def won_text():
    won_text = end_font.render("YOU WON!", True, (0, 0, 0))
    note_text = note_font.render("PRESS SPACE TO REPLAY", True, (0, 0, 0))
    screen.blit(won_text, (300, 400))
    screen.blit(note_text, (465, 750))


def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((playerX - enemyX) ** 2 + (playerY - enemyY) ** 2)
    if distance < 45:
        return True


def start_():
    for i in range(3,-1,-1):
        screen.blit(tlo, (0, 0))
        player(playerX, playerY)
        time_text = end_font.render(str(i), True, (0, 0, 0))
        screen.blit(time_text, (550, 400))
        pygame.display.update()
        time.sleep(1)
    return True


def reset():
    for i in range(num_of_enemies):
        enemyX[i] = random.randint(1210, 1400)
        enemyY[i] = random.randint(20, 1100)
        enemyX_move[i] = random.random() + random.randint(1, 2)
        fire[i] = False


running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(tlo, (0, 0))
    # wychodzenie z gry
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # sterowanie
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_move -= 3
            if event.key == pygame.K_DOWN:
                playerY_move += 3
            if event.key == pygame.K_LEFT:
                playerX_move -= 3
            if event.key == pygame.K_RIGHT:
                playerX_move += 3
            if event.key == pygame.K_SPACE and (lose or won):
                lose = False
                ile = 1
                lives = 3
                reset()
                start=False

        if event.type == pygame.KEYUP:
            playerY_move = 0
            playerX_move = 0

    playerX += playerX_move
    playerY += playerY_move
    if playerY >= 800:
        playerY = 800
    elif playerY <= 0:
        playerY = 0
    if playerX >= 300:
        playerX = 300
    elif playerX <= 100:
        playerX = 100
    if not lose:
        for j in range(ile):
            enemyX[j] -= enemyX_move[j]
            if not fire[j]:
                enemyY[j] = playerY
                fire[j] = True
            enemy(enemyX[j], enemyY[j], j)
            collision = isCollision(enemyX[j], enemyY[j], playerX, playerY)
            if collision:
                lives -= 1
                print("trafiony")
                enemyX[j] = (-50)
                enemyY[j] = random.randint(40, 1050)
                if lives == 0:
                    lose = True
        for n in range(ile):
            if enemyX[n] > -35:
                plus = False
                break
            else:
                plus = True
        if plus and ile < num_of_enemies:
            ile = ile + 1
            print(ile)
            for n in range(ile - 1):
                enemyX[n] = random.randint(1200, 1399)
    if lose:
        game_over_text()
    if ile == 12 and plus:
        won_text()
        won = True
    live(lives)
    player(playerX, playerY)
    if not start:
        start = start_()
    pygame.display.update()
