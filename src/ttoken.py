class Token:
    def __init__(self, ttype: str, lexeme: str, literal: object, line: int):
        self.ttype = ttype
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __repr__(self):
        return f"({self.ttype}, \'{self.lexeme}\', {self.literal}, {type(self.literal)})"
