#ifndef MAMMIFERI_H_
#define MAMMIFERI_H_
#include "animali.h"

class Mammiferi:public Animali
{
      private:
              float Peso;
      public:
              Mammiferi(const char*, const char*, const float);
              void StampaDati();
              float getPeso(){return Peso;}
};

#endif
