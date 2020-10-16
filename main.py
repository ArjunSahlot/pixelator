import pygame
import os
from Pixelator.constants import *
from Pixelator.classes import Image
from pumpkinpy import pygame as pg
from tkinter.filedialog import askdirectory, askopenfilename


# Window Management
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_width//2-WIDTH//2, screen_height//2-HEIGHT//2)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixelator, By: Arjun Sahlot")


def draw_window(win, width, height, image, open_button, pixel_button, save_button):
    win.fill(WHITE)
    win.fill(GREY, (950, 0, 550, HEIGHT))
    file_name = image.path.split("/")
    if len(file_name) == 1:
        file_name = "".join(file_name).split("\\")
    file_name = file_name[-1]
    text = FONT.render(file_name if file_name != "starter_image.png" else "None", 1, BLACK if file_name != "starter_image.png" else RED)
    win.blit(text, (1250 - text.get_width()//2, 25))
    open_button.Draw(win)
    pixel_button.Draw(win)
    save_button.Draw(win)


def main(win, width, height):
    clock = pygame.time.Clock()
    image = Image(os.path.join("assets", "starter_image.png"), 50, 50)
    open_button = pg.Button((1250 - 100, 100), (200, 60), FONT, "Open", GREEN, borderThickness=5)
    pixel_button = pg.Button((1250 - 125, 200), (250, 80), B_FONT, "Pixelate", GREEN, borderThickness=5)
    save_button = pg.Button((1250 - 100, 320), (200, 60), FONT, "Save", GREEN, borderThickness=5)
    resolution_text = pg.TextInput((1250 - 100, 650), (200, 50), initial_string="Resolution")
    typing = False
    run = True
    while run:
        clock.tick(FPS)
        draw_window(win, width, height, image, open_button, pixel_button, save_button)
        events = pygame.event.get()
        image.update(win, events)
        if open_button.Clicked():
            image.change_image(askopenfilename())
        if pixel_button.Clicked():
            try:
                res = int(resolution_text.get_text())
                image.pixelate(res)
            except ValueError:
                resolution_text.input_string = "200"
                image.pixelate(200)

        if save_button.Clicked():
            image.save(askdirectory())
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                # exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resolution_text.rect.collidepoint(event.pos):
                    typing = True
                    if resolution_text.get_text() == "Resolution":
                        resolution_text.clear_text()
                else:
                    typing = False
                    if resolution_text.get_text() == "":
                        resolution_text.input_string = "Resolution"

        resolution_text.update(events, typing)
        resolution_text.draw(win)

        pygame.display.update()


main(WINDOW, WIDTH, HEIGHT)
