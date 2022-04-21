import pygame
from pygame.locals import *

import random
import sys


DRAW_SIZE = DRAW_WIDTH, DRAW_HEIGHT = 320, 200
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = tuple(d * 4 for d in DRAW_SIZE)

CHAR_WIDTH = 5
CHAR_HEIGHT = 10
CHAR_TOP_MARG = 2
CHAR_BOTTOM_MARG = 1

font_img = pygame.image.load("pixel_font.png")
print("a is ", ord("a"))
print("b is ", ord("b"))


def get_text_size(string):
    substrings = string.split("\n")
    return len(max(substrings, key=len)), len(substrings)


def shift_string(string):
    substrings = string.split("\n")
    substrings = [substrings[-1]] + substrings[:-1]
    return "\n".join(substrings)


def change_color_to(surface, old_color, new_color):
    w, h = surface.get_size()
    for i in range(w):
        for j in range(h):
            if surface.get_at((i, j)) == old_color:
                surface.set_at((i, j), new_color)
    return surface


def draw_text(text, surface, pos, font_size=1, spacing=1, color=(0, 0, 0)):
    x, y = pos

    cw, ch = get_text_size(text)
    total_width = cw * (CHAR_WIDTH + spacing) * font_size
    total_height = ch * (CHAR_HEIGHT + spacing) * font_size
    text_surface = pygame.Surface((total_width, total_height), SRCALPHA, 32).convert_alpha()

    scaled_font = pygame.transform.scale(font_img, tuple(d * font_size for d in font_img.get_size()))
    scaled_font = change_color_to(scaled_font, pygame.Color(0, 0, 0), color)
    char_width = CHAR_WIDTH * font_size
    char_height = CHAR_HEIGHT * font_size

    xx = 0
    yy = 0
    for char in text:
        if char == " ":
            xx += 1
            continue
        elif char == "\n":
            xx = 0
            yy += 1
            continue
        text_surface.blit(scaled_font,
                          (xx * (char_width + spacing * font_size), yy * (char_height + spacing * font_size)),
                          ((ord(char)-97) * (char_width + font_size), 0, char_width, char_height))
        xx += 1
    surface.blit(text_surface, (x, y))


class App:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.draw_surface = pygame.Surface(DRAW_SIZE)
        self.display_surface = pygame.display.set_mode(SCREEN_SIZE)

        self.string = "anya\nwill\nbe\nfine"
        self.words = ["die", "god", "human", "hope", "dream", "scars", "hard times", "drugs", "lil"]
        self.string2 = "\n".join(random.sample(self.words, 4))
        print(self.string2)

    def run(self):
        while True:

            frame_time_ms = self.clock.tick(4)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            #self.string = self.string[-1] + self.string[:-1]
            self.string = shift_string(self.string)

            self.draw_surface.fill("white")
            #draw_text("hello there", self.draw_surface, (10, 10), 3, 5)
            draw_text(self.string2, self.draw_surface, (80, 50), 2, 4, pygame.Color(195, 48, 31))
            draw_text(self.string, self.draw_surface, (10, 10), 1, 10)

            new_surf = pygame.transform.scale(self.draw_surface, SCREEN_SIZE)
            self.display_surface.blit(new_surf, (0, 0))
            pygame.display.update()

if __name__ == "__main__":
    print(get_text_size("hello, my\nname is\nnic"))
    App().run()
