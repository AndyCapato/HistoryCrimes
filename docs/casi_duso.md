-----
title: CASI D'USO
-----

**INTERAGIRE CON GLI ELEMENTI E I PERSONAGGI DEL GIOCO**:

**ATTORI**: 

- Utente

- Personaggi non giocabili

**DESCRIZIONE**:

L'utente può interagire con gli elementi e i personaggi presenti nel mondo di gioco;

**PRECONDIZIONI**:

- La verifica delle licenze è andata a buon fine.

- Il gioco è stato avviato correttamente.

- L'utente ha interagito con un personaggio interrogabile.

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

- L'utente interagisce con un elemento o personaggio che offre un indizio, un oggetto o una dichiarazione.

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