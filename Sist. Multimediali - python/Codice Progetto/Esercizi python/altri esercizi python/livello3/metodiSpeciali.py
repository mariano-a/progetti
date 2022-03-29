################# DUNDER METHODS ##################

class Auto:
    def __init__(self,produttore,modello,cilindrata,anno):
        self.produttore = produttore
        self.modello = modello
        self.cilindrata = cilindrata
        self.anno = anno

    def __add__(self,other):
        """ solo per fini didattici """
        return self.produttore + other.modello

    def __str__(self):
        """rappresentazione leggibile per non tecnici """
        return f"{self.produttore} {self.modello}"

    def accelera(self):
        print(self.modello, ": sta accelerando")
    def rifornimento(self):
        print(self.modello, ": sta rifornendo...")

my_car = Auto(produttore="Lancia",modello="Delta",cilindrata = 1300,anno=1980)
lambo = Auto("Lamborghini","Gallardo",5000,2013)

lambo.accelera()
my_car.rifornimento()

print(my_car + lambo)

print(lambo)    #avendo definito __str__ non otteniamo in output l'indirizz di memoria, ma i nomi
