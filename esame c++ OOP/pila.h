#ifndef PILA_H_
#define PILA_H_
#include "rettili.h"

struct Nodo
{
    Animali A;
    Nodo*next;
};

class Pila
{
      private:
              Nodo*first;
      public:
              Pila(){first=0;}
              void InserisciNodo(Animali);
              void StampaPila();
              ~Pila();   
};
#endif
