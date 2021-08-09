''' holds HumanCtrlr class '''
import pygame
from ctrlr import Ctrlr


class BossCtrlr(Ctrlr):
    '''
    A class which manipulates controlled entities
    '''

    def __init__(self):    
        Ctrlr.__init__(self)  
        self.running = True
    
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.running = False
