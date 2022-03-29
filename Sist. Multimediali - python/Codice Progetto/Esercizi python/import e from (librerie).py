import random #modulo/libreria random

for n in range(10):
    numero = random.randint(1,100)
    print(numero)

print("FROM")
from math import sqrt # prendo dalla libreria math una singola funzione in questo caso sqrt
print(sqrt(36))

from os import * #utilizzo tutte le funzioni del modulo os senza richiamare il nome del modulo stesso
print(getcwd())
