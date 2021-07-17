import pygame as pg


class Obstacle:

    def __init__(self, screen, size, coordinates) -> None:
        self.screen, self.w, self.h = screen, screen.get_width(), screen.get_height()
        
        self.surf = pg.Surface(size)
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(topleft=coordinates)

    def update(self):
        self.screen.blit(self.surf, self.rect)