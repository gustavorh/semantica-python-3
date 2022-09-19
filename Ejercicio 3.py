# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:39:52 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

# Preguntamos al usuario por un número
numero = input("Ingrese un número: ")
numero = int(numero)

# Inicializamos la variable 'contador' con un valor 0
contador = 0

for divisor in range(1, numero):
    # Si el resto de la división es 0 (mod), entonces es un valor divisible del numero entregado por el usuario
    if (numero % divisor == 0):
        contador = contador + divisor
if (contador == numero):
    print(f'\n{numero} es un número perfecto')
else:
    print(f'{numero} no es un número perfecto')
