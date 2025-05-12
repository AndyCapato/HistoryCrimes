**USER STORIES**


- Come utente, voglio navigare nel mondo di gioco;

- Come utente, voglio interagire con gli elementi e i personaggi presenti nella mappa;

- Come utente, voglio visualizzare il diario del protagonista;

- Come utente, voglio poter interrogare gli altri personaggi presenti nel gioco; 

- Come utente, voglio raccogliere indizi, oggetti e dichiarazioni, che possono tornare utili andando avanti con la storia;

- Come utente, voglio poter effettuare delle scelte durante la storia per sbloccare percorsi alternativi;

- Come utente, voglio che il gioco salvi automaticamente i miei progressi;

**CASI D'USO**

**INTERAGIRE CON GLI ELEMENTI E I PERSONAGGI DEL GIOCO**:

**ATTORI**: 

- Utente

- Personaggi non giocabili

**DESCRIZIONE**:

L'utente può interagire con gli elementi e i personaggi presenti nel mondo di gioco;

**PRECONDIZIONI**

- La mappa è stata caricata correttamente;

- Il personaggio non giocabile sia nel raggio d'azione del protagonista e sia disponibile al dialogo;

**FLUSSO PRINCIPALE**

- L'utente sceglie una direzione; 

- Il sistema sposta l'avatar nella direzione scelta;

- Viene aggiornato il mondo di gioco;

-**INTERROGAZIONE DEGLI ALTRI PERSONAGGI**:

**ATTORE**: 

Utente

**DESCRIZIONE**: 

L'utente può avviare e condurre conversazioni con i personaggi non giocanti (NPC) presenti nel gioco.

**PRECONDIZIONI**:

- La verifica delle licenze è andata a buon fine.

- Il gioco è stato avviato correttamente.

- L'utente ha interagito con un personaggio interrogabile (vedi Caso d'Uso 2).

**FLUSSO PRINCIPALE**:

- L'utente seleziona l'opzione per avviare una conversazione con il personaggio.

- Il sistema visualizza una finestra di dialogo o un'interfaccia di conversazione.

- Il sistema presenta all'utente diverse opzioni di domanda o affermazione da scegliere, l’utente può modellare le parole della domanda o dell’affermazione.

- L'utente seleziona una delle opzioni.

- Il personaggio risponde in base alla domanda o affermazione scelta dall'utente e al suo stato attuale nella storia su base di AI.

- La conversazione può proseguire con ulteriori opzioni di dialogo.

- L'utente conclude la conversazione.

- Il sistema torna alla visualizzazione precedente del gioco.

**FLUSSO ALTERNATIVO**:

- Personaggio non disponibile per l'interrogatorio: In determinate circostanze, un personaggio potrebbe non essere disponibile per essere interrogato (es. impegnato in un'altra azione, ostile). Il sistema indica questa indisponibilità.

- Opzioni di dialogo limitate: Le opzioni di dialogo disponibili potrebbero variare a seconda dei progressi nella storia e delle informazioni già in possesso del protagonista.

-**RACCOLTA DI INDIZI, OGGETTI E DICHIARAZIONI:**

**ATTORE**:

 Utente

**DESCRIZIONE**: 

L'utente può acquisire elementi utili per progredire nella storia.

**PRECONDIZIONI**:

- La verifica delle licenze è andata a buon fine.

- Il gioco è stato avviato correttamente.

- L'utente interagisce con un elemento o personaggio che offre un indizio, un oggetto o una dichiarazione (vedi Caso d'Uso 2 e 4).

**FLUSSO PRINCIPALE**:

- Durante l'interazione, il sistema determina se un indizio, un oggetto o una dichiarazione è disponibile per la raccolta.

- Il sistema notifica all'utente l'acquisizione dell'elemento se molto importante (es. messaggio a schermo, animazione).

- Gli oggetti vengono aggiunti all'inventario del protagonista (se applicabile).

- Gli indizi e le dichiarazioni vengono registrate nel diario o in un'altra sezione dedicata.
**FLUSSO ALTERNATIVO**:

- Inventario pieno: Se l'inventario degli oggetti è pieno, il sistema potrebbe impedire la raccolta di nuovi oggetti o chiedere all'utente di scartarne uno esistente.

- Oggetto già raccolto: Se l'utente tenta di raccogliere un oggetto già presente nel suo inventario, il sistema potrebbe impedirlo o fornire un messaggio indicativo.

**REQUISITI FUNZIONALI**

FR1: Controlli e movimento

FR2: Interazione con gli NPC

FR3: Statistiche e progressione

FR4: Inventario ed equipaggiamento

FR5: Gestione delle quest

FR6: Commercio ed economia

FR7: User Interface e User Experience

FR8: Stato del gioco


**FR1: Controlli e movimento**
- Il sistema deve visualizzare il mondo di gioco da una prospettiva 3D.

- Il sistema deve permettere al giocatore di controllare il proprio personaggio usando dei dispositivi di input (tastiera o joypad).

- Il sistema deve permettere al personaggio di muoversi in maniera libera all’interno dell’area di gioco.

