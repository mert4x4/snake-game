import pygame

screen_size = (640,480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("game")
clock = pygame.time.Clock()

running = True
gridlen = 20

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
        self.rects.append(Rectangle(self.x,self.y,(255,255,0)))
        self.rects.append(Rectangle(self.x-20,self.y,(255,255,0)))
        self.rects.append(Rectangle(self.x-40,self.y,(255,255,0)))
    def addRect(self):
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

        print(self.dir)
    def draw_snake(self,screen):
        for i in self.rects:
            i.draw_rect(screen)

class Food():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw_food(self,screen):
        food_rect = Rectangle(self.x*gridlen,self.y*gridlen,(0,100,255))
        food_rect.draw_rect(screen)

def draw_grid(screen):
    x_ = screen_size[0]/gridlen
    y_ = screen_size[1]/gridlen
    for x in range(0,int(x_)):
        for y in range(0,int(y_)):
            if (x+y) % 2 == 0:
                pygame.draw.rect(screen,(255,100,0),(x*gridlen,y*gridlen,gridlen,gridlen),0)
            else:
                pygame.draw.rect(screen,(200,100,0),(x*gridlen,y*gridlen,gridlen,gridlen),0)

def draw():
    screen.fill((255,255,255))
    draw_grid(screen)
    mert.draw_snake(screen)
    yemek.draw_food(screen)
    pygame.display.flip()

def input(event_type):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            mert.dir = "left"
        if event.key == pygame.K_RIGHT:
            mert.dir = "right" 
        if event.key == pygame.K_UP:
            mert.dir = "up"
        if event.key == pygame.K_DOWN:
            mert.dir = "down"

mert = Snake("right")
yemek = Food(20,20)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    input(event.type)
    mert.move()
    draw()
    clock.tick(10)
    
pygame.quit()

