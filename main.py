import pygame
import os
from bossctrlr import BossCtrlr
from humanctrlr import HumanCtrlr
from answerctrlr import AnswerCtrlr


#os.putenv('SDL_FBDEV', '/dev/fb0')

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800


def main():
    '''main'''
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    pygame.display.update()

    # font stuff
    font_big = pygame.font.Font(None, 140)

    # bg stuff
    raw_bg_img = pygame.image.load("bg.jpg")
    bg_img = pygame.transform.scale(
        raw_bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # controller
    human = HumanCtrlr()
    answer = AnswerCtrlr()
    boss = BossCtrlr()

    while boss.running:
        # Scan the buttons
        for event in pygame.event.get():
            boss.handle_event(event)
            human.handle_event(event)

        if human.dirty:
            answer.checkAll(human.lines)

        
        delta = 1.0 / 60.0
        steps = 1
        for _ in range(steps):
            human.tick(delta)

        # Draw stuff
        screen.blit(bg_img, (0, 0))
        
        human.draw(screen, font_big)
        answer.draw(screen, font_big)

        pygame.display.update()



if __name__ == "__main__":
    main()


