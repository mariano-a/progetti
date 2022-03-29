/*
Studente: ASTARITA MARIANO
Matricola: N46/002698
Docente: Fasolino


 Corso di Ingegneria del Software-  Prof. FASOLINO Corso di Laurea in INGEGNERIA 
INFORMATICA Prova Intercorso del 17_12_2019  	Allievo  Cognome e Nome: Matricola:	

Descrizione del Problema

Si faccia riferimento al documento di descrizione dei requisiti del sistema software per 
gestire gli accessi dei soci iscritti ad una palestra (oggetto della prima prova intercorso)

La palestra possiede diversi soci iscritti. Ogni socio all'atto dell'iscrizione alla palestra deve presentare un 
certificato medico che ne attesti l'idoneità allo svolgimento di attività sportiva e deve aver effettuato il 
pagamento della quota di iscrizione annuale. Il sistema deve permettere al segretario della palestra di 
registrare l'iscrizione di ciascun socio, memorizzando nome, cognome, data di nascita, numero di 
telefono del socio, nonchè la disponibilità del certificato medico, la data di scadenza del certificato e la 
data di scadenza dell'iscrizione (che avviene esattamente dopo un anno dal momento del pagamento). Il 
segretario, al momento dell'iscrizione, rilascia inoltre al socio un badge magnetico caratterizzato da un 
codice identificativo univoco (intero compreso fra 1 e 500) e memorizza nel sistema il codice del badge 
assegnato al socio.
La palestra dispone di una porta di accesso che è dotata di due lettori di badge (uno posto all'esterno della 
palestra e l'altro posto all'interno) che consentono l'apertura della porta di accesso. 
Per eseguire l'accesso alla palestra, il socio avvicinerà il proprio badge al lettore di badge, che acquisirà il 
codice identificativo del badge e lo fornirà al sistema per verificare se il socio sia autorizzato all'accesso al 
locale. Per effettuare la verifica, il sistema controlla che il numero del badge sia valido (ossia corrisponda 
ad uno dei badge assegnati ai soci), che il socio associato al badge abbia fornito un certificato medico e 
che la data di scadenza del certificato sia successiva o uguale alla data corrente,  e che la data di 
scadenza dell'iscrizione del socio sia successiva o uguale alla data corrente. In caso di esito positivo di 
questi controlli, il sistema fornirà in output un segnale di apertura della porta, registrerà la data e l'ora 
dell'accesso del socio, e visualizzerà su un display un messaggio di avvenuto accesso, altrimenti 
visualizzerà sul display un apposito messaggio di errore (MSG1: Badge non valido, oppure MSG2: 
Certificato Medico non valido, oppure MSG3: Quota di Iscrizione Scaduta). 
Nel momento in cui il socio decide di uscire dalla palestra, utilizzerà il proprio badge avvicinandolo al 
lettore di badge interno alla palestra. Il lettore acquisisce il numero del badge e lo fornisce al sistema che 
verificherà che il codice sia associato ad un accesso avvenuto,  e conseguentemente aggiornerà i dati 
dell'accesso, registrando anche la data e l'ora di uscita, e invierà un segnale di apertura della porta. Se il 
sistema non troverà un accesso valido associato al badge, esso visualizzerà un apposito messaggio di 
errore sul display (MSG4: Errore di uscita).
Il sistema dovrà permettere al segretario della palestra di ricercare tutti gli accessi effettuati da un 
determinato socio in un intervallo di tempo fra due date, riportando la data e l'ora di ingresso e la data e 
l'ora di uscita per ciascun accesso effettuato. 

QUESITI

Si richiede di modificare il sistema di gestione della palestra in modo da realizzare anche i 
seguenti requisiti aggiuntivi:  

Il sistema deve permettere ad un socio, che abbia già effettuato l'accesso alla palestra, di 
richiedere di usare una delle attrezzature disponibili. 
La palestra dispone di un insieme di attrezzature caratterizzate da un tipo (es. manubrio, cyclette, 
panca…) ed un identificativo univoco (intero su 4 cifre). Ogni attrezzatura può essere in un dato 
istante libera oppure assegnata ad un socio. Ogni socio può usare al più una attrezzatura alla volta.
Un socio che voglia richiedere di usare una delle attrezzature disponibili dovrà fornire in input al 
sistema il proprio codice badge ed il tipo di attrezzatura richiesta. Il sistema dovrà verificare che il 
codice badge sia valido (ossia corrisponda ad uno dei badge assegnati ai soci), che il socio abbia 
già effettuato l'accesso alla palestra e che non abbia ancora utilizzato nessuna attrezzatura. 
Superati con esito positivo questi controlli, il sistema dovrà cercare la prima attrezzatura disponibile 
fra quelle del tipo specificato in input dal socio e ne fornirà in output l'identificativo univoco. A 
questo punto il sistema registrerà che quella attrezzatura non è più disponibile e che è stata 
assegnata al socio nell'ambito dello specifico accesso effettuato dal socio.  Se il codice badge non 
dovesse risultare valido, oppure se nessuna attrezzatura del tipo richiesto è disponibile, o il socio 
sta già utilizzzando una attrezzatura, il sistema dovrà restituire appositi messaggi di errore.

Nel momento in cui il socio esce dalla palestra, il sistema dovrà rendere nuovamente disponibile 
l'attrezzatura eventualmente assegnata al socio.

1.	Si modifichino il diagramma dei casi d'uso ed il diagramma delle classi concettuali 
(System Domain Model) del sistema originario, integrando anche i nuovi requisiti richiesti. 
(N.B. gli studenti dovranno creare una nuova versione di ciascun diagramma ed aggiungerli 
ai diagrammi già sviluppati nella prova precedente. Eventuali modifiche ai precedenti 
diagrammi saranno consentite, ma dovranno essere realizzate solo ed esclusivamente nei 
diagrammi modificati).

2.	Per il caso d'uso Esegui Richiesta Attrezzatura, si disegni il Sequence Diagram di analisi 
che mostra la dinamica di questo caso d'uso. 

*/


