''' holds MusicCtrlr class '''
import pygame
from ctrlr import Ctrlr


class MusicCtrlr(Ctrlr):
    '''
    A class which represents the music
    '''

    def __init__(self):    
        Ctrlr.__init__(self)  
        self.current_sounds = []
        self.is_playing = []
        self.current_sounds.append(pygame.mixer.Sound('IAMM_Gsh1_PEDAL_HIHAT.wav'))
        self.current_sounds.append(pygame.mixer.Sound('IAMM_D1_ACOUSTIC_SNARE.wav'))
        self.current_sounds.append(pygame.mixer.Sound('IAMM_Dsh2_RIDE_CYMBAL_1.wav'))
        self.current_sounds.append(pygame.mixer.Sound('IAMM_E1_ELECTRIC_SNARE.wav'))
        
        for idx in range(len(self.current_sounds)):
            self.current_sounds[idx].set_volume(0.1)
            self.is_playing.append(False)
    

    def play(self, idx):
        if not self.is_playing[idx]:
            self.current_sounds[idx].play()
            self.is_playing[idx] = True

    def stop(self, idx):
        if self.is_playing[idx]:
            self.current_sounds[idx].stop()
            self.is_playing[idx] = False