- Il sistema deve gestire le collisioni tra il personaggio del giocatore ed oggetti non penetrabili, come rocce, costruzioni, NPC, ecc.

- Il sistema deve permettere al personaggio del giocatore di transitare tra diverse zone della mappa .

- Il sistema deve permettere al personaggio di interagire con oggetti specifici all’interno dell’ambiente di gioco mediante specifiche azioni e rispettando specifici vincoli di vicinanza.

**FR2: Interazione con gli NPC**
- Il sistema deve popolare il mondo con degli NPC.

- Il sistema deve permettere ai giocatori di inizializzare un dialogo con gli NPC.

- Il sistema deve mostrare il testo del dialogo in una parte dedicata della UI.

- Il sistema deve supportare dialoghi ad opzioni multiple.

- Gli NPC devono poter assegnare quest al giocatore.

-Alcuni NPC potranno mostrare schemi di movimento di base (come camminare lungo percorsi predefiniti).


**FR3: STATISTICHE E PROGRESSIONE**
- Il sistema fornisce le seguenti statistiche potenziabili dal giocatore:

- HP (Punti Salute) Rappresenta la salute fisica del personaggio giocabile.

- MP (Mental Point) Rappresenta le capacità del detective nella concetrazione durante l'investigazione, l'analisi e la deduzione delle scene del crimine.

-IQ (Intelligenza) Rappresenta statistica primaria e fondamentale, determina la capacità di risolvere 
enigmi, scovare indizi, compredere informazioni complesse e migliorie nelle abilità d'investigazione.

-Velocità: Rappresenta la statistica di velocità delle operazioni durante le varie operazioni di Gameplay.

-Fortuna: Aumenta la possibilità di trovare segreti o aiuti durante il gioco.


**FR4: Inventario ed equipaggiamento**

-Il sistema dovrà fornire un inventario che il giocatore userà per conservare gli oggetti raccolti.

-Il sistema dovrà mostrare l'inventario tramite una schermata dedicata dell'interfaccia utente.

-Il sistema dovrà permettere al giocatore di usare oggetti consumabili e permanenti dall'inventario.

-Il sistema dovrà permettere al giocatore di visualizzare le descrizioni e le proprietà degli oggetti.

-Il sistema dovrà permettere al giocatore di equipaggiare e rimuovere oggetti negli slot appropriati tramite l'interfaccia utente.

-Il sistema dovrà conferire abilità in base agli oggetti equipaggiati.

-Il sistema dovrà permettere al giocatore di visualizzare nel dettaglio gli oggetti se si tratta di documenti, fondamentali per progredire nel gioco.

**FR5: Gestione delle missioni**

-Il sistema dovrà permettere al giocatore di accettare missioni dagli NPC o da altre fonti (episodi principali).

-Il sistema dovrà fornire una schermata per il Registro Missioni, tracciando le missioni attive e completate, e mostrandone obiettivi e descrizioni.

-Il sistema dovrà tracciare i progressi del giocatore verso gli obiettivi della missione.

-Il sistema dovrà aggiornare automaticamente lo stato della missione al completamento degli obiettivi.

-Il sistema dovrà permettere al giocatore di consegnare le missioni completate all’NPC pertinente o completarle in maniera automatica.

-Il sistema dovrà distribuire le ricompense al completamento della missione.

-Il sistema dovrà localizzare le missioni all'interno delle aree di gioco.

**FR6: Commercio ed Economia**

-Il sistema dovrà tenere traccia della valuta del giocatore.

-Il sistema dovrà offrire una interfaccia per commercio con appositi NPC.

-Il sistema dovrà permettere al giocatore di comprare oggetti dal venditore, deducendone il costo dalla valuta a disposizione.

-Il sistema dovrà permettere al giocatore di vendere oggetti al venditore, aggiungendone il costo alla valuta a disposizione.

**FR7: User Interface e User Experience**

-Il sistema dovrà fornire un menu principale all'avvio del gioco.

-Il sistema dovrà fornire un menu di gioco accessibile durante l'esplorazione.

-Il sistema dovrà mostrare informazioni essenziali del personaggio sullo schermo durante l'esplorazione.

-Il sistema dovrà fornire un chiaro feedback visivo per azioni, cambiamenti di stato, interazioni con NPCs e eventi speciali di indagini.

-Il sistema dovrà mostrare informazioni essenziali relative alle missioni in corso e alla loro posizione.

**FR8: Stato del gioco**

-Il sistema dovrà permettere al giocatore di salvare i dettagli del progresso nel gioco.

-Il sistema dovrà permettere il salvataggio presso punti di salvataggio designati o potenzialmente ovunque al di fuori di combattimenti o cutscene.

-Il sistema dovrà permettere al giocatore di caricare uno stato di gioco precedentemente salvato.

-Il sistema dovrà gestire le impostazioni audio, video, e dei controlli di gioco.
 

**REQUISITI NON FUNZIONALI**

**NFR1: Prestazioni**

- Su configurazioni dalle specifiche raccomandate, il gioco dovrà mantenere un frame rate costante di almeno 60 FPS (escludendo le scene cinematiche);

