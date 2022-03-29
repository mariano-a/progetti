class Auto:
    def __init__(self,produttore,modello,cilindrata,anno):
        self.produttore = produttore
        self.modello = modello
        self.cilindrata = cilindrata
        self.anno = anno

    def accelera(self):
        print("Sto accelerando")
        print(self.modello, ": sta accelerando")
    def rifornimento(self):
        print(self.modello, ": sta rifornendo...")

my_car = Auto(produttore="Lancia",modello="Delta",cilindrata = 1300,anno=1980)
lambo = Auto("Lamborghini","Gallardo",5000,2013)

print(type(my_car))
print(type(lambo))
print(my_car)
print(lambo)

lambo.accelera()
my_car.rifornimento()
