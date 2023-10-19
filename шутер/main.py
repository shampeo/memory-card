from pygame import *
from assets_table import *
from classes import *
from langs import *

lang = "UKR"
need_to_win = 10
need_to_lose = 10



game_run, game_finish = True, False

display.set_caption(languages[lang]["GAMENAME"])

clock = time.Clock()

background = MakeImage(sprites["BACKGROUND"], win_width, win_height)

player = Player(sprites["PLAYER"], 5, win_height - 100, 75, 100, 5)

monsters = sprite.Group()

bullets = sprite.Group()

mixer.init()
mixer.music.load(sounds["MUSIC"])
mixer.music.play()

fire = mixer.Sound(sounds["FIRE"])

font.init()
font_main = font.Font(None, 48)

font_screens = font.Font(None, 92)

delay = 50
spawnrate = delay

while game_run:
    for e in event.get():
        if e.type == QUIT:
            game_run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire.play()
                player.fire()

    if not game_finish:

        if spawnrate <= 0:
            monster = Enemy(sprites["ENEMY"], randint(
                80, win_width - 80), -50, 80, 50, randint(3, 4))
            monsters.add(monster)
            delay -= 2
            spawnrate = delay
        else:
            spawnrate -= 1

        window.blit(background, (0, 0))

        kills_text = font_main.render(
            languages[lang]["SCORE_KILLS"] + str(player.kills), True, (255, 255, 255))
        window.blit(kills_text, (10, 10))

        losts_text = font_main.render(
            languages[lang]["SCORE_MISSES"] + str(player.losts), True, (255, 255, 255))
        window.blit(losts_text, (10, 60))

        player.reset()  # отрисовка
        player.update()  # управление

        player.bullets.draw(window)
        player.bullets.update()

        monsters.draw(window)
        monsters.update()

        if player.kills >= need_to_win:
            win_screen = font_screens.render(
                languages[lang]["WIN_TEXT"], True, (50, 255, 0))
            window.blit(win_screen, (225, 225))
            game_finish = True

        if player.losts >= need_to_lose:
            lose_screen = font_screens.render(
                languages[lang]["LOSE_TEXT"], True, (225, 0, 0))
            window.blit(lose_screen, (225, 225))
            game_finish = True

        if sprite.groupcollide(monsters, player.bullets, True, True):
            player.kills += 1

        if sprite.spritecollide(player, monsters, False):
            lose_screen = font_screens.render(
                languages[lang]["LOSE_TEXT"], True, (225, 0, 0))
            window.blit(lose_screen, (225, 225))
            game_finish = True

        display.update()

    clock.tick(60)
