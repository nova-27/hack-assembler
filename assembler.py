from instruction_parser import InstructionParser
from symbol_manager import SymbolManager


class Assembler:
    instructions: list[InstructionParser]
    symbol_manager: SymbolManager

    def __init__(self, lines: list[str]):
        self.instructions = []
        self.symbol_manager = SymbolManager()

        instruction_address = 0
        for line in lines:
            normalized_line = self._normalize_line(line)
            if not normalized_line:
                continue
            if normalized_line[0] == '(':
                # label symbol
                label = normalized_line[1:-1]
                self.symbol_manager.register_symbol(label, instruction_address)
            else:
                # instruction
                self.instructions.append(InstructionParser(normalized_line, self.symbol_manager))
                instruction_address += 1

    @staticmethod
    def _normalize_line(line: str) -> str:
        """
        Delete comments and strip whitespace
        """
        comment_index = line.find('//')
        if comment_index != -1:
            line = line[:comment_index]
        return line.strip()

    def parse_all(self):
        for instruction in self.instructions:
            instruction.parse()

    def to_binary_all(self) -> list[str]:
        self.symbol_manager.address_resolution()
        return [instruction.to_binary() for instruction in self.instructions]

