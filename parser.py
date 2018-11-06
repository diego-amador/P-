
# -----------------------------------------------------------------------------
# parser.py
# A parser for the P++ Language.
# -----------------------------------------------------------------------------
import ply.yacc as yacc

#token map
from lexer import tokens

def p_expression_(p):
    'expression : ID '