import pygame as pg
import math
from geometry_utils import *

class Player:

    def __init__(self, screen, obstacle_list):

        self.screen, self.w, self.h = screen, screen.get_width(), screen.get_height()

        self.surface = pg.Surface((10, 10), pg.SRCALPHA)
        self.rect = self.surface.get_rect(center=(self.w//2, self.h//2))
        self.velocity = 4

        self.view_angle = math.pi/4

        self.obs_list = obstacle_list

    def move_left(self):
        if not self.collide_left():
            self.rect.x -= self.velocity

    def move_right(self):
        if not self.collide_right():
            self.rect.x += self.velocity

    def move_up(self):
        if not self.collide_up():
            self.rect.y -= self.velocity

    def move_down(self):
        if not self.collide_down():
            self.rect.y += self.velocity

    def collide_up(self):
        if self.rect.y - self.velocity < 0:
            return True
        pt = self.rect.x, self.rect.y - self.velocity
        for obs in self.obs_list:
            if obs.rect.collidepoint(pt):
                return True
        return False

    def collide_down(self):
        if self.rect.bottom + self.velocity > self.h:
            return True
        pt = self.rect.x, self.rect.y + self.velocity
        for obs in self.obs_list:
            if obs.rect.collidepoint(pt):
                return True
        return False

    def collide_left(self):
        if self.rect.x - self.velocity < 0:
            return True
        pt = self.rect.x - self.velocity, self.rect.y
        for obs in self.obs_list:
            if obs.rect.collidepoint(pt):
                return True
        return False

    def collide_right(self):
        if self.rect.right + self.velocity > self.w:
            return True
        pt = self.rect.right + self.velocity, self.rect.y
        for obs in self.obs_list:
            if obs.rect.collidepoint(pt):
                return True
        return False

    def udpate(self):
        pg.draw.circle(self.surface, (255, 0, 0), (5, 5), 5)
        
        ct = Point(*self.rect.center)
        points = self.get_all_points()

        vectors = [
            pg.Vector2(pt[0]-ct.x, pt[1]-ct.y)/2 for pt in points
        ]
        
        pts = []
        for vec in vectors:
            x, y = ct.x, ct.y
            pt = [x, y]
            while 0 < pt[0] < self.w and 0 < pt[1] < self.h:

                pt += vec
                #self.screen.set_at((int(pt[0]), int(pt[1])), (255, 0, 0))
                for obs in self.obs_list:
                    if obs.rect.collidepoint(pt):
                        break
                else:
                    continue
                break
            pts.append(pt)

        """pg.draw.circle(self.screen, (0, 255, 255), pts[0]-vectors[0], 10)
        pg.draw.circle(self.screen, (0, 255, 255), pts[-1]-vectors[-1], 10)
        for index, pt in enumerate(pts):
            pg.draw.circle(self.screen, (0, 0, 255), pt-vectors[index], 5)
            pg.draw.aaline(self.screen, (255, 0, 0), (ct.x, ct.y), pt)"""

        pg.draw.polygon(self.screen, (255, 255, 0), [
            (ct.x, ct.y),
            *pts,
            (ct.x, ct.y)
        ])

        self.screen.blit(self.surface, self.rect)

    def get_all_points(self):
        ct = Point(*self.rect.center)
        mo = Point(*pg.mouse.get_pos())
        angle = math.atan2(mo.y-ct.y, mo.x-ct.x)
        mo.x = ct.x + math.cos(angle)*30
        mo.y = ct.y + math.sin(angle)*30
        points = [(mo.x, mo.y)]
        for i in range(1, 768//4):
            angle = i*math.pi/768/2
            xM = mo.x - ct.x
            yM = mo.y - ct.y
            points.append(
                (round(xM * math.cos (angle) + yM * math.sin (angle) + ct.x),
                round(- xM * math.sin (angle) + yM * math.cos (angle) + ct.y))
            )
            points.insert(0,
                (round(xM * math.cos (-angle) + yM * math.sin (-angle) + ct.x),
                round(- xM * math.sin (-angle) + yM * math.cos (-angle) + ct.y))
            )

        return points

