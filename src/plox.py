#! /usr/bin/env python3
import sys
import argparse
from class_plox import Plox

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="PLOX", description="Lox interpreter written in Python.")
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('-f', help="Path to source file.")
    args = vars(parser.parse_args())

    plox = Plox()
    plox.DEBUG = args['debug']
            
    if(args['f']): plox.run_file(args['f'])
    else:
        try: plox.run_prompt()
        except EOFError: print("\nBye!\n")
