import re
import math

# Definir los tokens
tokens = [
    ('NUMERO', r'\d+(\.\d*)?'),  # Número entero o decimal
    ('SUMA', r'\+'),               # Operador suma
    ('RESTA', r'\-'),              # Operador resta
    ('MULTIPLICACION', r'\*'),     # Operador multiplicación
    ('DIVISION', r'/'),            # Operador división
    ('RAIZ', r'raiz'),             # Palabra reservada para raíz cuadrada
    ('PARENTESIS_IZQ', r'\('),     # Paréntesis izquierdo
    ('PARENTESIS_DER', r'\)'),     # Paréntesis derecho
    ('ESPACIO', r'\s+'),           # Espacios en blanco
]

# Unir los patrones de los tokens
patron_tokens = '|'.join('(?P<%s>%s)' % par_token for par_token in tokens)

# Función para generar los tokens
def generar_tokens(expresion):
    for coincide in re.finditer(patron_tokens, expresion):
        tipo = coincide.lastgroup
        valor = coincide.group(tipo)
        if tipo == 'ESPACIO':
            continue
        elif tipo == 'NUMERO':
            valor = float(valor)  # Convertir a flotante
        yield tipo, valor

# Función para evaluar una expresión matemática
def evaluar_expresion(expresion):
    tokens_expresion = generar_tokens(expresion)
    pila_numeros = []
    pila_operadores = []
    for tipo, valor in tokens_expresion:
        if tipo == 'NUMERO':
            pila_numeros.append(valor)
        elif tipo == 'RAIZ':
            # Calcular la raíz cuadrada del número anterior
            pila_numeros[-1] = math.sqrt(pila_numeros[-1])
        elif tipo in {'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION'}:
            pila_operadores.append(valor)
    while pila_operadores:
        operador = pila_operadores.pop(0)
        if operador == '+':
            pila_numeros[0] += pila_numeros.pop(1)
        elif operador == '-':
            pila_numeros[0] -= pila_numeros.pop(1)
        elif operador == '*':
            pila_numeros[0] *= pila_numeros.pop(1)
        elif operador == '/':
            pila_numeros[0] /= pila_numeros.pop(1)
    return pila_numeros[0]

# Ciclo principal
while True:
    expresion = input("Ingrese una expresión matemática (o 'salir' para terminar el programa): ")
    if expresion.lower() == 'salir':
        break
    resultado = evaluar_expresion(expresion)
    print("El resultado es:", resultado)
