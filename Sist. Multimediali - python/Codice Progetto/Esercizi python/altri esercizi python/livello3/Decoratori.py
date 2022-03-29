#i decoratori sono uno strumento che ci consente di estendere e modificare il comportamento
#di funzioni e classi  senza doverne alterare direttamente il codice sorgente

#il decoratore è una funzione che prende come parametro un'altra funzione, aggiunge delle
#funzionalità e restituisce un'altra funzione
#senza alterare il codice sorgente della funzione passata come parametro

#ricorda che; tutto in python è un oggetto anche le funzioni

def funz_decoratore(funz_parametro):
    def wrapper():
        print("codice da eseguire PRIMA di funz_parametro")
        funz_parametro()
        print("codice da eseguire DOPO di funz_parametro")
    return wrapper


def mia_funz():
    print("Hello")


mia_funz = funz_decoratore(mia_funz)
mia_funz()

@funz_decoratore #stessa chiamata di: mia_funz = funz_decoratore(mia_funz)
