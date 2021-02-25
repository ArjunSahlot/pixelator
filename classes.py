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
from constants import *


class Image:
    max_width = 850

    def __init__(self, image, x, y):
        self.x, self.y = x, y
        self.active_image = self.prev_image = image if isinstance(image, pygame.Surface) else pygame.image.load(image)
        self.path = image if isinstance(image, str) else None
        self.width = max(1, min(self.max_width, self.active_image.get_width()))

    def update(self, win, events):
        self.draw(win)
        self.width = max(1, min(self.max_width, self.width))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.max_width // 2 + self.x - self.width // 2 <= x <= self.max_width // 2 + self.x - self.width // 2 + self.width and self.max_width // 2 + self.y - self.width // 2 <= y <= self.max_width // 2 + self.y - self.width // 2 + self.width:
                    if event.button == 4:
                        self.make_bigger()
                    if event.button == 5:
                        self.make_smaller()

    def change_image(self, new_image):
        try:
            self.__init__(new_image, self.x, self.y)
        except pygame.error:
            pass

    def reset_image(self):
        self.active_image = self.prev_image

    def make_smaller(self):
        self.width -= 5
        self.width = max(1, self.width)

    def make_bigger(self):
        self.width += 5
        self.width = min(self.max_width, self.width)

    def pixelate(self, resolution):
        self.active_image = pygame.transform.scale(pygame.transform.scale(self.prev_image, (resolution, resolution)), (self.width, self.width))

    def save(self, path):
        file_name = self.path.split("/")
        if len(file_name) == 1:
            file_name = "".join(file_name).split("\\")
        file_name = file_name[-1]
        pygame.image.save(self.active_image, os.path.join(path, "pixelated_" + file_name))

    def draw(self, win):
        win.blit(pygame.transform.scale(self.active_image, (round(self.width), round(self.width))), (round(self.max_width // 2 + self.x - self.width // 2), round(self.max_width // 2 + self.y - self.width // 2)))
