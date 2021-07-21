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
    r'\n\n'
    return t

def t_HEADER(t):
    r'\#+.+'
    return t

def t_ENUM(t): 
    r'1\..+'
    return t

def t_ITEM(t):
    r'\-.+'
    return t

def t_WORD(t):
    r'[a-zA-Z0-9,]+'
    return t

def t_BOLD(t):
    r'\*\*[a-zA-Z0-9,\.]*\*\*'
    return t

def t_ITALIC(t):
    r'\_[a-zA-Z0-9,\.]*\_'
    return t

def t_LINK(t):
    r'\[.*\]\(.*\)'
    return t

def t_NEWLINE(t):
    r'\n'
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
    enumstart = False
    itemstart = False
    for t in tl:
        if t.type == 'ITEM':
            if(not itemstart):
                html +="\n<ul>\n"
                itemstart = True
            html +="<li>" + t.value.split("-")[1][1:]
        elif itemstart and t.type =='PARAGRAPH':
            itemstart = False
            html += "\n</ul>"
        if t.type == 'ENUM':
            if(not enumstart):
                html +="\n<ol>\n"
                enumstart = True
            html +="<li>" + t.value.split("1.")[1][1:]
        elif enumstart and t.type =='PARAGRAPH':
            enumstart = False
            html += "\n</ol>"
        if t.type == 'HEADER':
            hv = t.value.count("#")
            parts = t.value.split()
            for part in parts:
                if(part.startswith("#")):
                    html += "\n<h" + str(hv) + ">"
                else:
                    html += part + " "
            html += "</h" + str(hv) + ">"
            pass
        if t.type == 'NEWLINE':
            html +="\n"
        if t.type == 'PARAGRAPH':
            html +="\n<p>"
            pass
        if t.type == 'WORD':
            html += t.value + " "
            pass
        if t.type == 'BOLD':
            html += "<strong>" + t.value[2:-2] + "</strong>"
            pass
        if t.type == 'ITALIC':
            html += "<em>" + t.value[1:-1] + "</em>"
            pass
        if t.type == 'LINK':
            parts = t.value.split("]")
            name = parts[0][1:]
            url = parts[1][1:-1]
            html += '<a href="' + url + '">'
            html += name + "</a>"
    html += "</html>"        
    return html

import sys
if __name__ == '__main__':
    lex = MDLexer()
    lex.setData(open(sys.argv[1], "r").read())
    t = lex.tokenize()
    print(toHtml(t))
