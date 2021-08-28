''' holds CanvasCtrlr class '''
from math import sin, cos, pi
import pygame
from ctrlr import Ctrlr
from lib import coord_to_draw, val_to_color, polygon_verts


def draw_polygon(surface, color, vertex_count, radius, position):
    verts = polygon_verts(vertex_count, radius, position)
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
        rowcount = min(self.current_row+1, self.rows)
        for row in range(rowcount):
            for step in range(self.steps):
                (x, y) = coord_to_draw(row+2, step+2, 2)
                val = self.grid[row][step]
                color = val_to_color(val, False)
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

    def mark_row(self, row, answer):
        for s in range(self.steps):
            self.grid[row][s] = answer[row][s]

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
                    print("miss",s,answer[row][s])
                    miss += 1
            else:
                hit += 1
        print("hit", hit, "extra", extra, "miss", miss)
        return miss == 0
