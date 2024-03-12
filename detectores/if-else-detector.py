import ast
from sys import argv, exit

LIMITE = 7 #Cuántos son demasiados if-else?
"""
TODO:
En ppio
 * No toma cuando son if's uno abajo del otro. Ej
        if A
        if B
        if C 
        if D

 * Tampoco cuando están anidados
  if A:
    if B:
       if C:

"""

class IfElifVisitor(ast.NodeVisitor):
    def visit_If(self, node):
        if_count = 1
        #Si hay un orelse y es de tipo condicional
        while node.orelse and isinstance(node.orelse[0], ast.If):
            if_count += 1
            node = node.orelse[0]
        if if_count > LIMITE:  
            print(f"Hay más de {LIMITE} ramas en el if else")
        self.generic_visit(node)

if __name__=="__main__":
    if len(argv) != 2:
        print("Necesito el parcial para corregir! Ayuda: python3 detector.py parcial_a_corregir.py")
        exit(1)

    with open(argv[1], "r") as archivo:
        codigo = archivo.read()

        tree = ast.parse(codigo)
        visitor = IfElifVisitor()
        visitor.visit(tree)
