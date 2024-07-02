from assembler import Assembler
import sys

if __name__ == '__main__':
    asm_filename = sys.argv[1]
    asm_file = open(asm_filename, 'r')
    assembler = Assembler(asm_file.readlines())
    assembler.parse_all()

    export_filename = asm_filename[:asm_filename.rfind('.')] + '.hack'
    export_file = open(export_filename, 'w')
    export_data = "\n".join(assembler.to_binary_all())
    export_file.write(export_data)