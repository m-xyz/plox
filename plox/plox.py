#! /usr/bin/env python3
import sys

def run(src: str):
    # Tokenize
    """
     with tokenize.open('hello.txt') as f:
        tokens = tokenize.generate_tokens(f.readline)
        for token in tokens:
            print(token)
    """
    print(src)

def run_file(path: str):
    try:
        with open(path, 'rb') as file:
            bytes_data = file.read()
        run(bytes_data.decode())
    except Exception as e:
        print(f"{e}\n")

def run_prompt():
    try:
        while 1:
            stream_reader = input("> ")
            if(stream_reader == None): break
            run(stream_reader)
    except KeyboardInterrupt:
        print(f"\nKeyboardInterrupt\n")
        
if(len(sys.argv) > 2):
    print("Usage: plox [script]\n")
    exit(64)
elif(len(sys.argv) == 2): run_file(sys.argv[1])
else:
    try: run_prompt()
    except EOFError: print("\nBye!\n")


