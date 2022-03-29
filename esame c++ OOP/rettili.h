#ifndef RETTILI_H_
#define RETTILI_H_
#include "mammiferi.h"

class Rettili:public Animali
{
      private:
              char*Tipo;
      public:
              Rettili(const char*, const char*, const char*);
              void StampaDati();
              char* getTipo(){return Tipo;}
              ~Rettili();
};

#endif
