cont =0
while cont < 11:
    print(cont)
    cont += 1
print("\n")


print("Un altro esempio: \n")
cont =0
while True:
    print(cont)
    cont += 1
    if cont > 12:
        print("esco dal ciclo")
        break
print("fine \n")# print fuori dal while


print("Un altro esempio: ")
cont=0
while cont < 10:
    cont += 1
    if cont == 3:
        print("salta valore")
        continue #ritorna all'inizio del while senza eseguire le istruzioni che vengono dopo
        print("continue") # non la stampa, appunto perche continue salta direttamente su al while
    print(cont) # print dentro al while
