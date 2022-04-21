"""
sorting algorithms visualiser made with pygame
ps: special thanks to https://github.com/keon/algorithms
"""

import pygame
from pygame.locals import *

import random
import sys

from font_system import draw_text
from sort import bubble_sort, cycle_sort

pygame.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
TARGET_FPS = 60


class Application:

    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Sort Visualizer")
        self.display_surface = pygame.display.set_mode(SCREEN_SIZE)
        self.is_running = False

        self.iteration = 0
        self.unsorted_lists = [[i for i in range(100)] for _ in range(2)]
        for lst in self.unsorted_lists:
            random.shuffle(lst)

    def run(self):
        self.is_running = True
        while self.is_running:

            frame_time_ms = self.clock.tick(TARGET_FPS)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.terminate()

            self.draw_frame()
            self.iteration += 1

        pygame.quit()
        sys.exit()

    def terminate(self):
        self.is_running = False

    def draw_frame(self):
        self.display_surface.fill("white")

        # bubble sort
        draw_text("bubble sort", self.display_surface, (10, 10))
        self.draw_iteration(self.unsorted_lists[0],
                            bubble_sort, pygame.Rect(10, 20, 200, 100))

        # cycle sort
        draw_text("cycle sort", self.display_surface, (220, 10))
        #self.draw_iteration(self.unsorted_lists[1],
        #                    cycle_sort, pygame.Rect(220, 20, 200, 100))

        pygame.display.update()

    def draw_iteration(self, lst, sort_func, rect):
        current_state = sort_func(lst)
        col_width = rect.width // len(lst)
        for i, number in enumerate(current_state):
            pygame.draw.rect(self.display_surface, "black", (rect.x + i * col_width,
                                                             rect.y + rect.height - number,
                                                             col_width,
                                                             number))


if __name__ == "__main__":
    Application().run()
