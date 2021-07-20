# ------------------------------------------------------------
# Simple markdown lexer
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   
tokens = [
    'HEADER',
    'WORD',
    'BOLD',
    'ITALIC',
    'NEWLINE',
    'LINK',
    'ENUM',
    'ITEM',
    'PARAGRAPH'
] 

# A string containing ignored characters (spaces, tabs and newline)
t_ignore  = ' '

def t_PARAGRAPH(t):
    r''
    return t

def t_HEADER(t):
    r ''
    return t

def t_ENUM(t):
    r''
    return t

def t_ITEM(t):
    r''
    return t

def t_WORD(t):
    r''
    return t

def t_BOLD(t):
    r''
    return t

def t_ITALIC(t):
    r''
    return t

def t_LINK(t):
    r''
    return t

def t_NEWLINE(t):
    r''
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])

class MDLexer:
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
                break      # No more input
            tokens.append(tok)
        return tokens

def toHtml(tl):
    html = "<html>"
    for t in tl:
        if t.type == 'ITEM':
        if t.type == 'ENUM':
        if t.type == 'HEADER':
        if t.type == 'NEWLINE':
        if t.type == 'PARAGRAPH':
        if t.type == 'WORD':
        if t.type == 'BOLD':
        if t.type == 'ITALIC':
        if t.type == 'LINK':
    html += "\n</html>"        
    return html

import sys
if __name__ == '__main__':
    lex = MDLexer()
    lex.setData(open(sys.argv[1], "r").read())
    t = lex.tokenize()
    print(toHtml(t))
