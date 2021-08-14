''' holds WorldCtrlr class '''
from math import sin, cos, pi
import pygame
import random
from ctrlr import Ctrlr


def draw_polygon(surface, color, vertex_count, radius, position):
    n, r = vertex_count, radius
    x, y = position
    verts = []
    for i in range(n):
        deg = 2 * pi * i / n + 0.5*pi
        verts.append((x + r * cos(deg), y + r * sin(deg)))
    pygame.draw.polygon(surface, color, verts)


def draw_polygon_outline(surface, color, vertex_count, radius, position):

    n, r = vertex_count, radius
    x, y = position
    verts = []
    for i in range(n):
        deg = 2 * pi * i / n + 0.5*pi
        verts.append((x + r * cos(deg), y + r * sin(deg)))

class AnswerCtrlr(Ctrlr):
    '''
    A class which represents the world
    '''

    def __init__(self):
        Ctrlr.__init__(self)

        self.answer = []
        self.rows = 12
        self.steps = 16
        self.current_row = 0
        for _ in range(self.rows):
            row = []
            for _ in range(self.steps):
                row.append(0)
            self.answer.append(row)

    def make(self):
        for r in range(self.rows):
            for s in range(self.steps):
                mode = 0
                if r > 6:
                    mode = random.randint(0,2)
                elif r > 3:
                    mode = random.randint(0,1)
                elif s % 2 == 0:
                    mode = random.randint(0,1)
                if mode == 0:
                    self.answer[r][s] = 0
                elif mode == 1:
                    col = random.randint(0,3)
                    self.answer[r][s] = 1 << col
                else:
                    self.answer[r][s] = random.randint(0,15)
                    

    def draw(self, screen):
        rowcount = min(self.current_row,self.rows)
        for r in range(self.rows):
            for s in range(self.steps):
                xoffset = r%4*23
                x = 22+s*46+xoffset
                y = 540-r*39
                val = self.answer[r][s]
                color = [0,0,0]
                if val & 1:
                    color[0]=250
                if val & 2:
                    color[0]=max(color[0], 180)
                    color[1]=max(color[1], 180)
                if val & 4:
                    color[1]=250
                if val & 8:
                    color[2]=250
                if r > rowcount:
                    color[0] *= 0.4
                    color[1] *= 0.4
                    color[2] *= 0.4
                draw_polygon(screen, tuple(color), 6, 26, (x, y))
