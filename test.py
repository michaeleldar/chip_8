import os

pixels = []
# symbols: ⬛ ⬜
for x in range(0, 2048):
    pixels.append("⬛")


def update_screen():
    os.system("clear")
    rowid = 0
    for pixel in pixels:
        rowid = rowid + 1
        if rowid == 64:
            print(pixel, end="\n")
            rowid = 0
        else:
            print(pixel, end="")


update_screen()
