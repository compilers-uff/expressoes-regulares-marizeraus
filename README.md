# MD para HTML

Trabalho para a disciplina de Linguagens Formais, 2021.1

Data de entrega: 23/07/21

## Objetivo

Exercitar o uso de expressões regulares.

## Tarefa

Implementar um tradutor de uma simplificação da linguagem Markdown para HTML em Python 3 utilizndo o pacote PLY.

## Preparação

* Instale Python 3 com o pacote PLY. 
  - Com Python 3 instalado no seu sistema, execute `$ pip3 install PLY`.

## A linguagem Markdown simplificada e sua tradução à HTML

- Permite a escrita de documentos como por exemplo:
```
# Teste header 1

## Teste header 2

**teste** **bold**

_teste_ _italico_

- teste itemizacao 1
- teste itemizacao 2

1. teste enumeracao 1
1. teste enumeracao 2

teste paragrafo 1, teste paragrafo 2

[teste link Google](http://www.google.com)
```

- A tradução para HTML deve produzir:
```
<html>
<h1>Teste h1 </h1>
<p>
<h2>Teste h2 </h2>
<p><strong>teste</strong> <strong>bold</strong>
<p><em>teste</em> <em>italico</em>
<p>
<ul>
<li>teste itemizacao 1 </li>
<li>teste itemizacao 2 </li>
</ul>
<p>
<ol>
<li>teste enumeracao 1 </li>
<li>teste enumeracao 2 </li>
</ol>
<p>teste paragrafo 1, teste paragrafo 2
<p><a href="http://www.google.com">teste link Google</a>
</html>
```

- Os elementos de Markdown simplificado são
1. Headers: linhas começadas com `#`. A tradução de `#` para HTML é `h1`, de `##` é `h2` e assim sucessivamente.
2. Palavras em negrito e itálico. O texto `**texto**` é traduzido em `<b>texto</b>` e `_texto_`.
3. Parágrafos. Uma linha em branco inicia um parágrafo. 
4. Itemizações. Linhas iniciadas com `-` determinam um item numa lista não-ordenada em HTML. Por exemplo, o texto Markdown abaixo     
   ```
   - Isto é um item.
   - E isto também.
   ``` 
   deve ser traduzido ao código HTML abaixo.
   ```
   <ul>
   <li>Isto é um item.
   <li>E isto também.
   </ul>
   ```
5. Enumerações. Linhas iniciadas com `1.` determinam um item numa lista ordenada em HTML. Por exemplo, o texto Markdown abaixo     
   ```
   1. Isto é um item.
   1. E isto também.
   ``` 
   deve ser traduzido ao código HTML abaixo.
   ```
   <ol>
   <li>Isto é um item.
   <li>E isto também.
   </ol>
   ```
6. Links. Um link em Markdown simplificado `[Google](http://www.google.com)` deve ser traduzido à `<a href="http://www.google.com">Google</a>`.

## Um exemplo

- O tradutor deve ser implementado em Python 3 utilizando a biblioteca PLY. Ela implementa analisadores léxicos através de expressões regulares e analisadores sintáticos através de gramática livres de contexto. Para este trabalho utilizaremos somente o suporte à análise léxica.

- Os principais elementos do analisador são a lista de tokens e as regras que definem as expressões regulares e que darão origem aos lexemas. No exemplo abaixo há somente um token chamado `WORD` e a expressão regular que reconhece `WORD` é dada por repetições de caracters, números e `,`, indefinidamente. A função principal cria o lexer e o invoca com a string `Ola mundo`. O resultado é o seguinte:
`[LexToken(WORD,'Ola',1,0), LexToken(WORD,'mundo',1,4)]`.

```python3
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
```

## Implementação

1. Seu analisador léxico deve definir os seguintes tokens.
```python
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
```
1. Para cada token deve haver uma regra que define uma expressão regular que reconheça o token associado segundo a definição informal acima.
2. Voce deve definir também a função `toHtml` que dada uma lista de tokens produza uma string contendo a tradução de Markdwon simplificado para HTML. A estrutura da função é a seguinte, que basicamente acumula a tradução de cada token à HTML na variável `html` e depois a retorna.
```python
def toHtml(tl):
    html = "<html>"
    # ...
    for t in tl:
        if t.type == 'ITEM':
            # ...
            html += # ...
        if t.type == 'ENUM':
            # ...           
            html += # ...
        if t.type == 'HEADER':
            # ...
            html += # ...
        if t.type == 'PARAGRAPH':
            # ...
            html += # ...
        if t.type == 'WORD':
            # ...
            html += # ...
        if t.type == 'BOLD':
            # ...
            html += # ...
        if t.type == 'ITALIC':
            # ...
            html += # ...
        if t.type == 'LINK':
            # ...
            html += # ...
    html += "\n</html>"
    return html
```
1. Se a maioria dos tokens têm uma tradução quase literal à HTML, cuidado particular deve ser tomado com relação as itemizações e enumerações. Não é possível escrever uma expressão regular que capture todas as itemizações (ou enumerações) de uma vez pois este problema se reduz ao problema do balanceamento de parênteses que não é regular. (Veremos isso ao falarmos do lema do bombeamento para linguagens regulares.)
2. Sua implementação deve refinar o arquivo `mdlexer.py` no repositório e sua execução passando o arquivo `teste.md` como parâmetro deve produzir o código HTML acima na saída padrão do sistema, quando executado de um console.

Boa sorte e divirtam-se!
