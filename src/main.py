import os
import sys
from Parser import *

if __name__ == "__main__":
    parser = Parser(os.path.abspath(sys.argv[1]))
    try:
        print(parser.parseFile())
    except Exception as e:
        print(e)
        exit()
