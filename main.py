#
#  Pixelator
#  A pygame application that converts your image into a pixelated image
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import pygame
import os
from Pixelator.constants import *
from Pixelator.classes import Image
from pumpkinpy.pygameutils import elements as pg
from tkinter.filedialog import askdirectory, askopenfilename


# Window Management
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_width//2-WIDTH//2, screen_height//2-HEIGHT//2)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixelator")


def draw_window(win, width, height, image, open_button, pixel_button, save_button, events):
    win.fill(WHITE)
    win.fill(GREY, (950, 0, 550, HEIGHT))
    file_name = image.path.split("/")
    if len(file_name) == 1:
        file_name = "".join(file_name).split("\\")
    file_name = file_name[-1]
    text = FONT.render(file_name if file_name != "starter_image.png" else "None", 1, BLACK if file_name != "starter_image.png" else RED)
    win.blit(text, (1250 - text.get_width()//2, 25))
    open_button.Draw(win, events)
    pixel_button.Draw(win, events)
    save_button.Draw(win, events)


def main(win, width, height):
    clock = pygame.time.Clock()
    image = Image(os.path.join("assets", "starter_image.png"), 50, 50)
    open_button = pg.ButtonText((1250 - 100, 100), (200, 60), (0, 255, 0), (0, 200, 0), (0, 255, 0), FONT.render("Open", 1, BLACK), (0, 0), 5, BLACK)
    pixel_button = pg.ButtonText((1250 - 125, 200), (250, 80), (0, 255, 0), (0, 200, 0), (0, 255, 0), B_FONT.render("Pixelate", 1, BLACK), (0, 0), 5, BLACK)
    save_button = pg.ButtonText((1250 - 100, 320), (200, 60), (0, 255, 0), (0, 200, 0), (0, 255, 0), FONT.render("Save", 1, BLACK), (0, 0), 5, BLACK)
    resolution_text = pg.TextInput((1250 - 100, 650), (200, 50), WHITE, label="Resolution")
    run = True
    while run:
        clock.tick(FPS)
        events = pygame.event.get()
        draw_window(win, width, height, image, open_button, pixel_button, save_button, events)
        image.update(win, events)
        if open_button.clicked:
            image.change_image(askopenfilename())
        if pixel_button.clicked:
            try:
                res = int(resolution_text.text)
                image.pixelate(res)
            except ValueError:
                resolution_text.input_string = "200"
                image.pixelate(200)

        if save_button.clicked:
            image.save(askdirectory())
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                # exit()
        resolution_text.Draw(win, events)

        pygame.display.update()


main(WINDOW, WIDTH, HEIGHT)
