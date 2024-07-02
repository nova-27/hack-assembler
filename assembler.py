from instruction_parser import InstructionParser


class Assembler:
    instructions: list[InstructionParser]

    def __init__(self, lines: list[str]):
        self.instructions = []
        for line in lines:
            comment_index = line.find('//')
            instruction = line
            if comment_index != -1:
                instruction = line[:comment_index]
            instruction = instruction.strip()
            if len(instruction) > 0:
                self.instructions.append(InstructionParser(instruction))

    def parse_all(self):
        for instruction in self.instructions:
            instruction.parse()

    def to_binary_all(self) -> list[str]:
        return [instruction.to_binary() for instruction in self.instructions]

