import pygame
import os
from math import floor
from bossctrlr import BossCtrlr
from humanctrlr import HumanCtrlr
from canvasctrlr import CanvasCtrlr
from musicctrlr import MusicCtrlr
from answerctrlr import AnswerCtrlr


#os.putenv('SDL_FBDEV', '/dev/fb0')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    '''main'''
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    joysticks = [pygame.joystick.Joystick(x) for x in range(joystick_count)]
    for j in range(joystick_count):
        joysticks[j].init()

    pygame.display.update()

    # controller
    human = HumanCtrlr()
    boss = BossCtrlr()
    canvas = CanvasCtrlr()
    music = MusicCtrlr()
    answer = AnswerCtrlr()
    music.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    answer.make()
    music.load_sounds()

    while boss.running:
        # Scan the buttons
        for event in pygame.event.get():
            boss.handle_event(event)
            human.handle_event(event)

        delta = 1.0 / 60.0
        steps = 1
        for _ in range(steps):
            canvas.tick(delta)
            human.tick(delta)

        if human.dirty_iteration:
            if canvas.check_answer(human.current_row, answer.answer):
                human.current_row = human.current_row + 1
                if human.current_row == 16:
                    canvas.clearall()
                    answer.make()
                    human.current_row = 0
                canvas.current_row = human.current_row
                answer.current_row = human.current_row
                music.stopall()

        if human.dirty_beat:
            row = human.current_row
            step = human.current_beat
            base_row = 4*floor(row/4)
            for r in range(base_row, base_row+4):
                val = canvas.read(r, step)
                for idx in range(4):
                    if r == row and human.pressed[idx]:
                        canvas.mark(row, step, idx)
                        music.play(r, idx)
                    elif val & (1 << idx):
                        music.play(r, idx)
                    else:
                        music.stop(r, idx)
        elif human.dirty_button:
            row = human.current_row
            step = human.current_beat
            canvas.clear(row, step)
            for idx in range(4):
                if human.pressed[idx]:
                    music.play(row, idx)
                    canvas.mark(row, step, idx)

        # Draw stuff
        music.draw(screen)
        answer.draw(screen)
        canvas.draw(screen)
        human.draw(screen)

        pygame.display.update()

        for _ in range(steps):
            human.post_tick()


if __name__ == "__main__":
    main()