- Su configurazioni dalle specifiche raccomandate, il gioco dovrà garantire il completamento delle transizioni tra le diverse zone della mappa entro cinque secondi;

- Su configurazioni dalle specifiche raccomandate, Il caricamento di uno stato di gioco salvato dovrà completarsi entro 15 secondi sull'hardware;

- Su configurazioni dalle specifiche raccomandate, le transizioni tra le cinematiche e lo stato attivo di gioco dovranno essere quasi istantanee, con ritardo inferiore al secondo.
Il consumo delle risorse disponibili dovrà essere ragionevolmente compatibile con quello previsto per un semi-open world 3D;

- Su configurazioni dalle specifiche raccomandate, il gioco dovrà registrare tutte le scelte decisive (relative al percorso della storia) prese dal giocatore entro 5 secondi;

**NFR2: Usabilità**

- Tutti gli elementi dell'interfaccia utente (ad esempio, menu, finestre di dialogo, interfaccia delle scene di indagine) dovranno essere chiari, leggibili e facili da navigare usando mouse, tastiera o gamepad;

- L'input del giocatore dovrà risultare reattivo con una latenza minima percepibile;

- Il gioco dovrà fornire un chiaro feedback visivo e audio per le azioni chiave, come puzzle completati, prove importanti raccolte, navigazione nei menu, raccolta oggetti o completamento missioni;

- I giocatori dovranno essere introdotti alle meccaniche principali da un sistema di tutorial opzionali e non intrusivi;

- I controlli dovranno essere riconfigurabili a piacimento dal giocatore.
Le informazioni importanti dovranno essere sempre a disposizione durante indagini ed esplorazione;

**NFR3: Affidabilità e Stabilità**

- Il software del gioco deve operare in modo stabile, riducendo al minimo i crash inaspettati durante la sessione di gioco.

- Il sistema di salvataggio e caricamento dei progressi di gioco deve essere veloce e affidabile, evitando la corruzione dei file di salvataggio.

- I calcoli fondamentali del gioco, in particolare quelli alla progressione (guadagno di esperienza, effetti delle abilità), devono essere coerenti, prevedibili e riproducibili date le stesse condizioni in input e stato di gioco.

- Il gioco deve essere in grado di gestire errori non gravi (perdite di connessione, file di configurazione mancanti ma con valori predefiniti) senza interrompere immediatamente l'esperienza di gioco.

**NFR4: Manutenibilità**

- Il codice sorgente del gioco dovrà essere strutturato seguendo un design modulare, con componenti ben definiti e interfacce chiare, e dovrà essere adeguatamente documentato per: la correzione di bug, l'aggiornamenti futuri e integrazione di nuove funzionalità da parte del team di sviluppo.

- I contenuti di gioco (oggetti, nemici, missioni) dovrebbero essere definiti e gestiti in modo da permettere agli sviluppatori di proporre modifiche o aggiunte in maniera efficace, tramite sistemi di configurazione esterni al codice sorgente principale.        Questa definizione dovrebbe basarsi sull'analisi dell'utenza giocante (fase di testing, recensioni post-lancio).

- I sistemi devo essere differenti ma affini all'interno del gioco, in grado di condividere una logica comune tra esse, implementata nel codice promuovendo così coerenza, riducendo la ridondanza e semplificando la manutenzione e gli aggiornamenti futuri.

**NFR5: Portabilità**

- Il motore di gioco e l'architettura devono essere progettati per facilitare ragionevolmente potenziali porting futuri verso nuovi sistemi.

- La gestione dell'input e della risoluzione dello schermo deve essere flessibile.

**NFR6: Accessibilità**

- Gli elementi testuali (dialoghi, menu, descrizioni) dovranno supportare dimensioni del carattere regolabili o fornire un'opzione predefinita ad alto contrasto.

- Le scelte cromatiche adottate nell’interfaccia utente dovrebbero tenere in adeguata considerazione le principali forme di daltonismo, prevedendo l’impiego di indicatori alternativi al colore.

- Dovranno essere forniti controlli del volume separati per l'audio principale, la musica, gli effetti sonori e i dialoghi.

- Dovrà essere possibile cambiare la configurazione dei comandi.

**NFR7: Estetica**

- Il gioco presenta uno stile 3D ultra-realistico; 

- I modelli dei personaggi, l'ambientazione, gli elementi visivi e sonori, devono essere coerenti tra di loro;

- Gli effetti sonori devono segnalare gli eventi del gioco;

- Il gioco deve mantenere la qualità visiva anche su schermi con risoluzioni diverse;

- Il design dovrebbe considerare anche giocatori con disabilità sensoriali, ad esempio offrendo opzioni per regolare contrasto, effetti visivi e livelli audio separati;

**NFR8: Integrità**

- I progressi del giocatore devono essere salvati automaticamente durante la partita;

- Il sistema deve mantenere una copia di backup del salvataggio automatico più recente per permettere il ripristino in caso di corruzione dei dati;

- Il giocatore deve ricevere un'indicazione chiara (es. icona discreta) quando un salvataggio automatico è in corso, per evitare chiusure improvvise;














