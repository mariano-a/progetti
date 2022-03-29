spam = "la pratica "
eggs = "rende perfetti"
print(spam + eggs)
print(spam * 3)

a = [1,2,"tre"]
b= [4,5,"sei"]
print(a+b)
print(a * 3)
print("\n")

print(len(spam))
print(len(a))

print(2 in a)
print("sei" in b)
print("sette" in b)

#capovolgo la stringa
def reverse(stringa):
    indice = (len(stringa) -1)
    nuova_string = ""
    while indice >=0:
        nuova_string += stringa[indice]
        indice -= 1
    print(nuova_string)
reverse("abcd")

#per eliminare parole dalla stringa
string= "ciao Giovanniof"
print(string[:-2])

#formo una lista contenente tutti i caratteri di una stringa
print(list(string))
