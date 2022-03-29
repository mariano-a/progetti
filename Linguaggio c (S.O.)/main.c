#include "lib.h"

int main(){
	key_t key=IPC_PRIVATE;

	int shmid=shmget(key, sizeof(Monitor_posta), IPC_CREAT|0664);

	Monitor_posta* m=(Monitor_posta*)shmat(shmid,0,0);

	inizia(m);

	//srand...

	int pid=fork();
	if(pid==0){  //sportellista
		for(int i=0; i<16; i++){
			Consuma(m);
			sleep(1);
		}
		
		exit(0);
	}

	pid=fork();
	if(pid==0){
		for(int i=0; i<4; i++){
			Produci_c_fin(m);
			sleep(4);
		}
		
		exit(0);
	}

	for(int i=0; i<3; i++){
		pid=fork();
		if(pid==0){
			for(int i=0; i<4; i++){
				sleep(2);
				Produci_c_post(m);
			}
			
			exit(0);
		}
	}

	int stato;
	for(int i=0; i<5; i++)
		pid=wait(&stato);

	rimuovi(m);

	shmctl(shmid, IPC_RMID,0);

	return 0;
}
