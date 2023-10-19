from pygame import *
from random import randint
from assets_table import sprites

win_width, win_height = 800, 600
window = display.set_mode((win_width, win_height))


def MakeImage(img, w, h):
    return transform.scale(
        image.load(img),
        (w, h)
    )


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()

        self.speed = speed
        self.width = w
        self.height = h

        self.image = transform.scale(
            image.load(img),
            (w, h)
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    kills, losts = 0, 0
    bullets = sprite.Group()

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            if self.rect.x > 5:
                self.rect.x -= self.speed
        if keys[K_RIGHT] or keys[K_d]:
            if self.rect.x < win_width - self.width:
                self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(sprites["BULLET"],
                        self.rect.centerx - 7.5, self.rect.top, 15, 15, 10)
        self.bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        global losts
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(self.width, win_width - self.width)
            self.rect.y = 0
            Player.losts += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
