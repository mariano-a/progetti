#LISTEEEEEEEEEEEEE
elenco = [2,5,"pizza",5.4,"nutella"] #indici: 0,1,2,3,4
print(elenco)
print(elenco[2])
print(elenco[-2]) #=5.4  ..accesso al penultimo elemento il meno ci fa partire dalla fine della lista in questo caso non parto da zero
elenco[1] = 8
print(elenco)
##########################################################
fetta = [5,9,7,5,3,2]
bo=fetta[1:4]   #dall indice 1 al 4
print(fetta) #stampa la lista completa originaria
print(bo) #stampa gli elementi scelti

##########################################################
bo=fetta[3:] #parto dall'indice 3 fino alla fine della lista
print(bo)

##########################################################
bo=fetta[:3]#parto dal primo fino all elemento dell indice 3
print(bo)
##########################################################
for lista in fetta: #cicla e stampa la lista fetta
    print(lista)

##########################################################
lista_numerica =list(range(50,100))
print(lista_numerica)

#### MODIFICHE ALL LISTA GIA CREATA ############################
print("MODIFICHE ALL LISTA GIA CREATA")
elenco.append("6") #aggingi valore alla fine della lista
print(elenco)
elenco.reverse()  #invertire la lista
print(elenco)

l = [5,3,8,1,7]
l.sort()    #ordina lista in ordine crescente
print(l)

##########################################################
lista = [2,"bob",7.8,"alice",[2,3,4,5],44]
print(lista)
print(lista[4]) #stampo sotto lista
print(lista[4][1]) #stampo il secondo elemento della sottolista quindi 3
lista[3]="DAN"  #modifico l'elemento 3 della lista
print(lista)
del lista[2] #cancello l elemento 2 ovvero 7.8 della lista a partire DALL'INDICE
print(lista)
lista.remove(44) #cancello l elemento 5 ovvero 44 della lista a partire DAL VALORE
#TUPLEEEEEEEEEEEEE SONO IMMUTABILI
tuple1 = (2,3,5)
tuple2 = 6,1,3          #non c'è differenza con le parentesi
print(tuple1)
print(tuple2)
print(tuple1[2])
del tuple1[1] ##### ERRORE gli elementi delle tuple non possono essere cancellati
#le tuple vengono eseguite piu velocemente delle liste

#SET LISTA NON ORDINATA DI ELEMENTI - ELEMENTI UNICI -> NO COPIE ma possono essere MODIFICATI
print("SETTTTTTTTTTTTTTTTTTTTTTTTTTT")
list = [2,3,4,2,3]
unici = set(list)
print(unici)
unici.add(55)
print(unici)
#help(unici) inserito in shell di python, ci mostra la documentazione dei metodi adottati da set
