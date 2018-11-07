
# -----------------------------------------------------------------------------
# parser.py
# A parser for the P++ Language.
# -----------------------------------------------------------------------------
import ply.yacc as yacc

#token map
from lexer import tokens

def p_variable_assignment(p):
    'expresion : ID ASSIGN Operation COLON Function LPAREN ParameterList RPAREN Location END'
def p_appending(p):
    'expression : APPEND ID TO ID END'
def p_rotating(p):
    'expression : ROTATE ID AROUND ID END'
def p_param_list(p):
    """ParameterList : Parameter AND ParameterList 
                     | Parameter 
                     | empty """
def p_parameter(p):
    """Parameter : ID ASSIGN DIGIT 
                 | ID ASSIGN String"""
def p_string(p) :
    'String : QUOTE ID QUOTE'
def p_operation(p):
    'Operation : DRAW'
def p_function(p):
    """Function : SIN 
                | CIRCLE 
                | GRID 
                | LINE """
def p_idlist(p):
    """IdList : ID AND IdList 
              | ID"""
def p_location(p):
    'Location : REGARDING Coordinate'
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

while True:
   try:
       s = '''
draw:Sine(amplitude = 9, frequency = 100, color = "blue", line = dot);
draw:Circle(radius = 5, color = "red");
draw:Grid(x=300 , y = 300);
draw:Line(@A);

'''
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

