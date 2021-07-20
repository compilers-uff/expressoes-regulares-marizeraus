import ply.lex as lex

tokens = [
    'WORD'
] 

t_ignore  = ' \t\n'

def t_WORD(t):
    r'[a-zA-Z0-9,]+'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])

class Lexer:
    def __init__(self):
        self.lexer = lex.lex()

    def setData(self, data):
        self.data = data
        self.lexer.input(data)
        
    def tokenize(self):
        tokens = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break      
            tokens.append(tok)
        return tokens
    
if __name__ == '__main__':
    lex = Lexer()
    lex.setData("Ola mundo")
    t = lex.tokenize()
    print(t)
