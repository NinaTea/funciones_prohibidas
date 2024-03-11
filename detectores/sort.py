from ast import NodeVisitor, Attribute, parse
from sys import argv, exit


class SortDetector(NodeVisitor):
    def visit_Call(self, node):
        if isinstance(node.func, Attribute) and node.func.attr == "sort":
            print("Advertencia: Se esta utilizando el metodo sort()")
        
        
if __name__=="__main__":
    if len(argv) != 2:
        print("Necesito el parcial para corregir! Ayuda: python3 sort.py parcial_a_corregir.py")
        exit(1)

    with open(argv[1], "r") as archivo:
        codigo = archivo.read()

        tree = parse(codigo)
        sort_detector = SortDetector()
        sort_detector.visit(tree)