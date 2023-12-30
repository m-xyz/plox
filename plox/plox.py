#! /usr/bin/env python3
import sys
from class_plox import Plox

if __name__ == "__main__":
    plox = Plox()
            
    if(len(sys.argv) > 2):
        print("Usage: plox [script]\n")
        exit(64)
    elif(len(sys.argv) == 2): plox.run_file(sys.argv[1])
    else:
        try: plox.run_prompt()
        except EOFError: print("\nBye!\n")
