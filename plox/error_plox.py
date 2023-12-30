class PloxError:
    def __init__(self, line: int, msg: str, where: str):
        self.line = line
        self.msg = msg
        self.where = where

    def report(self): print(f"[LINE {self.line}] Error {self.where}: {self.msg}")
