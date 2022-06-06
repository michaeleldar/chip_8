class CPU:
    def __init__(self, renderer, keyboard):
        self.renderer = renderer
        self.keyboard = keyboard

        self.memory = []  # 4096 byte memory
        for x in range(0, 4096):
            self.memory.append(0)
        self.v = []  # 16 8-bit registers
        for x in range(0, 16):
            self.v.append(0)
        self.i = 0

        self.delayTimer = 0

        self.pc = 0x200

        self.stack = []

        self.paused = False

        self.speed = 10

    def loadSpritesIntoMemory(self):
        sprites = [
            0xF0,
            0x90,
            0x90,
            0x90,
            0xF0,
            0x20,
            0x60,
            0x20,
            0x20,
            0x70,
            0xF0,
            0x10,
            0xF0,
            0x80,
            0xF0,
            0xF0,
            0x10,
            0xF0,
            0x10,
            0xF0,
            0x90,
            0x90,
            0xF0,
            0x10,
            0x10,
            0xF0,
            0x80,
            0xF0,
            0x10,
            0xF0,
            0xF0,
            0x80,
            0xF0,
            0x90,
            0xF0,
            0xF0,
            0x10,
            0x20,
            0x40,
            0x40,
            0xF0,
            0x90,
            0xF0,
            0x90,
            0xF0,
            0xF0,
            0x90,
            0xF0,
            0x10,
            0xF0,
            0xF0,
            0x90,
            0xF0,
            0x90,
            0x90,
            0xE0,
            0x90,
            0xE0,
            0x90,
            0xE0,
            0xF0,
            0x80,
            0x80,
            0x80,
            0xF0,
            0xE0,
            0x90,
            0x90,
            0x90,
            0xE0,
            0xF0,
            0x80,
            0xF0,
            0x80,
            0xF0,
            0xF0,
            0x80,
            0xF0,
            0x80,
            0x80,
        ]

        for i in range(0, sprites.__len__()):
            self.memory[i] = sprites[i]

    def loadProgramIntoMemory(self, program):
        for loc in range(0, program.__len__()):
            self.memory[0x200 + loc] = program[loc]

    def loadRom(self, romName):
        rom = open("roms/" + romName, "r")
