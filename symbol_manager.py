class SymbolManager:
    symbols: dict[str, int]

    def __init__(self):
        self.symbols = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'SCREEN': 0x4000,
            'KBD': 0x6000
        }
        for i in range(0, 15):
            self.symbols[f'R{i}'] = i

    def register_symbol(self, symbol: str, address: int = -1):
        if (symbol not in self.symbols) or (self.symbols[symbol] is -1):
            # never overwrite label(instruction) address
            self.symbols[symbol] = address

    def address_resolution(self):
        address = 16
        for symbol in self.symbols:
            if self.symbols[symbol] != -1:
                continue
            self.symbols[symbol] = address
            address += 1

    def get_int_address(self, symbol: str) -> int:
        return self.symbols[symbol]