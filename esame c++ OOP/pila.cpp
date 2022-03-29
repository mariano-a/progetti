#include "pila.h"

void Pila::InserisciNodo(Animali bestia)
{
    Nodo*temp=new Nodo;
    temp->A.setCodice(bestia.getCodice());
    temp->A.setSpecie(bestia.getSpecie());
    temp->next=first;
    first=temp;
}

void Pila::StampaPila()
{
    Nodo*temp=first;
    while (temp!=0)
    {
        cout<<"\nEsemplare: "<<temp->A.getSpecie();	//dato che ho un cout<< ho la funzione getspecie per il valore non posso fare ->
        cout<<"\nCodice: "<<temp->A.getCodice();
        temp=temp->next;
    }
}

Pila::~Pila()
{
    Nodo*temp;
    while(first!=0)
    {
        temp=first;
        first=temp->next;
        delete temp;         
    }
}
