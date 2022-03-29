while True:
    print('''
    Calcolatrice
    Funzioni disponibili:
    Per effetturare una divisione, seleziona 1;
    per effettuare un calcolo esponenziale, seleziona 2;
    ''')

    scelta = input("inserisci il numero\n")

    if scelta == "1":
        print("divisione\n")
        a = float(input("inserisci il primo numero\n"))
        b = float(input("inserisci il secondo numero\n"))
        print("il risultato e': " + str(a/b))

    elif scelta == "2":
        print("esponenziale\n")
        a = float(input("primo numero\n"))
        b = float(input("secondo numero\n"))
        print("il risulatato e' : "+ str(a ** b))
    elif scelta == "Esc":
        break

    loop = input("Desideri ancora usare la calcolatrice ? S/N \n")
    if loop == "S" or loop == "s":
        continue
    else:
        break

