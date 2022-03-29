#ifndef ANIMALI_H_
#define ANIMALI_H_
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

void copias(const char*, char* &);

class Animali
{
      protected:
              char*Codice;
              char*Specie;
      public:
              Animali();
              Animali(const Animali &);
              void StampaDati();
              char* getCodice(){return Codice;}
              char* getSpecie(){return Specie;}
              char* setCodice(const char* c){copias(c, Codice);}
              char* setSpecie(const char* c){copias(c, Specie);}
              ~Animali();
};

#endif
