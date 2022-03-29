#DIZIONARI22
dizio = {"chiave":"valore", "nome":"mario", "eta":27, 80052:"cap","coordinate":[2,3]}
print(dizio["nome"])
print(dizio[80052])

dizio["nome"] = "peppe"
print(dizio["nome"])
print(dizio)

#cerchiamo
a="nome" in dizio  #puoi cercare solo la chiave che e di conseguenza avremo anche il valore
print(a)

del dizio[80052] # puoi cancellare solo la chiave e di conseguenza cancelli anche il valore
print(dizio)

print(dizio.keys())     #stampo solo le chiavi
print(dizio.values())   #stampo solo i valori
print(dizio.items())    #metto in lista tutte le coppie chiavi:valore presenti

solo_val = list(dizio.values()) #stampo i valori
print(solo_val)

for chiave in dizio.keys(): #stampo solo le chiavi
    print(chiave)

#gestione degli errori
b=dizio.get("borra","chiave non trovata")
print(b)
c=dizio.get("nome","chiave non trovata")
print(c)

#settare un valore sulla chiave indicata, se non la trova crea la coppia indicata
dizio["nazionalita"] = "italiana"
dizio.setdefault("cognome","nicola")
print(dizio)


if "chiave_non_esistente" in dizio:
    print(dizio["chiave_non_esistente"])
else:
    print("chiave non trovata")


print("###################################à")
dizio.setdefault("nazionalita","cuba") #nota che non puo settare una chiave gia esistente
print(dizio)
dizio.setdefault("naz","cuba")
print(dizio)
