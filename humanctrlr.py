''' holds HumanCtrlr class '''
from math import sin, cos, pi, floor
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


def draw_polygon_outline(surface, color, vertex_count, radius, position):

    n, r = vertex_count, radius
    x, y = position
    verts = []
    for i in range(n):
        deg = 2 * pi * i / n + 0.125*pi
        verts.append((x + r * cos(deg), y + r * sin(deg)))

    pygame.draw.lines(surface, color, True, verts, 4)


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
        active_rows = 1
        for idx in range(active_rows):
            # x = self.beat_time*44/self.beat_duration + idx*22
            x = 48+self.beat_time*46/self.beat_duration
            y = 500-(self.current_row+idx)*46
            draw_polygon_outline(screen, (255, 255, 255), 8, 24, (x, y))

    def tick(self, delta):
        last_beat = round(self.beat_time/self.beat_duration)
        self.beat_time += delta*1000
        if self.beat_time >= 16*self.beat_duration:
            self.beat_time -= 16*self.beat_duration
            self.iteration = self.iteration + 1
            self.dirty_iteration = True
        self.current_beat = floor(self.beat_time/self.beat_duration)

        if last_beat != self.current_beat:
            self.dirty_beat = True

    def post_tick(self):
        self.dirty_button = False
        self.dirty_beat = False
        self.dirty_iteration = False