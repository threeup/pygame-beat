''' holds HumanCtrlr class '''
import pygame
from ctrlr import Ctrlr


class HumanCtrlr(Ctrlr):
    '''
    A class which manipulates controlled entities
    '''

    def __init__(self):    
        Ctrlr.__init__(self)  
        self.pressed = []
        self.released = []
        self.snd = []
        self.img = []
        count = 4
        for _ in range(count):
            self.pressed.append(0)
            self.released.append(0)
        self.snd.append(pygame.mixer.Sound('pulse-motive-2.ogg'))
        self.snd.append(pygame.mixer.Sound('pulse-motive-3.ogg'))
        self.snd.append(pygame.mixer.Sound('pulse-thing-2.ogg'))
        self.snd.append(pygame.mixer.Sound('pulse-motive-4.ogg'))
        self.img.append(pygame.image.load('hoopred.png'))
        self.img.append(pygame.image.load('hoopyellow.png'))
        self.img.append(pygame.image.load('hoopgreen.png'))
        self.img.append(pygame.image.load('hoopblue.png'))
        
        for i in range(count):
            self.snd[i].set_volume(0.01)
            self.img[i] = pygame.transform.scale(self.img[i], (150,150))
        self.dark_mode = False
        self.alive_time = 0
        self.dirty = False
    
    def handle_event(self, event):
        count = 4
        if event.type == pygame.JOYBUTTONDOWN:
            for i in range(count):
                if event.button == i:
                    self.pressed[i] = self.alive_time
                    if self.released[i] > 2000:
                        self.snd[i].stop()
                        self.released[i] = 0
        elif event.type == pygame.JOYBUTTONUP:
            for i in range(count):
                if event.button == i:
                    self.released[i] = self.alive_time - self.pressed[i]
                    if self.released[i] > 2000:
                        print(self.released[i])
                        self.snd[i].play()
                    self.pressed[i] = 0
        

    def draw(self, screen, font_big):
        self.dirty = False
        count = 4
        for i in range(count):
            if self.pressed[i] > 0:
                draw_x = 100+i*100
                draw_y = 100
                screen.blit(self.img[i], (draw_x, draw_y))
        

    def tick(self, delta):
        self.alive_time = round(self.alive_time + delta*1000)
        return
