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
div(9,0)
