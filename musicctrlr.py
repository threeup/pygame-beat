''' holds MusicCtrlr class '''
import pygame
from ctrlr import Ctrlr


class MusicCtrlr(Ctrlr):
    '''
    A class which represents the music
    '''

    def __init__(self):
        Ctrlr.__init__(self)

    def setup(self, screen_width, screen_height):
        raw_bg_img = pygame.image.load("hexbg.jpg")
        self.bg = pygame.transform.scale(
            raw_bg_img, (screen_width, screen_height))

    def load_sounds(self):
        self.current_sounds = []
        self.is_playing = []

        self.current_sounds.append(
            pygame.mixer.Sound('audio/bassdrum.ogg'))  
        self.current_sounds.append(pygame.mixer.Sound(
            'audio/acousticsnare.ogg'))  
        self.current_sounds.append(
            pygame.mixer.Sound('audio/cymbal.ogg'))  
        self.current_sounds.append(pygame.mixer.Sound('audio/clap.ogg'))  
        self.current_sounds.append(pygame.mixer.Sound(
            'audio/electricsnare.ogg'))  
        self.current_sounds.append(
            pygame.mixer.Sound('audio/cabasa.ogg'))  
        self.current_sounds.append(
            pygame.mixer.Sound('audio/closehihat.ogg'))  
        self.current_sounds.append(pygame.mixer.Sound('audio/hiconga.ogg'))
        self.current_sounds.append(pygame.mixer.Sound('audio/bassdrum.ogg'))
        self.current_sounds.append(pygame.mixer.Sound('audio/pedalhihat.ogg'))
        self.current_sounds.append(pygame.mixer.Sound('audio/closehihat.ogg'))
        self.current_sounds.append(pygame.mixer.Sound('audio/cymbal.ogg'))
        self.current_sounds.append(
            pygame.mixer.Sound('audio/acousticsnare.ogg'))
        self.current_sounds.append(pygame.mixer.Sound('audio/cabasa.ogg'))
        self.current_sounds.append(pygame.mixer.Sound('audio/closehihat.ogg'))
        self.current_sounds.append(
            pygame.mixer.Sound('audio/electricsnare.ogg'))

        for idx in range(len(self.current_sounds)):
            self.current_sounds[idx].set_volume(0.25)
            self.is_playing.append(False)

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))

    def play(self, row, idx):
        slot = (row % 4)*4+idx
        if not self.is_playing[slot]:
            #print("play", row, " ", idx)
            self.current_sounds[slot].play()
            self.is_playing[slot] = True

    def stop(self, row, idx):
        slot = (row % 4)*4+idx
        if self.is_playing[slot]:
            #print("stop", row, " ", idx)
            self.current_sounds[slot].stop()
            self.is_playing[slot] = False

    def stopall(self):
        for idx in range(len(self.current_sounds)):
            if self.is_playing[idx]:
                self.current_sounds[idx].stop()
                self.is_playing[idx] = False
