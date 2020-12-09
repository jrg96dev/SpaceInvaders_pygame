import pygame

class Enemy:
    sprite = None
    pos_x = 0
    pos_y = 0

    def __init__(self):
        # Load default sprite image
        self.sprite = pygame.image.load('enemy.png')

