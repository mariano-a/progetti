#include "pila.h"
#include <cstring>
int main(int argc, char *argv[])
{
    Pila pila;
    Mammiferi M1("M1", "Leone", 120);
    Mammiferi M2 ("M2", "Tigre", 110);
    Mammiferi M3 ("M3", "Capra", 70);
    Rettili R1 ("R1", "Cobra", "A");
    Rettili R2("R2", "Vipera", "A");
    Rettili R3 ("R3", "Alligatore", "B");
 
    Mammiferi M[3]={M1,M2,M3};
    Rettili R[3]={R1,R2,R3};
 
    for (int i=0; i<3; i++) {
       M[i].StampaDati();
       R[i].StampaDati();
    } 
    system("PAUSE");
    system("CLS");
    
    Animali A;
    for (int i=0; i<3; i++)
    {
        if (M[i].getPeso()<100)
        {
            A.setCodice(M[i].getCodice());
            A.setSpecie(M[i].getSpecie());
            pila.InserisciNodo(A);
        }
        if (!strcmp("A", R[i].getTipo()))
        {
            A.setCodice(R[i].getCodice());
            A.setSpecie(R[i].getSpecie());
            pila.InserisciNodo(A);
        }
    }

    cout << "\n I seguenti esemplari sono attualmente nella pila: " << endl; 
    pila.StampaPila(); 
    cout << "\n";
    system("PAUSE");
    return EXIT_SUCCESS;
}
