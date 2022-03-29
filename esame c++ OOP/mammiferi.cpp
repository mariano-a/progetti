#include "mammiferi.h"

Mammiferi::Mammiferi(const char* cod, const char* spe, const float pes)
{
    copias(cod, Codice);
    copias(spe, Specie);
    Peso=pes;
}

void Mammiferi::StampaDati()
{
    cout<<"\n*******************************";
    cout<<"\nSpecie: "<<Specie;
    cout<<"\nCodice: "<<Codice;
    cout<<"\nPeso: "<<Peso<<"kg";
    cout<<"\n*******************************";
}
