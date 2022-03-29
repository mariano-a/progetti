#include "lib.h"


void inizia(Monitor_posta* m){
	init_monitor(&(m->m),3);

	m->testa=0;
	m->coda=0;
	m->spz_disp=DIM;

	m->num_fin_bloc=0;
}
void rimuovi(Monitor_posta* m){
	remove_monitor(&(m->m));
}

void Produci_c_fin(Monitor_posta* m){
	enter_monitor(&(m->m));

	while(m->spz_disp==0){
		m->num_fin_bloc++;
		wait_condition(&(m->m), OK_PRODUCI_FIN);
		m->num_fin_bloc--;
	}

	m->spz_disp--;

	int i=m->testa;
	m->testa=(m->testa+1)%DIM;

	leave_monitor(&(m->m));

	m->job_id[i]=rand()%50+1;
	printf("[CLIENTE FIN] Ho prodotto %d in posizione %d \n",m->job_id[i], i);

	enter_monitor(&(m->m));

	signal_condition(&(m->m), OK_CONSUMA);
	
	leave_monitor(&(m->m));
}

void Produci_c_post(Monitor_posta* m){
	enter_monitor(&(m->m));

	while(m->spz_disp==0 || m->num_fin_bloc>0)
		wait_condition(&(m->m), OK_PRODUCI_POST);

	m->spz_disp--;

	int i=m->testa;
	m->testa=(m->testa+1)%DIM;

	leave_monitor(&(m->m));

	m->job_id[i]=rand()%50+51;
	printf("[CLIENTE POST] Ho prodotto %d in posizione %d\n",m->job_id[i], i);

	enter_monitor(&(m->m));

	signal_condition(&(m->m), OK_CONSUMA);
	
	leave_monitor(&(m->m));
}

void Consuma(Monitor_posta* m){
	enter_monitor(&(m->m));

	while(m->spz_disp==DIM)
		wait_condition(&(m->m), OK_CONSUMA);

	int i=m->coda;
	m->coda=(m->coda+1)%DIM;

	leave_monitor(&(m->m));

	printf("[SPORTELLISTA] Ho consumato %d in posizione %d \n",m->job_id[i], i);

	enter_monitor(&(m->m));

	m->spz_disp++;

	if(m->num_fin_bloc>0)
		signal_condition(&(m->m), OK_PRODUCI_FIN);
	else
		signal_condition(&(m->m), OK_PRODUCI_POST);	

	leave_monitor(&(m->m));
}




