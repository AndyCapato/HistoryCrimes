**USER STORIES**


- Come utente, voglio navigare nel mondo di gioco;

- Come utente, voglio interagire con gli elementi e i personaggi presenti nella mappa;

- Come utente, voglio visualizzare il diario del protagonista;

- Come utente, voglio poter interrogare gli altri personaggi presenti nel gioco; 

- Come utente, voglio raccogliere indizi, oggetti e dichiarazioni, che possono tornare utili andando avanti con la storia;

- Come utente, voglio poter effettuare delle scelte durante la storia per sbloccare percorsi alternativi;

- Come utente, voglio che il gioco salvi automaticamente i miei progressi;

**CASI D'USO**

-**NAVIGARE NEL MONDO DI GIOCO**:

**ATTORI**: 

Utente

**DESCRIZIONE**:

L'utente può navigare liberamente nel mondo di gioco.

**PRECONDIZIONI**

- La verifica delle licenze è andata a buon fine

- Il gioco è stato avviato correttamente.

**FLUSSO PRINCIPALE**

- L'utente sceglie una direzione; 

- Il sistema sposta l'avatar nella direzione scelta;

- Viene aggiornato il mondo di gioco;

**FLUSSO ALTERNATIVO**

- L'utente cerca di accedere a un'area non accessibile, viene mostrato un messaggio di errore.

-**INTERAGIRE CON GLI ELEMENTI E I PERSONAGGI DEL GIOCO**:

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

-**VISUALIZZARE DIARIO PROTAGONISTA**:

**ATTORI**: 

Utente

**DESCRIZIONE**:

L'utente può visualizzare il diario del protagonista.

**PRECONDIZIONI**

- Il gioco è in esecuzione;

- Sono presenti voci nel diario;

**FLUSSO PRINCIPALE**

- L’utente apre il menu;

- Seleziona “Diario”;

- Il sistema mostra la lista delle voci registrate;

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

-**EFFETTUARE SCELTE PER SBLOCCARE PERCORSI ALTERNATIVI:**

**ATTORE**: Utente

**DESCRIZIONE**: L'utente può influenzare lo sviluppo della storia attraverso decisioni.

**PRECONDIZIONI**:

- La verifica delle licenze è andata a buon fine.

- Il gioco è stato avviato correttamente.

- Il gioco raggiunge un punto narrativo in cui è richiesta una scelta.

**FLUSSO PRINCIPALE**:

- Il sistema presenta all'utente diverse opzioni di scelta (testuali o visive).

- L'utente seleziona una delle opzioni.

- Il sistema registra la scelta dell'utente.

- La narrazione prosegue in base alla scelta effettuata, potenzialmente sbloccando nuove scene, dialoghi o interazioni.

**FLUSSO ALTERNATIVO**:

- Scelta con conseguenze immediate: La scelta dell'utente potrebbe avere un impatto immediato sull'ambiente di gioco o sui personaggi.

- Scelta con conseguenze a lungo termine: La scelta dell'utente potrebbe influenzare gli eventi futuri della storia.

-**SALVATAGGIO AUTOMATICO DEI PROGRESSI**:

**ATTORE**: Sistema

**DESCRIZIONE**: Il sistema assicura che i progressi dell'utente nel gioco vengano salvati automaticamente per evitare la perdita di dati.

**PRECONDIZIONI**:

- La verifica delle licenze è andata a buon fine.

- Il gioco è stato avviato correttamente.

- L'utente sta attivamente giocando.

**FLUSSO PRINCIPALE**:

- Il sistema monitora costantemente lo stato del gioco e i progressi dell'utente (es. posizione, oggetti raccolti, dialoghi completati, scelte effettuate).

- A intervalli predefiniti o in punti specifici della storia, il sistema esegue un salvataggio automatico dei dati di gioco.

- Il sistema notifica all'utente che il salvataggio è stato completato (es. breve icona a schermo).

**FLUSSO ALTERNATIVO**:

- Errore durante il salvataggio: In rari casi, potrebbe verificarsi un errore durante il salvataggio. Il sistema dovrebbe tentare di salvare nuovamente o informare l'utente del problema; in caso di ulteriori problemi, contattare il servizio clienti della piattaforma di gioco.




Il sistema dovrà garantire la possibilità di fare un salvataggio automatico frequentemente.

**REQUISITI FUNZIONALI**

FR1: Controlli e movimento

FR2: Interazione con gli NPC

FR3: Statistiche e progressione

FR4: Inventario ed equipaggiamento

FR5: Gestione delle quest

FR6: Commercio ed economia

FR7: User Interface e User Experience

FR8: Stato del gioco

FR9: Narrativa ed eventi scriptati

**FR1: Controlli e movimento**
-Il sistema deve visualizzare il mondo di gioco da una prospettiva 3D.

-Il sistema deve permettere al giocatore di controllare il proprio personaggio usando dei dispositivi di input (tastiera o joypad).

-Il sistema deve permettere al personaggio di muoversi in maniera libera all’interno dell’area di gioco.

-Il sistema deve gestire le collisioni tra il personaggio del giocatore ed oggetti non penetrabili, come rocce, costruzioni, NPC, ecc.

-Il sistema deve permettere al personaggio del giocatore di transitare tra diverse zone della mappa .

-Il sistema deve permettere al personaggio di interagire con oggetti specifici all’interno dell’ambiente di gioco mediante specifiche azioni e rispettando specifici vincoli di vicinanza.

**FR2: Interazione con gli NPC**
-Il sistema deve popolare il mondo con degli NPC.

-Il sistema deve permettere ai giocatori di inizializzare un dialogo con gli NPC.

-Il sistema deve mostrare il testo del dialogo in una parte dedicata della UI.

-Il sistema deve supportare dialoghi ad opzioni multiple.

-Gli NPC devono poter assegnare quest al giocatore.

-Alcuni NPC potranno mostrare schemi di movimento di base (come camminare lungo percorsi predefiniti).


**TFR3: STATISTICHE E PROGRESSIONE**
-Il sistema fornisce le seguenti statistiche potenziabili dal giocatore:
-HP (Punti Salute) Rappresenta la salute fisica del personaggio giocabile
-MP (Mental Point) Rappresenta le capacità del detective nella concetrazione durante l'investigazione, l'analisi e la deduzione delle scene del crimine.
-IQ (Intelligenza) Rappresenta statistica primaria e fondamentale, determina la capacità di risolvere enigmi, scovare indizi, compredere informazioni complesse e migliorie nelle abilità d'investigazione.
-Velocità: Rappresenta la statistica di velocità delle operazioni durante le varie operazioni di Gameplay
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
















