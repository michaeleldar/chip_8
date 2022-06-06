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
        self.loadProgramIntoMemory(rom.read())
        rom.close()

    def cycle(self):
        for i in range(0, self.speed):
            if not self.paused:
                opcode = self.memory[self.pc] << 8 | self.memory[self.pc + 1]
                self.executeInstruction(opcode)

        if not self.paused:
            self.updateTimers()

        self.renderer.render()

    def updateTimers(self):
        if self.delayTimer > 0:
            self.delayTimer = self.delayTimer - 1

    def executeInstruction(self, opcode):
        self.pc = self.pc + 2
        x = (opcode & 0x0F00) >> 4
        y = (opcode & 0x00F0) >> 4

        if (opcode & 0xF000) == 0x0000:
            if opcode == 0x00E0:
                self.renderer.clear()

            elif opcode == 0x00EE:
                self.pc = self.stack.pop()
        elif (opcode & 0xF000) == 0x1000:
            self.pc = opcode & 0xFFF
        elif (opcode & 0xF000) == 0x2000:
            self.stack.append(self.pc)
            self.pc = opcode & 0xFFF
        elif (opcode & 0xF000) == 0x3000:
            if self.v[x] == (opcode & 0xFF):
                self.pc = self.pc + 2
        elif (opcode & 0xF000) == 0x4000:
            if self.v[x] != (opcode & 0xFF):
                self.pc = self.pc + 2
        elif (opcode & 0xF000) == 0x5000:
            if self.v[x] == self.v[y]:
                self.pc = self.pc + 2
        elif (opcode & 0xF000) == 0x6000:
            self.v[x] = opcode & 0xFF
        elif (opcode & 0xF000) == 0x7000:
            self.v[x] = self.v[x] + (opcode & 0xFF)
        elif (opcode & 0xF000) == 0x8000:
            if (opcode & 0xF) == 0x0:
                self.v[x] = self.v[y]
            elif (opcode & 0xF) == 0x1:
                self.v[x] |= self.v[y]
            elif (opcode & 0xF) == 0x2:
                self.v[x] &= self.v[y]
            elif (opcode & 0xF) == 0x3:
                self.v[x] ^= self.v[y]
            elif (opcode & 0xF) == 0x4:
                sum = self.v[x] + self.v[y]

                self.v[0xF] = 0

                if sum > 0xFF:
                    self
            elif (opcode & 0xF) == 0x5:
                pass
            elif (opcode & 0xF) == 0x6:
                pass
            elif (opcode & 0xF) == 0x7:
                pass
            elif (opcode & 0xF) == 0xE:
                pass
        elif (opcode & 0xF000) == 0x9000:
            pass
        elif (opcode & 0xF000) == 0xA000:
            pass
        elif (opcode & 0xF000) == 0xB000:
            pass
        elif (opcode & 0xF000) == 0xC000:
            pass
        elif (opcode & 0xF000) == 0xD000:
            pass
        elif (opcode & 0xF000) == 0xE000:
            if (opcode & 0xFF) == 0x9E:
                pass
            elif (opcode & 0xFF) == 0xA1:
                pass
        elif (opcode & 0xF000) == 0xF000:
            if (opcode & 0xFF) == 0x07:
                pass
            elif (opcode & 0xFF) == 0x0A:
                pass
            elif (opcode & 0xFF) == 0x15:
                pass
            elif (opcode & 0xFF) == 0x18:
                pass
            elif (opcode & 0xFF) == 0x1E:
                pass
            elif (opcode & 0xFF) == 0x29:
                pass
            elif (opcode & 0xFF) == 0x33:
                pass
            elif (opcode & 0xFF) == 0x55:
                pass
            elif (opcode & 0xFF) == 0x65:
                pass
        else:
            raise SyntaxError("Unknown opcode " + opcode)
