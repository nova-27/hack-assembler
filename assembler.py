from instruction_parser import InstructionParser


class Assembler:
    instructions: list[InstructionParser]

    def __init__(self, lines: list[str]):
        self.instructions = [InstructionParser(line) for line in lines]

    def parse_all(self):
        for instruction in self.instructions:
            instruction.parse()

    def to_binary_all(self) -> list[str]:
        return [instruction.to_binary() for instruction in self.instructions]

