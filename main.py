def addmultiplenumbers(numbers):
    """
    Suma una lista de números.
    """
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    """
    Multiplica todos los números de una lista.
    """
    if not numbers:
        return None
    result = 1
    for x in numbers:
        result *= x
    return result

def isiteven(x):
    """
    Devuelve True si el número es par e integer, False en otro caso.
    """
    return isinstance(x, int) and x % 2 == 0

def isitaninteger(x):
    """
    Devuelve True si el número es entero, False en caso contrario.
    """
    return isinstance(x, int)


lista = [2, 3, 4]
print("Suma:", addmultiplenumbers(lista))
print("Multiplicación:", multiplymultiplenumbers(lista))
print("¿El número 4 es par?", isiteven(4))
print("¿El número 4.5 es entero?", isitaninteger(4.5))

def main():
  print("Hello learners!")




if __name__=="__main__":
  main()