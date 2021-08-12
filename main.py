from worldctrlr import WorldCtrlr
import pygame
import os
from bossctrlr import BossCtrlr
from humanctrlr import HumanCtrlr
from worldctrlr import WorldCtrlr
from musicctrlr import MusicCtrlr


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
    world = WorldCtrlr()
    music = MusicCtrlr()
    world.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    music.load_sounds(human.current_row)

    while boss.running:
        # Scan the buttons
        for event in pygame.event.get():
            boss.handle_event(event)
            human.handle_event(event)

        
        delta = 1.0 / 60.0
        steps = 1
        for _ in range(steps):
            world.tick(delta)
            human.tick(delta)

        if human.dirty_iteration:
            print(human.iteration)
            if human.iteration % 12 == 0:
                world.clearall()
            if human.iteration % 2 == 0:
                human.current_row = (human.current_row + 1) % 3
                music.stopall()
                music.load_sounds(human.current_row)
            

        if human.dirty_beat:
            row = human.current_row
            step = human.current_beat
            val = world.read(row,step)
            for idx in range(human.button_count):
                if human.pressed[idx]:
                    world.mark(row,step,idx)
                    music.play(idx)
                elif val & (1 << idx):
                    music.play(idx)
                else:
                    music.stop(idx)
        elif human.dirty_button:
            row = human.current_row
            step = human.current_beat
            world.clear(row,step)
            for idx in range(human.button_count):
                if human.pressed[idx]:
                    music.play(idx)
                    world.mark(row,step,idx)


        # Draw stuff
        world.draw(screen)
        human.draw(screen)

        pygame.display.update()

        
        for _ in range(steps):
            human.post_tick()



if __name__ == "__main__":
    main()


