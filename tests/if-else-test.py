#the cursed code
input = int(input("ingrese un numero"))


def es_par(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return False
    elif n == 4:
        return True
    elif n == 5:
        return False
    elif n == 6:
        return True
    elif n == 7:
        return False
    elif n == 8:
        return True
    else:
        return n % 2 == 0
    
