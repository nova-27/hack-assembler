from assembler import Assembler

if __name__ == '__main__':
    file = open('test.asm', 'r')
    assembler = Assembler(file.readlines())
    assembler.parse_all()
    print(assembler.to_binary_all())