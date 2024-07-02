JUMP2BIN: dict[str, int] = {
    'JGT': 0b001,
    'JEQ': 0b010,
    'JGE': 0b011,
    'JLT': 0b100,
    'JNE': 0b101,
    'JLE': 0b110,
    'JMP': 0b111
}
COMP2BIN: dict[str, int] = {
    '0':   0b0101010,
    '1':   0b0111111,
    '-1':  0b0111010,
    'D':   0b0001100,
    'A':   0b0110000,
    '!D':  0b0001101,
    '!A':  0b0110001,
    '-D':  0b0001111,
    '-A':  0b0110011,
    'D+1': 0b0011111,
    'A+1': 0b0110111,
    'D-1': 0b0001110,
    'A-1': 0b0110010,
    'D+A': 0b0000010,
    'D-A': 0b0010011,
    'A-D': 0b0000111,
    'D&A': 0b0000000,
    'D|A': 0b0010101,
    'M':   0b1110000,
    '!M':  0b1110001,
    '-M':  0b1110011,
    'M+1': 0b1110111,
    'M-1': 0b1110010,
    'D+M': 0b1000010,
    'D-M': 0b1010011,
    'M-D': 0b1000111,
    'D&M': 0b1000000,
    'D|M': 0b1010101
}
DEST2BIN: dict[str, int] = {
    'M':   0b001,
    'D':   0b010,
    'DM':  0b011,
    'A':   0b100,
    'AM':  0b101,
    'AD':  0b110,
    'ADM': 0b111
}


class InstructionParser:
    instruction: str
    address: int
    dest: int
    comp: int
    jump: int

    def __init__(self, instruction: str):
        self.instruction = instruction
        self.address = 0
        self.dest = 0
        self.comp = 0
        self.jump = 0

    def is_a_instruction(self) -> bool:
        return self.instruction[0] == '@'

    def parse(self):
        if self.is_a_instruction():
            self.address = int(self.instruction[1:])
        else:
            semi_split = self.instruction.split(';')
            if len(semi_split) >= 2:
                self.jump = JUMP2BIN[semi_split[1]]
            equal_split = semi_split[0].split('=')
            if len(equal_split) >= 2:
                self.comp = COMP2BIN[equal_split[1]]
                sorted_dest = "".join(sorted(equal_split[0]))
                self.dest = DEST2BIN[sorted_dest]
            else:
                self.comp = COMP2BIN[equal_split[0]]

    def to_binary(self) -> str:
        if self.is_a_instruction():
            return f'0{self.address:015b}'
        else:
            return f'111{self.comp:07b}{self.dest:03b}{self.jump:03b}'
