import parser as Parser
import time

#   2018 Processing Plus Plus. Computational Thinking.
#
#   Eduardo Santiago 
#   Maria Marrero
#   Diego Amador
#   Javier Velez

print("Processing Code...\n")
time.sleep(0.25)

file = 'PPPCode.txt'

try:
    Parser.translateCode(file)
    time.sleep(5)
except:
    print("Errors were encountered\n")
