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
        raw_bg_img = pygame.image.load("hexgame.jpg")
        self.bg = pygame.transform.scale(
            raw_bg_img, (screen_width, screen_height))

    def load_sounds(self):
        self.current_sounds = []
        self.is_playing = []

        drum_sound_files = ['audio/bassdrum.ogg','audio/acousticsnare.ogg','audio/cymbal.ogg','audio/clap.ogg']
        melody_sound_files = ['audio/daaaadeedooFMinor.ogg','audio/duhduhA.ogg','audio/lowvibesBb.ogg','audio/lowvibesF.ogg']
        flare_sound_files = ['audio/flutepop.ogg','audio/flutebreathyFMin.ogg','audio/flutepulseG.ogg','audio/fluteunderwater.ogg']
        extra_sound_files = ['audio/scifihigh.ogg','audio/scifilow.ogg','audio/bellsdusty.ogg','audio/swellingnoise.ogg']

        for f in drum_sound_files:
            snd = pygame.mixer.Sound(f)
            snd.set_volume(0.30)
            self.current_sounds.append(snd)
        
        for f in melody_sound_files:
            snd = pygame.mixer.Sound(f)
            snd.set_volume(0.20)
            self.current_sounds.append(snd)
            
        for f in flare_sound_files:
            snd = pygame.mixer.Sound(f)
            snd.set_volume(0.15)
            self.current_sounds.append(snd)
            
        for f in extra_sound_files:
            snd = pygame.mixer.Sound(f)
            snd.set_volume(0.20)
            self.current_sounds.append(snd)


        for idx in range(len(self.current_sounds)):
            self.current_sounds[idx].set_volume(0.25)
            self.is_playing.append(False)

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))

    def play(self, row, idx):
        slot = (row % 4)*4+idx
        if not self.is_playing[slot]:
            self.current_sounds[slot].play()
            self.is_playing[slot] = True

    def stop(self, row, idx):
        slot = (row % 4)*4+idx
        if self.is_playing[slot]:
            self.current_sounds[slot].stop()
            self.is_playing[slot] = False

    def stopall(self):
        for idx in range(len(self.current_sounds)):
            if self.is_playing[idx]:
                self.current_sounds[idx].stop()
                self.is_playing[idx] = False
