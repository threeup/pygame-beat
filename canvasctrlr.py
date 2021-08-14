''' holds CanvasCtrlr class '''
from math import sin, cos, pi
import pygame
from ctrlr import Ctrlr


def draw_polygon(surface, color, vertex_count, radius, position):
    n, r = vertex_count, radius
    x, y = position
    verts = []
    for i in range(n):
        deg = 2 * pi * i / n + 0.5*pi
        verts.append((x + r * cos(deg), y + r * sin(deg)))
    pygame.draw.polygon(surface, color, verts)


class CanvasCtrlr(Ctrlr):
    '''
    A class which represents the canvas
    '''

    def __init__(self):
        Ctrlr.__init__(self)

        self.grid = []
        self.rows = 12
        self.steps = 16
        self.current_row = 0
        for _ in range(self.rows):
            row = []
            for _ in range(self.steps):
                row.append(0)
            self.grid.append(row)


    def draw(self, screen):
        rowcount = min(self.current_row+1,self.rows)
        for r in range(rowcount):
            for s in range(self.steps):
                xoffset = r%4*23
                x = 22+s*46+xoffset
                y = 540-r*39
                val = self.grid[r][s]
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
                draw_polygon(screen, tuple(color), 6, 16, (x, y))

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

    def check_answer(self, row, answer):
        hit = 0
        extra = 0
        miss = 0
        for s in range(self.steps):
            if self.grid[row][s] != answer[row][s]:
                self.grid[row][s] = 0
                if answer[row][s] == 0:
                    extra += 1
                else:
                    miss += 1
            else:
                hit += 1
        print("hit",hit,"extra",extra,"miss",miss)
        return miss == 0