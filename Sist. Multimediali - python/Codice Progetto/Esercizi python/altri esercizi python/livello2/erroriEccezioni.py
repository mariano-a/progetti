'''
def divisore(x,y)
    ris = x/y
    print(ris)


divisore(9,0)   #errore
divisore(9,"spam")  #errore
'''
######
def div(x,y):
    try:
        ris = x/y
        print(ris)
    except:
        print("Errore dati inseriti")
    finally:
        print("questo codice verra eseguito in ogni caso")
div(9,0)

##############################à
def funz(x,y):
    try:
        ris = x/y

    except:
        print("Errore dati inseriti")
    except TypeError:
        print("Non hai inserito un numero")
    else:
        print(ris)
funz(9,3)
##############################
def div(x,y):
