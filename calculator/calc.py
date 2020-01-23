from module.parser import parser
import sys

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)