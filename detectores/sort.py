from ast import NodeVisitor, Attribute, parse
from sys import argv, exit

funciones = ["enumerate", "filter", "map", "sort", "sum", "zip", "reverse"]

class Visitor(NodeVisitor):
    def visit_Call(self, node):
        if isinstance(node.func, Attribute) and node.func.attr in funciones:
            print("Advertencia: Se esta utilizando una funcion no permitida: ", node.func.attr)

        self.generic_visit(node)

if __name__=="__main__":
    if len(argv) != 2:
        print("Necesito el parcial para corregir! Ayuda: python3 sort.py parcial_a_corregir.py")
        exit(1)

    with open(argv[1], "r") as archivo:
        codigo = archivo.read()

        tree = parse(codigo)
        visitor = Visitor()
        visitor.visit(tree)