import re
from enum import Enum, auto


class TokenType(Enum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    NUMBER = auto()
    SYMBOL = auto()
    STRING = auto()
    NEWLINE = auto()
    INPUT = auto()
    EOF = auto()


TOKEN_PATTERNS = [
    (r"LET|IF|THEN|ELSE|END|FOR|NEXT|GOTO|GOSUB|RETURN|REM|INPUT", TokenType.KEYWORD),
    (r"[A-Za-z_][A-Za-z0-9_]*", TokenType.IDENTIFIER),
    (r"\d+(\.\d+)?", TokenType.NUMBER),
    (r"[\+\-\*\/\=\>\<\!$$\,\:\;]", TokenType.SYMBOL),
    (r"\".*?\"", TokenType.STRING),
    (r"\n", TokenType.NEWLINE),
    (r"\s+", None),  # Ignore whitespace characters
]

TOKEN_TYPE_NAMES = {token_type: token_type.name for token_type in TokenType}


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({TOKEN_TYPE_NAMES[self.type]}, {self.value})"


class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.tokens = []

    def lex(self):
        while self.pos < len(self.code):
            match = None
            for pattern, token_type in TOKEN_PATTERNS:
                match = re.match(pattern, self.code[self.pos :])
                if match:
                    if token_type is not None:
                        token = Token(token_type, match.group())
                        self.tokens.append(token)
                    self.pos += len(match.group())
                    break
            if not match:
                raise Exception(f"Invalid character at position {self.pos}")
        self.tokens.append(Token(TokenType.EOF, "EOF"))
        return self.tokens


code = """
10 LET x = 5
20 IF x > 10 THEN GOTO 30
30 PRINT "Hello, World!"
40 END
"""
lexer = Lexer(code)
tokens = lexer.lex()
for token in tokens:
    if token.type != TokenType.NEWLINE:
        print(token)
