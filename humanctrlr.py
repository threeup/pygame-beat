''' holds HumanCtrlr class '''
from math import sin, cos, pi, floor
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


def draw_polygon_outline(surface, color, vertex_count, radius, position, width):

    n, r = vertex_count, radius
    x, y = position
    verts = []
    for i in range(n):
        deg = 2 * pi * i / n + 0.5*pi
        verts.append((x + r * cos(deg), y + r * sin(deg)))

    pygame.draw.lines(surface, color, True, verts, width)


class HumanCtrlr(Ctrlr):
    '''
    A class which manipulates controlled entities
    '''

    def __init__(self):
        Ctrlr.__init__(self)
        self.pressed = []
        self.current_row = 0
        self.current_beat = 0
        self.button_count = 4
        self.beat_time = 0
        self.iteration = 0
        self.dirty_button = False
        self.dirty_beat = False
        self.dirty_iteration = False
        self.beat_duration = 2000
        for _ in range(self.button_count):
            self.pressed.append(False)

    def handle_event(self, event):
        button_count = 4
        if event.type == pygame.JOYBUTTONDOWN:
            for idx in range(button_count):
                if event.button == idx:
                    self.pressed[idx] = True
                    self.dirty_button = True
        elif event.type == pygame.JOYBUTTONUP:
            for idx in range(button_count):
                if event.button == idx:
                    self.pressed[idx] = False

    def draw(self, screen):
        s = self.current_beat
        base_row = 4*floor(self.current_row/4)
        for r in range(base_row, base_row+4):
            xoffset = r%4*23
            x = 22+s*46+xoffset
            y = 540-r*39
            color = (55, 55, 55)
            width = 2
            outline = 22
            if r == self.current_row:
                color = (255, 255, 255)
                width = 4
                outline = 26
            draw_polygon_outline(screen, color, 6, outline, (x, y), width)

    def tick(self, delta):
        self.beat_time += delta*1000
        if self.beat_time >= 16*self.beat_duration:
            self.beat_time -= 16*self.beat_duration
            self.iteration = self.iteration + 1
            self.dirty_iteration = True
        
        last_beat = self.current_beat
        self.current_beat = floor(self.beat_time/self.beat_duration)

        if last_beat != self.current_beat:
            self.dirty_beat = True

    def post_tick(self):
        self.dirty_button = False
        self.dirty_beat = False
        self.dirty_iteration = False

