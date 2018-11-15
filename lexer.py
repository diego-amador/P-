
# -----------------------------------------------------------------------------
# lexer.py
# A lexer for the P++ Language.
# -----------------------------------------------------------------------------

import ply.lex as lex
# List of token names.   This is always required
tokens = (
    'ID',
    'CHARACTER',
    'DIGIT',
    'COLON',
    'ASSIGN',
    'SEMIC',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'REGARDING',
    'COMMA',
    'DOT',
    'OPERATOR', 
    'QUOTE', 
    'DRAW',
    'APPEND',
    'TO',
    'ROTATE',
    'AROUND',
    'AND',
    'SIN',
    'CIRCLE',
    'GRID',
    'LINE',
    'START',
    'END'
)

# Regular expression rules for simple tokens
t_CHARACTER    = r'[a-zA-z_]'
t_COLON = r'\:'
t_ASSIGN = r'\='
t_SEMIC = r'\;'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_REGARDING = r'\@'
t_COMMA = r'\,'
t_DOT = r'\.'
t_OPERATOR  = r'[\+\-\*]'
t_QUOTE = r'\"'

def t_DIGIT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

reserved = {
   'draw'   : 'DRAW',
   'append' : 'APPEND',
   'to'     : 'TO',
   'rotate' : 'ROTATE',
   'around' : 'AROUND',
   'and'    : 'AND',
   'sin'    : 'SIN',
   'circle' : 'CIRCLE',
   'grid'   : 'GRID',
   'line'   : 'LINE',
   'start'  : 'START',
   'end'    : 'END'
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

t_ignore  = ' \t\n'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''append A to B ;
'''
"""
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
"""