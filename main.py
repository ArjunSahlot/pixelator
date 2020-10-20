import pygame
import os
from Pixelator.constants import *
from Pixelator.classes import Image
from pumpkinpy.pygameutils import elements as pg
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
    open_button = pg.ButtonText((1250 - 100, 100), (200, 60), (0, 255, 0), (0, 200, 0), (0, 255, 0), FONT.render("Open", 1, BLACK), (0, 0), 5, BLACK)
    pixel_button = pg.ButtonText((1250 - 125, 200), (250, 80), (0, 255, 0), (0, 200, 0), (0, 255, 0), B_FONT.render("Pixelate", 1, BLACK), (0, 0), 5, BLACK)
    save_button = pg.ButtonText((1250 - 100, 320), (200, 60), (0, 255, 0), (0, 200, 0), (0, 255, 0), FONT.render("Save", 1, BLACK), (0, 0), 5, BLACK)
    resolution_text = pg.TextInput((1250 - 100, 650), (200, 50), initialText="Resolution")
    typing = False
    run = True
    while run:
        clock.tick(FPS)
        draw_window(win, width, height, image, open_button, pixel_button, save_button)
        events = pygame.event.get()
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resolution_text.rect.collidepoint(event.pos):
                    if resolution_text.text == "Resolution":
                        resolution_text.ClearText()
                else:
                    if resolution_text.text == "":
                        resolution_text.input_string = "Resolution"

        resolution_text.Update(events)
        resolution_text.Draw(win)

        pygame.display.update()


main(WINDOW, WIDTH, HEIGHT)
