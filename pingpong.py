#create a Maze game!

from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y -= self.speed
        

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        
        if self.direction == "left" :
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed





class Wall(sprite.Sprite):
    def __init__ (self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))    

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y 

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")

background = transform.scale(image.load("background.jpg"),(win_width, win_height))

fps = 60
clock = time.Clock()

hero = GameSprite("hero.png", 5, win_height - 80, 5)
cyborg = GameSprite("cyborg.png", 5, win_width - 100, 5)
treasure = GameSprite("treasure.png", win_width - 120, win_height - 120, 0)


mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()



Wall1 = Wall(192,197,20,70,250,30,300)
Wall2 = Wall(192,197,20,120,285,30,300)
Wall3 = Wall(192,192,20,100,300,30,300)
Wall4 = Wall(192,192,20,100,300,30,300)
Wall5 = Wall(192,192,20,100,300,30,300)


game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))

    if mouse.get_pressed()[0] == 1:
        print(mouse.get_pos())

    hero.reset()
    cyborg.reset()
    Wall1.draw_wall()
    display.update()
    clock.tick(fps)

