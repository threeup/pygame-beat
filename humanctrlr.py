''' holds HumanCtrlr class '''
import pygame
from ctrlr import Ctrlr


# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class HumanCtrlr(Ctrlr):
    '''
    A class which manipulates controlled entities
    '''

    def __init__(self):    
        Ctrlr.__init__(self)  
        self.lines = ["", "", "", ""]
        self.line_index = 0
        self.dark_mode = False
        self.alive_time = 0
        self.lshift = False
        self.rshift = False
        self.dirty = False
    
    def handle_event(self, event):
        if event.type == pygame.KEYUP:
            if event.key:
                if event.key == pygame.K_LSHIFT:
                    self.lshift = False
                elif event.key == pygame.K_RSHIFT:
                    self.rshift = False
        elif event.type == pygame.KEYDOWN:
            if event.key:
                if event.key == pygame.K_RETURN:
                    self.line_index = (self.line_index + 1) % 4
                    self.lines[self.line_index] = ""
                elif event.key == pygame.K_SPACE:
                    self.lines[self.line_index] += ' '
                    self.dirty = True
                elif event.key == pygame.K_LSHIFT:
                    self.lshift = True
                elif event.key == pygame.K_RSHIFT:
                    self.rshift = True
                elif event.key == pygame.K_BACKSPACE:
                    if len(self.lines[self.line_index]) > 0:
                        self.lines[self.line_index] = self.lines[self.line_index][:-1]
                        self.dirty = True
                elif event.key == pygame.K_TAB:
                    self.dark_mode = self.dark_mode == False
                else:
                    key_name = pygame.key.name(event.key)
                    if self.lshift or self.rshift:
                        key_name = key_name.upper()
                    self.lines[self.line_index] += key_name 
                    if len(self.lines[self.line_index]) > 27:
                        self.lines[self.line_index] = ""
                    self.dirty = True

    def draw(self, screen, font_big):
        half_width = screen.get_width()/2
        sixth_height = screen.get_height()/6
        for i in range(4):
            draw_x = half_width
            draw_y = sixth_height+i*sixth_height
            line = self.lines[i]
            remainder = self.alive_time % 50
            if remainder < 25 and i == self.line_index:
                line += "|"
            else:
                line += " "
            text_surface = font_big.render(
                '%s' % line, True, BLACK if self.dark_mode else WHITE)
            rect = text_surface.get_rect(center=(draw_x, draw_y))
            screen.blit(text_surface, rect)
        self.dirty = False
        

    def tick(self, delta):
        self.alive_time = round(self.alive_time + delta*1000)
        return
