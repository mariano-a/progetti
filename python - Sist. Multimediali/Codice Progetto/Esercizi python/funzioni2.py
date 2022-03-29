x = 15      #variabile globale definita nel global scope(all'esterno della funzione)


def funz_esempio():
    x += 2  #non è possibile modificarla . Abbiamo un errore in quanto non è stata dichiarata in ambito locale
    return (x)

print(funz_esempio()) #questa chiamata restituisce errore in quanto non possiamo modificare una variabile dic
#dichiarata globale(all esterno di una funz) all 'interno di una funz(dove ci sono le variabile locali)


def funz_esempio():
    global x        #python sa che ci stiamo riferendo alla x in ambito globale
    x += 2
    return(x)
print(funz_esempio())


def funz_esempio():
    y=x  #senza global la funzione non puo modificare la var globale ma puo vederla(leggerla)
    y += 2
    return(y)
print(funz_esempio()) # okk
print(y) #errore variabile visibile solo in locale nella funz

##################################altro esempio:
def mia_funz():
    spam = 24
    return(spam)

eggs = spam+6
print(eggs) #errore perche spam è stata definita nel local scope(all'interno della funzione)

#risolvo:
eggs = mia_funz() + 6
print(eggs)
