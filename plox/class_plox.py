import tokenize
from scanner import Scanner

class Plox:
    broke = False

    def error(self, line: int, msg: str): self.report(line, "", msg)

    def report(self, line: int, where: str, msg: str):
        print(f"[LINE {line}] Error {where}: {msg}")
        self.broke = True

    def run(self, src: str):
        """
        Syntax error handling happens here
        """
        scanner = Scanner(src)
        tokens = scanner.scan_tokens()

    def run_file(self, path: str):
        try:
            with tokenize.open(path) as file:
    #            bytes_data = file.read()
                tkns = tokenize.generate_tokens(file.readline)
                self.run([t.string for t in tkns])
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
