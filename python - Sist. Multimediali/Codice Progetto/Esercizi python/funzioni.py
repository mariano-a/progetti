def stampa_qualcosa():
    print("111111111qualcosa\n")

stampa_qualcosa()
#############################à
def somma(a,b):
    risultato= a+b
    print("222222222222Risultato della somma e' " + str(risultato))#print stampa solo stringhe quando concateni con del testo
    print(risultato)



x = input("primo numero \n")    #input prende in ingresso solo stringhe
y = input("secondo \n")
somma(int(x),int(y))

#############################################à

print("3333METODO RETURN:\n")
def sommaReturn(a,b):
    risultato= a+b
    return (risultato)
print(sommaReturn(int(x),int(y)))

########################################

def max(a,b):
    if a==b:
        print("i numeri sono uguali")
    elif a>b:
        print("il numero a è il piu grande: ",a)
    else:
        print("il numero b è il più grande: ",b)
max(2,4)
#################################################

def car(p,m,a=False):
    print("Acquisto macchina nuova, caratteristiche: ")
    print("Produttore: ",p)
    print("Modello: ", m)
    if a==True:
        print("Macchina accessoriata")

car("Tesla","model 3",True)
