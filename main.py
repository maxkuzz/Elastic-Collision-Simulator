from config import SCREEN_WIDTH, SCREEN_HEIGHT
from physics import Cube
from ui import draw_static_info
from input_handler import start_simulation

import os
import contextlib
with open(os.devnull, "w") as f, contextlib.redirect_stdout(f):
    import pygame

def main():
    s1, s2, v1, m1, v2, m2 = start_simulation()

    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 20, bold=True)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Elastic Collision Simulator")
    clock = pygame.time.Clock()

    cube1 = Cube(x=200, y=330, mass=m1, velocity=v1, color=(128, 0, 128), size=s1)
    cube2 = Cube(x=700, y=330, mass=m2, velocity=-v2, color=(0, 128, 0), size=s2)
    frame_count = 0
    running = True
    while running:
        dt = clock.tick(144) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        cube1.update(dt)
        cube2.update(dt)

        if cube1.collides_with(cube2):
            cube1.resolve_collision(cube2)

        screen.fill((170, 170, 170))
        cube1.draw(screen)
        cube2.draw(screen)
        draw_static_info(screen, font, cube1, cube2)
        pygame.display.flip()
        pygame.image.save(screen, f"frames/frame_{frame_count:04d}.png")
        frame_count += 1
        if frame_count >= 1440:
            running = False
    pygame.quit()


if __name__ == "__main__":
    main()
