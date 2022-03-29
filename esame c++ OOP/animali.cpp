#include "animali.h"
#include <cstring>
void copias(const char* source, char* &dest)
{
    dest=new char[strlen(source)+1];
    strcpy(dest, source);
}

Animali::Animali()
{
    Codice="";
    Specie="";
}

Animali::Animali(const Animali &x)
{
    copias(x.Codice, this->Codice);
    copias(x.Specie, this->Specie);
}

void Animali::StampaDati()
{
    cout<<"\n*******************************";
    cout<<"\nSpecie: "<<Specie;
    cout<<"\nCodice: "<<Codice;
    cout<<"\n*******************************";
}

Animali::~Animali()
{
    delete []Codice;
    delete []Specie;
}
