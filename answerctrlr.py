''' holds AnswerCtrlr class '''
import pygame
import json
import cairosvg
import io


from ctrlr import Ctrlr


# Colours
RED = (255, 22, 22)

class AnswerCtrlr(Ctrlr):
    '''
    A class which manipulates controlled entities
    '''

    def __init__(self):
        Ctrlr.__init__(self)
        self.answers = [None, None, None, None]
        self.snd = pygame.mixer.Sound('pulse-sound.ogg')
        self.snd.play()
        self.solved = set()
        
        filenames = ['basicdata.json','animalsdata.json','advanceddata.json','extradata.json']
        self.datadict = {}
        for filename in filenames:
            with open(filename) as f:
                self.data = json.load(f)
            
            for item in self.data["elements"]:
                txt = item["text"]
                img = item["img"]
                self.datadict[txt] = img

    def load_svg(self, filename, _w, _h):
        new_bites = cairosvg.svg2png(url = filename)
        byte_io = io.BytesIO(new_bites)
        return pygame.image.load(byte_io)

    # def load_svg(self, filename, w, h):
    #     svg = Parser.parse_file(filename)
    #     rast = Rasterizer()
    #     buff = rast.rasterize(svg, w, h)
    #     return pygame.image.frombuffer(buff, (w, h), 'RGBA')

    def checkAll(self, lines):
        for i in range(len(lines)):
            self.check(i, lines[i])

    def check(self, idx, line):
        line_spaces = line.lower().replace(' ', '_')
        if line_spaces in self.datadict:
            raw_img = self.load_svg(self.datadict[line_spaces], 512, 512)
            prev = self.answers[idx]
            self.answers[idx] = pygame.transform.scale(raw_img, (120, 120))
            if line_spaces not in self.solved:
                self.solved.add(line_spaces)
            if prev is None:
                self.snd.play()
        else:
            self.answers[idx] = None

    def draw(self, screen, font_big):
        half_width = screen.get_width()/2
        sixth_height = screen.get_height()/6
        for i in range(4):
            if self.answers[i] != None:
                draw_x = half_width + 0.5*half_width
                draw_y = sixth_height + i*sixth_height - 50
                screen.blit(self.answers[i], (draw_x, draw_y))
        
        text_surface = font_big.render('%d' % len(self.solved), True, RED)
        draw_x = screen.get_width()-70
        draw_y = 50
        rect = text_surface.get_rect(center=(draw_x, draw_y))
        screen.blit(text_surface, rect)
