
# -----------------------------------------------------------------------------
# parser.py
# A parser for the P++ Language.
# -----------------------------------------------------------------------------
import ply.yacc as yacc

#token map
from lexer import tokens

def p_expression_ID(p):
    """expresion : ID ASSIGN Operation COLON Function LPAREN ParameterList RPAREN Location END
                 | APPEND ID TO ID END
                 | ROTATE ID AROUND ID END"""
    if p[1] == 'append'     : p[0] = p[0]
    elif p[1] == 'rotate'   : p[0] = p[0]
    else                    : p[0] = p[0]
    print (*p)


def p_param_list(p):
    """ParameterList : Parameter AND ParameterList 
                     | Parameter 
                     | empty"""
def p_parameter(p):
    """Parameter : ID ASSIGN DIGIT 
                 | ID ASSIGN String
                 | LINE ASSIGN String """
def p_string(p) :
    'String : QUOTE ID QUOTE'
    p[0] = p[1]
def p_operation(p):
    'Operation : DRAW'
    p[0] = "draw"
def p_function(p):
    """Function : SIN 
                | CIRCLE 
                | GRID 
                | LINE"""
    if p[1] == 'sin' : p[0] = 'sin'
    elif p[1] == 'circle' : p[0] = 'circle'
    elif p[1] == 'grid' : p[0] = 'grid'
    elif p[1] == 'line' : p[0] = 'line'
    

def p_location(p):
    """Location : REGARDING Coordinate
                | empty"""
    print(*p)
    p[0] = p[1] + ' ' + p[2]
def p_coordinate(p):
    """Coordinate : ID 
                  | LPAREN DIGIT COMMA DIGIT RPAREN"""
    print(*p)
    p[0] = p[1]
def p_empty(p):
    'empty :'
    pass
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

s = '''A = draw : sin (color = "blue") @ a ; 
'''

result = parser.parse(s)
print(result)

