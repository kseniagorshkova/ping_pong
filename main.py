from pygame import *
init()

W = 800
H = 500

window = display.set_mode((W,H))
bg = transform.scale(image.load('bg.jpg'), (W, H))
clock = time.Clock()#лічильник кадрів

class GameSprite(sprite.Sprite):# базовий клас для всіх спрайтів
   def __init__(self, img, x, y, width, height, speed_x, speed_y):# конструткор класу
       super().__init__()
       self.image = transform.scale(image.load(img), (width, height))
       self.rect = self.image.get_rect()# автоматичне створення хіт боксу
       self.rect.x = x
       self.rect.y = y
       self.speed_x = speed_x
       self.speed_y = speed_y
       self.width = width
       self.height = height
  
   def draw(self):# малювання картинки
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_s] and self.rect.y < H - self.height:
            self.rect.y += self.speed_y
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y < H - self.height:
            self.rect.y += self.speed_y
player1 = Player('racket.png',5 ,5, 50, 130, 10, 10)
player2 = Player('racket.png',750 ,250, 50, 130, 10, 10)

game = True
while game:
    window.blit(bg, (0 , 0))
    player1.draw()
    player2.draw()

    player1.update_l()
    player2.update_r()
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(100)
    display.update()