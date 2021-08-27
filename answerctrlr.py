''' holds WorldCtrlr class '''
from math import sin, cos, pi, floor
import pygame
import random
import json
from ctrlr import Ctrlr
from lib import coord_to_draw, in_bounds, val_to_color, polygon_verts


def draw_polygon(surface, color, vertex_count, radius, position):
    verts = polygon_verts(vertex_count, radius, position)
    pygame.draw.polygon(surface, color, verts)


class AnswerCtrlr(Ctrlr):
    '''
    A class which represents the world
    '''

    def __init__(self):
        Ctrlr.__init__(self)

        self.answer = []
        self.picture = []
        self.rows = 16
        self.steps = 20
        self.padding = 2
        self.current_row = 0
        answer_rows = self.rows-self.padding*2
        answer_steps = self.steps-self.padding*2
        for _ in range(answer_rows):
            row = []
            for _ in range(answer_steps):
                row.append(0)
            self.answer.append(row)

        for _ in range(self.rows):
            row = []
            for _ in range(self.steps):
                row.append([100, 100, 100])
            self.picture.append(row)

        with open("picture.json") as f:
            self.data = json.load(f)
            for item in self.data["colors"]:
                x = item["x"]
                y = item["y"]
                rgba = item["rgba"]
                self.picture[y][x] = rgba

        for r in range(self.rows):
            if r > 0:
                for x in range(self.steps):
                    prev = self.picture[0][x]
                    base = self.picture[r-1][x]
                    next = [prev[0]+base[0], prev[1]+base[1], prev[2]+base[2]]
                    next[0] = next[0] + random.randint(-30, 30)
                    next[1] = next[1] + random.randint(-30, 30)
                    next[2] = next[2] + random.randint(-30, 30)
                    next[0] = max(next[0],0)
                    next[1] = max(next[1],0)
                    next[2] = max(next[2],0)
                    rgba = [next[0]/3, next[1]/3, next[2]/3, 1]
                    self.picture[r][x] = rgba

    def make_answer(self):
        answer_rows = self.rows-self.padding*2
        answer_steps = self.steps-self.padding*2
        for r in range(answer_rows):
            for s in range(answer_steps):
                mode = r % 4
                if mode == 0:
                    # beat every other
                    if s % 2 == 1:
                        col = random.randint(0, 3)
                        self.answer[r][s] = 1 << col
                    else:
                        col = random.randint(0, 6)
                        if col <= 3:
                            self.answer[r][s] = 1 << col 
                elif mode == 1:
                    # long pulse
                    if s % 4 == 0:
                        col = random.randint(0, 3)
                        self.answer[r][s] = 1 << col
                    elif s > 0 and s % 4 != 3:
                        self.answer[r][s] = self.answer[r][s-1]
                    else:
                        self.answer[r][s] = 0
                elif mode == 2:
                    if s % 2 == 0 or (s+1) % 4 == 0:
                        col = random.randint(0, 3)
                        self.answer[r][s] = 1 << col
                else:
                    if s % 2 == 1 or s % 4 == 0:
                        col1 = random.randint(0, 2)
                        col1 = col1+1 if col1 != 0 else col1
                        col2 = random.randint(0, 2)
                        col2 = col2+1 if col2 != 0 else col2
                        bit1 = 1 << col1
                        bit2 = 1 << col2
                        self.answer[r][s] = bit1 + bit2

    def draw_picture(self, screen, row, step, x, y):
        val = self.picture[row][step]
        color = [val[0], val[1], val[2]]
        if row > min(self.current_row+self.padding, self.rows):
            color[0] *= 0.7
            color[1] *= 0.7
            color[2] *= 0.7
        draw_polygon(screen, tuple(color), 6, 26, (x, y))
        return

    def draw_answer(self, screen, row, step, x, y):
        val = self.answer[row][step]
        muted = row > min(self.current_row, self.rows)
        color = val_to_color(val, muted)
        draw_polygon(screen, tuple(color), 6, 26, (x, y))

        return

    def draw(self, screen):

        base_row = 4*floor(self.current_row/4)+self.padding
        for row in range(self.rows):
            for step in range(self.steps):
                (x, y) = coord_to_draw(row, step, self.padding)
                if row < base_row or row >= base_row + 4:
                    self.draw_picture(screen, row, step, x, y)
                elif in_bounds(row, step, self.rows, self.steps, self.padding):
                    self.draw_answer(screen, row-self.padding,
                                     step-self.padding, x, y)
                else:
                    self.draw_picture(screen, row, step, x, y)
