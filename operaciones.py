def validar_numeros(num1, num2):
    """
    Función auxiliar para validar que ambos parámetros sean int o float.
    """
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise ValueError("Ambos parámetros deben ser números (int o float).")

def sumar(num1, num2):
    """
    Suma dos valores.
    """
    validar_numeros(num1, num2)
    return num1 + num2

def restar(num1, num2):
    """
    Resta dos valores.
    """
    validar_numeros(num1, num2)
    return num1 - num2

def multiplicar(num1, num2):
    """
    Multiplica dos valores mediante suma recurrente.
    """
    validar_numeros(num1, num2)

    # Inicializamos el resultado en 0
    resultado = 0

    # Sumamos num1 a sí mismo num2 veces
    for _ in range(int(num2)):
        resultado = sumar(resultado, num1)

    return resultado

def dividir(dividendo, divisor):
    """
    Divide dos valores. No se permite dividir por cero.
    """
    validar_numeros(dividendo, divisor)

    if divisor == 0:
        raise ValueError("No se puede dividir por cero.")

    cociente = 0

    while dividendo >= divisor:
        dividendo = restar(dividendo, divisor)
        cociente = sumar(cociente, 1)

    return cociente


