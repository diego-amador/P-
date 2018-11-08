
# -----------------------------------------------------------------------------
# parser.py
# A parser for the P++ Language.
# -----------------------------------------------------------------------------
import ply.yacc as yacc

#token map
from lexer import tokens

def p_expression(p):
    """expresion : ID ASSIGN Operation COLON Function LPAREN ParameterList RPAREN Location END
                 | APPEND ID TO ID END
                 | ROTATE ID AROUND ID END"""
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
def p_operation(p):
    'Operation : DRAW'
def p_function(p):
    """Function : SIN 
                | CIRCLE 
                | GRID 
                | LINE"""

def p_location(p):
    """Location : REGARDING Coordinate
                | empty"""
def p_coordinate(p):
    """Coordinate : ID 
                  | LPAREN DIGIT COMMA DIGIT RPAREN"""
def p_empty(p):
    'empty :'
    pass
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

s = '''A = draw:sin(amplitude = 9 and frequency = 100 and color = "blue" and line = "dot"); 
B = draw:circle(radius = 5 and color = "red"); 
C = draw:grid(x=300 and y = 300); 
D = draw:line()@A;
'''


result = parser.parse(s)
print(result)

