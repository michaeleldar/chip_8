from os import system
from math import floor


class Renderer:
    def __init__(self):
        self.cols = 64
        self.rows = 32
        self.display = []
        for x in range(0, 2048):
            self.display.append(0)

    def setPixel(self, x, y):
        if x > self.cols:
            x = x - self.cols
        elif x < 0:
            x = x + self.cols

        if y > self.rows:
            y = y - self.rows
        elif y < 0:
            y = y + self.rows
        pixelLoc = x + (y * self.cols)
        self.display[pixelLoc] ^= 1
        return not self.display[pixelLoc]

    def clear(self):
        self.display = []
        for x in range(0, 2048):
            self.display.append(0)

    def render(self):
        system("clear")
        ctr = 0
        for i in range(0, 2048):
            ctr = ctr + 1
            x = i % self.cols
            y = floor(i / self.cols)
            if self.display[i]:
                if ctr == 64:
                    ctr = 0
                    print("⬜", end="\n")
                else:
                    print("⬜", end="")
            else:
                if ctr == 64:
                    ctr = 0
                    print("⬛", end="\n")
                else:
                    print("⬛", end="")

    def testRender(self):
        self.setPixel(0, 0)
        self.setPixel(5, 2)
