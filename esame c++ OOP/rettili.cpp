#include "rettili.h"

Rettili::Rettili(const char* cod, const char* spe, const char* tip)
{
    copias(cod, Codice);
    copias(spe, Specie);
    copias(tip, Tipo);
}

void Rettili::StampaDati()
{
    cout<<"\n*******************************";
    cout<<"\nSpecie: "<<Specie;
    cout<<"\nCodice: "<<Codice;
    cout<<"\nTipo: "<<Tipo;
    cout<<"\n*******************************";
}

Rettili::~Rettili()
{
    delete []Tipo;
}
