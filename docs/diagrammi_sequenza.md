**CASO D'USO 1, INTERAGIRE CON GLI ELEMENTI E I PERSONAGGI DEL GIOCO:**

```mermaid
sequenceDiagram
actor Utente
actor Sistema
actor "Mondo di Gioco" as Mondo


Utente->>Sistema: Sceglie una direzione
Sistema->>Mondo: Sposta l'avatar nella direzione scelta
Mondo-->>Sistema: Mondo di gioco aggiornato
```

**CASO D'USO 2, RACCOLTA DI INDIZI, OGGETTI E DICHIARAZIONI:**
```mermaid
sequenceDiagram
actor Utente
    	actor Sistema
    	actor PNG


    Utente->>Sistema: Seleziona "Avvia conversazione" con Personaggio
    Sistema->>Sistema: Visualizza finestra/interfaccia di conversazione
    Sistema-->>Utente: Presenta opzioni di domanda
    Utente-->>Sistema: Seleziona tra le opzioni date da sistema
    Sistema-->>PNG: Invia selezione dall'utente
    PNG-->>Sistema: Risponde(basato su AI)
    Sistema-->>Utente: Visualizza risposta PNG
    loop Interazioni aggiuntive
        Utente->>Sistema: Seleziona domanda
        Sistema->>PNG: Invia selezione dall'utente
        PNG->>Sistema: Risponde (basato su AI e stato storia)
        Sistema->>Utente: Visualizza risposta PNG
    end
Utente->>Sistema: Conclude la conversazione
```

**CASO D'USO 3, EFFETTUARE SCELTE PER SBLOCCARE PERCORSI ALTERNATIVI:**
```mermaid
sequenceDiagram
actor Utente
    	actor Sistema
    	actor Inventario
    	actor Diario


    Sistema->>Sistema: Determina disponibilità Prova (oggetto, indizio)
    alt Elemento importante disponibile
        Sistema->>Utente: Notifica acquisizione (messaggio/animazione)
    end
   
    alt È un oggetto
        Sistema->>Inventario: Aggiungi oggetto
    else È un indizio
        Sistema->>Diario: Registra indizio
    end

```