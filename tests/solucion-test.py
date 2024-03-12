from typing import List, Tuple, Dict # Para Python 3.8

def valor_maximo(s: List[Tuple[float,float]]) -> float:
  maximo = s[0][1]
  for valores in s:
    if valores[1] > maximo:
      maximo = valores[1]
  
  return maximo

def funcion_trucha_sort(s: List[Tuple[float,float]]) -> float:
    s.sort()
    maximo = s[-1]
    return maximo


def funcion_trucha_reverse(s: List[Tuple[float,float]]) -> float:
    s.reverse()
    ultimo = s[0]
    return ultimo