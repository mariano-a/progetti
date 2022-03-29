#ifndef _LIB_
#define _LIB_

#include "monitor.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/shm.h>
#include <sys/ipc.h>

#define OK_PRODUCI_POST 0
#define OK_PRODUCI_FIN 1
#define OK_CONSUMA 2

#define DIM 3

typedef struct{
	Monitor m;
	
	int job_id[DIM];
	int testa;
	int coda;
	int spz_disp;
	int num_fin_bloc;
}Monitor_posta;

void inizia(Monitor_posta* m);
void rimuovi(Monitor_posta* m);

void Produci_c_fin(Monitor_posta* m);
void Produci_c_post(Monitor_posta* m);
void Consuma(Monitor_posta* m);


#endif
