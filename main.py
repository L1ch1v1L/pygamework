import pygame
import sys
import random


pygame.init()

window_size = (640, 480)
PLAYERCOLOR1 = [0,0,0]
PLAYERCOLOR2 = [1,1,1]
enemynumber = 10



def score():
    score1, score2, score3, score4 = score_manager.get_scores()
    print(f"WHITE PLAYER: {score1}")
    print(f"BLUE PLAYER: {score2}")
    print(f"RED PLAYER: {score3}")
    print(f"BLACK52 PLAYER: {score4}")

screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("ИГРА СМЕШНАЯ")

bullets = []
enemies = []
bosses = []


class ScoreManager:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.score4 = 0

    def increment_score(self, color):
        if color == (255, 255, 255):
            self.score1 += 1
        elif color == (0, 0, 255):
            self.score2 += 1
        elif color == (255, 0, 0):
            self.score3 += 1
        elif color == (0, 0, 0):
            self.score4 += 1
    def boss_score(self, color):
        if color == (255, 255, 255):
            self.score1 += 25
        elif color == (0, 0, 255):
            self.score2 += 25
        elif color == (255, 0, 0):
            self.score3 += 25
        elif color == (0, 0, 0):
            self.score4 += 25
    def set_text(self):
        font = pygame.font.SysFont('Arial',30)
        text = f"W:{self.score1} B:{self.score2} R:{self.score3} B:{self.score4}"
        text_surface = font.render(text, True,(255,255,255))
        screen.blit(text_surface,(10,10))
    def get_scores(self):
        return self.score1, self.score2, self.score3, self.score4

score_manager = ScoreManager()

class Boss(pygame.Rect):
    def __init__(self, x):
        super().__init__(x, 0, 60, 60)
        self.health = 15
        self.speed = 0.5
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color_change_time = pygame.time.get_ticks()

    def move(self):
        self.y += self.speed
        if self.y >= 420:
            score()
            pygame.quit()
            sys.exit()
            

    def draw(self, screen):
        current_time = pygame.time.get_ticks()
        if current_time - self.color_change_time > 100:  # изменять цвет каждые 100 мс
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.color_change_time = current_time
        pygame.draw.rect(screen,self.color,self)


class Enemy(pygame.Rect):
    def __init__(self, x):
        super().__init__(x, 0, 25, 25)
        self.speed = 1
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color_change_time = pygame.time.get_ticks()

    def move(self):
        self.y += self.speed
        if self.y >= 420:
            score()
            pygame.quit()
            sys.exit()
            

    def draw(self, screen):
        current_time = pygame.time.get_ticks()
        if current_time - self.color_change_time > 100:  # изменять цвет каждые 100 мс
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.color_change_time = current_time
        pygame.draw.rect(screen,self.color,self)
    

class Bullet(pygame.Rect):
    def __init__(self, x, y, color):
        super().__init__(x, y, 15, 10)
        self.color = color
        self.speed = 10
        self.to_remove = False

    def move(self):
        self.y -= self.speed
        for i in range(len(enemies)):
            if self.colliderect(enemies[i]):
                score_manager.increment_score(self.color)
                score_manager.set_text()
                enemies.pop(i)
                self.to_remove = True
                break
        for i in range(len(bosses)):
            if self.colliderect(bosses[i]):
                bosses[i].health -= 1
                self.to_remove = True
                if bosses[i].health == 0:
                    score_manager.boss_score(self.color)
                    score_manager.set_text()
                    bosses.pop(i)
                break

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)  


class Player1(pygame.Rect):
    def __init__(self):
        super().__init__(100, 400, 25, 25) 
        self.speed = 10
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_4]:
            if self.x >= 0:
                self.x -= self.speed
        if keys[pygame.K_KP_6]:
            if self.x <= window_size[0]-25:
                self.x += self.speed
        for i in range(len(enemies)):
            if self.colliderect(enemies[i]):
                score()
                pygame.quit()
                sys.exit()
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), self)

class Player2(pygame.Rect):
    def __init__(self):
        super().__init__(100, 400, 25, 25) 
        self.speed = 10
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.x >= 0:
                self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            if self.x <= window_size[0]-25:
                self.x += self.speed
        for i in range(len(enemies)):
            if self.colliderect(enemies[i]):
                score()
                pygame.quit()
                sys.exit()
    def draw(self, screen):
        pygame.draw.rect(screen,(0,0,255), self) 

class Player3(pygame.Rect):
    def __init__(self):
        super().__init__(100, 400, 25, 25) 
        self.speed = 10
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            if self.x >= 0:
                self.x -= self.speed
        if keys[pygame.K_l]:
            if self.x <= window_size[0]-25:
                self.x += self.speed
        for i in range(len(enemies)):
            if self.colliderect(enemies[i]):
                score()
                pygame.quit()
                sys.exit()

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self) 

class Player4(pygame.Rect):
    def __init__(self):
        super().__init__(100, 400, 25, 25) 
        self.speed = 10
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if self.x >= 0:
                self.x -= self.speed
        if keys[pygame.K_d]:
            if self.x <= window_size[0]-25:
                self.x += self.speed
        for i in range(len(enemies)):
            if self.colliderect(enemies[i]):
                score()
                pygame.quit()
                sys.exit()
                
    def draw(self, screen):
      pygame.draw.rect(screen, PLAYERCOLOR1, self) 



player = Player1()
player2 = Player2()
player3 = Player3()
player4 = Player4()
FPS = 60
image = pygame.image.load('background.jfif')
image = pygame.transform.scale(image, (640, 480))

def spawnEnemy():
    if len(enemies) < enemynumber:
        enemy = Enemy(random.randint(0,640))
        enemies.append(enemy)
    for i in enemies:
        i.move()
        i.draw(screen)

def spawnBoss():
    if len(bosses) < 1:
        boss = Boss(random.randint(0,640))
        bosses.append(boss)
    for i in bosses:
        i.move()
        i.draw(screen)

clock = pygame.time.Clock()

def spawnbullet1(): 
    bullet = Bullet(player.centerx, player.top, color=(255,255,255))
    bullets.append(bullet)
def spawnbullet2(): 
    bullet = Bullet(player2.centerx, player2.top, color=(0,0,255))
    bullets.append(bullet)
def spawnbullet3(): 
    bullet = Bullet(player3.centerx, player3.top, color=(255,0,0))
    bullets.append(bullet)
def spawnbullet4(): 
    bullet = Bullet(player4.centerx, player4.top, color=(0,0,0))
    bullets.append(bullet)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    if event.button == 1:
        #        spawnbullet1()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_8:
                spawnbullet1()
            if event.key == pygame.K_UP:
                spawnbullet2()
            if event.key == pygame.K_i:
                spawnbullet3()
            if event.key == pygame.K_w:
                spawnbullet4()
    screen.blit(image, (0, 0))
    player.move()
    player2.move()
    player3.move()
    player4.move()
    to_remove = []
    for bullet in bullets:
        bullet.move()
        if bullet.y < 0 or bullet.to_remove:
            to_remove.append(bullet)

    for bullet in to_remove:
        bullets.remove(bullet)
    for bullet in bullets:
        bullet.move()
        bullet.draw(screen)
        if bullet.y < 0:
            bullets.remove(bullet)
    spawnEnemy()
    spawnBoss()
    score_manager.set_text()
    player.draw(screen)
    player2.draw(screen)
    player3.draw(screen)
    player4.draw(screen)

    
    pygame.display.flip()
    clock.tick(FPS)
