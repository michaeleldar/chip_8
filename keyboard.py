from pynput import keyboard


class Keyboard:
    def on_press(key):
        if key == keyboard.Key.esc:
            quit()
        try:
            k = key.char
        except:
            k = key.name

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
