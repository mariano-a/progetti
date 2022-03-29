#metodi sulle liste
invent = ["gennaio","febbraio","marzo"]
invent.append("aprile")
print(invent)


def riempi_inventario():
    lista = []
    while True:
        ogg= input("Inserisci nell inventario quello che vuoi")
        if ogg == "terminato":
            break
        else:
            lista.append(ogg)

    print("Gli oggetti presenti sono: " + str(lista))

riempi_inventario()

#deu metodi per rimuovere il valore
del invent[0]
print(invent)

#invent.remove("gennaio")
print(invent)

#riordinare la lista
alfab= ["z","a","c"]
alfab.sort()
print(alfab)


num= [4,2,8,1]
num.sort()

num.sort(reverse=True)   #ordina al contrario

#restituire un indice di un dato
a=num.index(8)  #= 0 perche l ho riordinato ho fatto il reverse prima
print(a)

#inserire un valore
num.insert(1,"d") #inseriesco un valore "d" nella lista nel l'indice indicato

