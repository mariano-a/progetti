'''
class Esempio:
    pass

ogg = Esempio()
print(type(ogg))
'''
class Gatto:

    famiglia = "felini"     #variabili di classe -> per tutti gli oggetti della classe

    def __init__(self,nome,anni):   #variabili di istanza -> specifiche  per ciascun oggetto
        self.nome = nome            #self referenza all'oggetto del tipo Gatto
        self.anni = anni

mio_gatto = Gatto(nome="palla",anni=3)
print(type(mio_gatto))
print("Nome: ", mio_gatto.nome)
print("Anni: ", mio_gatto.anni)
print("Famiglia: ", mio_gatto.famiglia)

tuo_gatto = Gatto(nome="codino",anni=5)
print(type(tuo_gatto))
print("Nome: ", tuo_gatto.nome)
print("Anni: ", tuo_gatto.anni)
print("Famiglia: ", tuo_gatto.famiglia)


class Cane:
    def __init__(self, nome, anni ,razza):
        self.nome = nome
        self.anni = anni
        self.razza = razza
mio_cane = Cane("Bob",5,"pastore tedesco")
print(type(mio_cane))
print(mio_cane.nome)
print(mio_cane.anni)
print(mio_cane.razza)
