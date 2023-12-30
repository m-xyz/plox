from token_type import TokenType
from ttoken import Token

class Scanner:
    _tokens = []
    _start = 0
    _current = 0
    _line = 1

    def __init__(self, source: str):
        self.source = source
        self.N = len(source)

    def scan_tokens(self):
        while not self.at_end():
            self.start = self._current
            self.scan_token()
        self._tokens.append(Token(TokenType.EOF, "", None, self._line))
        
        return self._tokens

    def scan_token(self):
        c = self.advance()

        match c:
            case '(': self.add_token(TokenType.LEFT_PAREN, None)
            case ')':self.add_token(TokenType.RIGHT_PAREN, None)
            case '{':self.add_token(TokenType.LEFT_BRACE, None)
            case '}':self.add_token(TokenType.RIGHT_BRACE, None)
            case ',':self.add_token(TokenType.COMMA, None)
            case '.':self.add_token(TokenType.DOT, None)
            case '-':self.add_token(TokenType.MINUS, None)
            case '+':self.add_token(TokenType.PLUS, None)
            case ';':self.add_token(TokenType.SEMICOLON, None)
            case '*':self.add_token(TokenType.STAR, None)
            case '!':self.add_token(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG, None)
            case '=':self.add_token(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL, None)
            case '<':self.add_token(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS, None)
            case '>':self.add_token(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER, None)
            case '/':
                if(match('/')):
                    # See where the comment ends
                    while(self.peek() != '\n' and not self.at_end()): self.advance()
                else: self.add_token(TokenType.SLASH, None)
            case  _ :
                print(f"error -> {c}\n")
                #Plox.error(self._line, "Unexpected character.")

    def match(self, expected: str):
        if(self.at_end()): return False
        if(self.source[self._current] != expected): return False
        self._current += 1

        return True

    def advance(self):
        r = self.source[self._current]
        self._current += 1

        return r

    def peek(self):
        if(self.at_end()): return '\0'

        return self.source[self._current]

    def add_token(self, ttype: TokenType, literal: object):
        text = self.source[self._start:self._current]
        self._tokens.append(Token(ttype, text, literal, self._line))

    def at_end(self): return self._current >= self.N
