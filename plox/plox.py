#! /usr/bin/env python3
import sys
import tokenize

class Plox:
    broke = False

    def error(self, line: int, msg: str): report(line, "", msg)

    def report(self, line: int, where: str, msg: str):
        print(f"[LINE {line}] Error {where}: {msg}")
        self.broke = True

    def run(self, src: str):
        # Placeholder
        for t in src: print(t)

    def run_file(self, path: str):
        try:
            with tokenize.open(path) as file:
    #            bytes_data = file.read()
                tkns = tokenize.generate_tokens(file.readline)
                self.run(tkns)
            file.close()
            if(self.broke): exit(65)
    #        run(bytes_data.decode())
        except Exception as e:
            print(f"{e}\n")

    def run_prompt(self):
        try:
            while 1:
                stream_reader = input("> ")
                if(stream_reader == None): break
                self.run(stream_reader)
                self.broke = False
        except KeyboardInterrupt:
            print(f"\nKeyboardInterrupt\n")

plox = Plox()
        
if(len(sys.argv) > 2):
    print("Usage: plox [script]\n")
    exit(64)
elif(len(sys.argv) == 2): plox.run_file(sys.argv[1])
else:
    try: plox.run_prompt()
    except EOFError: print("\nBye!\n")


