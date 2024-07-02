from instruction_parser import InstructionParser

if __name__ == '__main__':
    parser = InstructionParser("@2")
    parser.parse()
    print(parser.to_binary())