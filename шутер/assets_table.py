import sys
from os import *  # path.join
# import os - os.path.join


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)


sprites = {
    "ASTEROID": resource_path(path.join("assets", "asteroid.png")),
    "BULLET": resource_path(path.join("assets", "bullet.png")),
    "BACKGROUND": resource_path(path.join("assets", "galaxy.png")),
    "PLAYER": resource_path(path.join("assets", "rocket.png")),
    "ENEMY": resource_path(path.join("assets", "ufo.png"))
}

sounds = {
    "FIRE": resource_path(path.join("music", "fire.ogg")),
    "MUSIC": resource_path(path.join("music", "space.ogg"))
}