import pygame
import random
import time

screen_size = (640,480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("game")
clock = pygame.time.Clock()

running = True
gridlen = 20

colors = {
  "snake_head": (244, 162, 97),
  "snake_body": (233, 196, 106),
  "grid_bright": (38, 72, 83),
  "grid_dark":(38, 70, 83),
  "food":(231,111,81),
}

class Rectangle():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.width = gridlen
        self.height = gridlen
        self.color = color
    def get_color(self):
        return self.color
    def get_pos(self):
        return self.x,self.y,self.height,self.width
    def draw_rect(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.height,self.width),0)

class Snake():
    def __init__(self,dir,len = 1):
        self.x = screen_size[0]/2
        self.y = screen_size[1]/2
        self.dir = dir
        self.len = len
        self.rects = []
        self.rects.append(Rectangle(self.x,self.y,colors["snake_head"]))
        self.rects.append(Rectangle(self.x,self.y,colors["snake_body"]))
        self.score = 0
        
    def addRect(self):
        self.rects.append(Rectangle(self.x,self.y,colors["snake_body"]))
        pass

    def move(self):
        for i in range(1,len(self.rects)):
            self.rects[len(self.rects)-i].x = self.rects[len(self.rects)-i-1].x
            self.rects[len(self.rects)-i].y = self.rects[len(self.rects)-i-1].y

        if self.dir == "right":
            self.rects[0].x += 1*gridlen
        if self.dir == "left":
            self.rects[0].x -= 1*gridlen
        if self.dir == "up":
            self.rects[0].y -= 1*gridlen
        if self.dir == "down":
            self.rects[0].y += 1*gridlen

        self.x = self.rects[0].x
        self.y = self.rects[0].y

    def draw(self,screen):
        for i in self.rects:
            i.draw_rect(screen)
    def self_collide(self):
        for i in self.rects[1:]:
            if self.x == i.x and self.y == i.y:
                return True
        return False

    def reset(self):
        self.x = screen_size[0]/2
        self.y = screen_size[1]/2
        self.dir = dir
        self.len = len
        self.rects = []
        self.rects.append(Rectangle(self.x,self.y,colors["snake_head"]))
        self.rects.append(Rectangle(self.x-gridlen,self.y,colors["snake_body"]))
        self.score = 0

class Food():
    def __init__(self,x,y):
        self.x = x*gridlen
        self.y = y*gridlen
    def draw(self,screen):
        food_rect = Rectangle(self.x,self.y,colors["food"])
        food_rect.draw_rect(screen)
    def teleport(self):
        self.x = random.randint(0,31)*gridlen
        self.y = random.randint(0,23)*gridlen

def checkPoint():
    if mert.x == food.x and mert.y == food.y:
        return True
    else:
        return False

def draw_grid(screen):
    x_ = screen_size[0]/gridlen
    y_ = screen_size[1]/gridlen
    for x in range(0,int(x_)):
        for y in range(0,int(y_)):
            if (x+y) % 2 == 0:
                pygame.draw.rect(screen,colors["grid_bright"],(x*gridlen,y*gridlen,gridlen,gridlen),0)
            else:
                pygame.draw.rect(screen,colors["grid_dark"],(x*gridlen,y*gridlen,gridlen,gridlen),0)

def draw():
    screen.fill((255,255,255))
    draw_grid(screen)
    mert.draw(screen)
    food.draw(screen)
    pygame.display.flip()

def edgeCollision():
    if mert.x > 620:
        mert.x = 0
        mert.rects[0].x = 0
    if mert.x < 0:
        mert.x = 620
        mert.rects[0].x = 620
    if mert.y < 0:
        mert.y = 460
        mert.rects[0].y = 460
    if mert.y > 460:
        mert.y = 0
        mert.rects[0].y = 0

def gameLogic():
    if(mert.self_collide()):
        reset()
    if(checkPoint()):
        mert.score += 1
        pygame.display.set_caption("score: "+str(mert.score))
        food.teleport()
        mert.addRect()
    edgeCollision()
    
def input(event_type):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and (mert.dir != "right"):
            mert.dir = "left"
        elif event.key == pygame.K_UP and (mert.dir != "down"):
            mert.dir = "up"
        elif event.key == pygame.K_RIGHT and (mert.dir != "left"):
            mert.dir = "right" 
        elif event.key == pygame.K_DOWN and (mert.dir != "up"):
            mert.dir = "down"

def reset():
    #score will set to zero
    #snake will shrink
    #snake will teleport to inital location
    #snake direction will be set to right
    food.teleport()
    mert.reset()
    pygame.display.set_caption("score: "+str(mert.score))

mert = Snake("right")
food = Food(20,20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        input(event.type)
    mert.move()
    draw()
    gameLogic()
    clock.tick(10)
    
pygame.quit()

