from ssl import OP_NO_COMPRESSION
from pynput import keyboard


class Keyboard:
    def __init__(self):
        self.KEYMAP = {
            49: 0x1,
            50: 0x2,
            51: 0x3,
            52: 0xC,
            81: 0x4,
            87: 0x5,
            69: 0x6,
            82: 0xD,
            65: 0x7,
            83: 0x8,
            68: 0x9,
            70: 0xE,
            90: 0xA,
            88: 0x0,
            67: 0xB,
            86: 0xF,
        }
        self.keysPressed = []

        self.onNextKeyPress = 0

    def on_press(self, key):
        if key == keyboard.Key.esc:
            quit()
        try:
            k = key.char
        except:
            k = key.name
        return k

    def isKeyPressed(self, keyCode):
        if self.on_press() == keyCode:
            print("False: " + keyCode)
            return True
        else:
            print("True: " + keyCode)
            return False
