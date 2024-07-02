from assembler import Assembler

if __name__ == '__main__':
    assembler = Assembler(['@2'])
    assembler.parse_all()
    print(assembler.to_binary_all())