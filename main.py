import re
from enum import Enum, auto
from pathlib import Path


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


def lex(source: str):
    pos = 0
    tokens = []
    while pos < len(source):
        match = None
        for pattern, token_type in TOKEN_PATTERNS:
            match = re.match(pattern, source[pos:])
            if match:
                if token_type == TokenType.KEYWORD and match.group() == "REM":
                    end = source[pos:].find("\n")
                    token = Token(token_type, source[pos:end])
                    tokens.append(token)
                    pos += end - pos
                    break
                if token_type is not None:
                    token = Token(token_type, match.group())
                    tokens.append(token)
                pos += len(match.group())
                break
        if not match:
            raise Exception(f"Invalid character at position {pos}")
    tokens.append(Token(TokenType.EOF, "EOF"))
    return tokens


def main():
    try:
        code = Path("guessing_game.bas").read_text()
        tokens = lex(code)
        for token in tokens:
            if token.type != TokenType.NEWLINE:
                print(token)
    except FileNotFoundError as e:
        print(f"Error: File '{e.filename}' not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
