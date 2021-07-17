import pygame as pg
import math

def draw_line(surface: pg.Surface, 
              color:tuple[int, int, int], 
              p1: tuple[int, int], 
              p2: tuple[int, int], 
              w_limit: int, 
              h_limit: int):

    x1, y1 = p1
    x2, y2 = p2
    try:
        k = (x1 - x2) / (y1 - y2)
    except ZeroDivisionError:
        k = 0
    m = y1 - k * x1
    def f(x):
        return x*k + m

    pg.draw.line(surface, color, (w_limit, f(w_limit)), (0, f(0)))


def dist(A: tuple[int, int], B: tuple[int, int]):
    return math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist(self, point):
        return math.sqrt((self.x-point.x)**2 + (self.y-point.y)**2)


def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)