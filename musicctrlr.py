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
            self.current_sounds.append(pygame.mixer.Sound('audio/clap.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('audio/bassdrum.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('audio/cymbal.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('audio/electricsnare.ogg'))
        elif(bank== 1):
            self.current_sounds.append(pygame.mixer.Sound('audio/acousticsnare.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('audio/cabasa.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('audio/closehihat.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('audio/hiconga.ogg'))
        else:
            self.current_sounds.append(pygame.mixer.Sound('audio/bassdrum.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('audio/pedalhihat.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('audio/closehihat.ogg'))
            self.current_sounds.append(pygame.mixer.Sound('audio/cymbal.ogg'))
        
        for idx in range(len(self.current_sounds)):
            self.current_sounds[idx].set_volume(0.25)
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