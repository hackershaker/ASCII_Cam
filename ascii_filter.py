import cv2 as cv
from PIL import Image, ImageFont, ImageDraw
import numpy as np

from filter import Filter
from util import measure_method_time


class AsciiFilter(Filter):
    def __init__(self):
        self.density = "Ñ@#W$9876543210?!abc;:+=-,._ "
        self.ascii_resolution = (50, 50)
        self.fontsize = 10

    def setResolution(self, cam, width, height):
        cam.set(3, width)
        cam.set(4, height)

    def filter(self, frame):
        return self._filter(frame, self.ascii_resolution)

    @measure_method_time
    def _filter(self, frame, size):
        frame = cv.resize(frame, size)
        cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # print(len(frame), len(frame[0]))
        fnt = ImageFont.truetype("arial.ttf", self.fontsize)
        img = Image.new(
            "L", (size[0] * self.fontsize, size[1] * self.fontsize), color="black"
        )
        draw = ImageDraw.Draw(img)

        for i in range(size[0]):
            for j in range(size[1]):
                light = self.density[
                    int(sum(frame[i][j]) / (256 * 3) * len(self.density))
                ]
                draw.text(
                    (j * self.fontsize, i * self.fontsize),
                    light,
                    fill="white",
                    font=fnt,
                    spacing=0,
                    align="center",
                )

        img = np.array(img)
        return img
