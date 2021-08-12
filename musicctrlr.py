''' holds MusicCtrlr class '''
import pygame
from ctrlr import Ctrlr


class MusicCtrlr(Ctrlr):
    '''
    A class which represents the music
    '''

    def __init__(self):    
        Ctrlr.__init__(self)

    def load_sounds(self, bank):
        self.current_sounds = []
        self.is_playing = []
        if(bank == 0):
            self.current_sounds.append(pygame.mixer.Sound('clap.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('bassdrum.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('cymbal.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('electricsnare.ogg'))
        elif(bank== 1):
            self.current_sounds.append(pygame.mixer.Sound('acousticsnare.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('cabasa.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('closehihat.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('hiconga.ogg'))
        else:
            self.current_sounds.append(pygame.mixer.Sound('bassdrum.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('pedalhihat.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('closehihat.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('cymbal.ogg'))
        
        for idx in range(len(self.current_sounds)):
            self.current_sounds[idx].set_volume(0.1)
            self.is_playing.append(False)
    

    def play(self, idx):
        if not self.is_playing[idx]:
            self.current_sounds[idx].play()
            self.is_playing[idx] = True

    def stopall(self):
        for idx in range(len(self.current_sounds)):
            if self.is_playing[idx]:
                self.current_sounds[idx].stop()
                self.is_playing[idx] = False
    

    def stop(self, idx):
        if self.is_playing[idx]:
            self.current_sounds[idx].stop()
            self.is_playing[idx] = False