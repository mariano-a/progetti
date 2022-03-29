#metodi per stringhe
nome = "mario "
num= 8
print("ciao " + nome + str(num))
a=[32,77,8]
b=[89,4,6]
print("\n",a+b)
print(len(a))
print(nome * 4)
print(nome[:2])
caratteri = list(nome)
print(caratteri)

#FORMATTAZIONE f
print(f"ciao sono {nome}, questo sono io")
w = f"ciao sono {nome}, questo sono io"
print(w)

z=5
print(f"il quadrato di {z} e' {z*z}")

#altri metodi
mes="fate il vostro gioco"
print("t" in mes)   # TRUE t presente in mes
print("w" in mes)   #FALSE w NON presente in mes
print(1 in a)       #FALSE l'1 non è presente nella lista a
print(mes.startswith("fate"))
print(mes.startswith("f"))
print(mes.startswith("g")) #FALSE

print(mes.endswith("gioco"))
print(mes.endswith("g"))
print(mes.endswith("f"))

print("SFSFsfsFsFsFSFs")
cog="CANE"
var="Pizza"
print(nome.islower())
print(nome.isupper())
print(cog.islower())
print(cog.isupper())
print(var.islower())

print("\n CONVERTIRE TUTTO IN MAIUSC O MINUSC")
print(cog.lower())  #è solo una stampa CANE non cambia definitivamente in cane, infatti:
print(var.upper())
print(cog) #osserva che le stringhe sono immutabili RIMANE MAIUSC ORIGINARIO
cog = cog.lower()
print(cog) # ora ho cambiato effettevimente, ho cane minusc
print("\n ")
print("\n NELLA STRINGHE SOLO LETTERE O SOLO NUMERI")
print(nome.isalpha()) #false perche c'è uno spazio dopo mario
ban="234"
print(ban.isdecimal())
print("\n STRINGA FORMATA O DA NUMERI O DA LETTERE")
#isalnum()
#se una STRINGA ha uno spazio uso: isspace()
print("\n UNIRE GLI ELEMENTI DI UNA LISTA")
lista= ["ciao","sono","luca"]
print(" ".join(lista)) #importate lo SPAZIO dopo la virgola se vuoi lasciarlo, altrimenti lo elimini
print("-> ".join(lista))
print("Presentati: "+ ", ".join(lista))
print("\n".join(lista))

print("\n Da STRINGA a Lista DIVIDENDO DOVE SPECIFICHI IL CARATTERE")
serie="33242-546346-46-4-6-46"
print(serie)
print("\n")
print(serie.split("-"))

#################################
print(f"io ho {lista} anni")
print(f"io ho {num * 3} anni")
