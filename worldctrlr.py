''' holds WorldCtrlr class '''
from math import sin, cos, pi
import pygame
from ctrlr import Ctrlr


def draw_polygon(surface, color, vertex_count, radius, position):
    n, r = vertex_count, radius
    x, y = position
    verts = []
    for i in range(n):
        deg = 2 * pi * i / n + 0.125*pi
        verts.append((x + r * cos(deg), y + r * sin(deg)))
    pygame.draw.polygon(surface, color, verts)


class WorldCtrlr(Ctrlr):
    '''
    A class which represents the world
    '''

    def __init__(self):
        Ctrlr.__init__(self)

        self.grid = []
        self.rows = 8
        self.steps = 16
        for _ in range(self.rows):
            row = []
            for _ in range(self.steps):
                row.append(0)
            self.grid.append(row)

    def setup(self, screen_width, screen_height):

        raw_bg_img = pygame.image.load("hexbg.jpg")
        self.bg = pygame.transform.scale(
            raw_bg_img, (screen_width, screen_height))

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        for r in range(self.rows):
            for s in range(self.steps):
                x = 48+s*46
                y = 500-r*46
                val = self.grid[r][s]
                color = [0,0,0]
                if val & 1:
                    color[0]=200
                if val & 2:
                    color[0]=150
                    color[1]=150
                if val & 4:
                    color[1]=200
                if val & 8:
                    color[2]=200
                draw_polygon(screen, tuple(color), 8, 24, (x, y))

    def mark(self, row, step, bit):
        self.grid[row][step] |= (1 << bit)
    
    def clear(self, row, step):
        self.grid[row][step] = 0

    def clearall(self):
        for row in range(self.rows):
            for step in range(self.steps):
                self.clear(row, step)

    def read(self, row, step):
        return self.grid[row][step]
