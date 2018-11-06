
# -----------------------------------------------------------------------------
# parser.py
# A parser for the P++ Language.
# -----------------------------------------------------------------------------

import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'CHARACTER',
   'DIGIT',
   'DELIMITER',
   'OPERATOR'

)
