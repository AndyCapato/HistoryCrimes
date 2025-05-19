-----
title: REQUISITI NON FUNZIONALI
-----
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














