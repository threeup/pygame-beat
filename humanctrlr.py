''' holds HumanCtrlr class '''
from math import sin, cos, pi, floor
import pygame
from ctrlr import Ctrlr
from lib import coord_to_draw, polygon_verts, polygon_outline


def draw_polygon(surface, color, vertex_count, radius, position):
    verts = polygon_verts(vertex_count, radius, position)
    pygame.draw.polygon(surface, color, verts)


def draw_polygon_outline(surface, color, vertex_count, radius, position, width):
    verts = polygon_outline(vertex_count, radius, position)
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
        self.skip_level = False
        self.beat_duration = 1600
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.pressed[0] = True
                self.dirty_button = True
            elif event.key == pygame.K_y:
                self.pressed[1] = True
                self.dirty_button = True
            elif event.key == pygame.K_g:
                self.pressed[2] = True
                self.dirty_button = True
            elif event.key == pygame.K_b:
                self.pressed[3] = True
                self.dirty_button = True
            elif event.key == pygame.K_RETURN:
                self.skip_level = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                self.pressed[0] = False
            elif event.key == pygame.K_y:
                self.pressed[1] = False
            elif event.key == pygame.K_g:
                self.pressed[2] = False
            elif event.key == pygame.K_b:
                self.pressed[3] = False

    def draw(self, screen):
        step = self.current_beat
        base_row = 4*floor(self.current_row/4)
        for row in range(base_row, base_row+4):
            (x,y) = coord_to_draw(row+2, step+2, 2)
            color = (55, 55, 55)
            width = 2
            outline = 22
            if row == self.current_row:
                color = (255, 255, 255)
                width = 6
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
        self.skip_level = False

