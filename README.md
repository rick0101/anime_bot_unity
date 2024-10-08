# Script per scaricare anime

Questo script Python automatizza il processo di download di tutti gli episodi di una serie anime. E' per `WINDOWS`, ma può essere facilmente adattato anche per Linux, è necessario cambiare il chromedriver utilizzato da selenium, l'estensione, e i vari percorsi che sono diversi tra windows a linux.


1. Scrape della pagina principale per identificare ed estrarre collegamenti ai singoli episodi.
2. Scarica in sequenza ogni episodio in una directory specificata.
3. Gestisce potenziali interruzioni e riprende i download se necessario.


## Requirements
Python 3


## Caratteristiche
Scraping automatico degli episodi dalla pagina principale.\
Download sequenziale degli episodi.\
Ripresa dei download interrotti.


## Funzionamento
Il programma utilizza un simulatore browser per bypassare delle difese anti-scraping di alcuni siti.
Per prima cosa aggiunge ublock a chrome, ogni volta che avviate il programma (tranquilli che chrome usato da selenium e il vostro chrome sono 2 cose completamente separate. Tutto quello fatto su selenium non va a impattare il vostro chrome personale), 
questo è essenziale per evitare pubblicità e blocker che renderebbero impossibile predire il comportamento della pagina.
Fatto quello, andrà a creare una cartella contenente il nome dell'anime nella vostra directory attuale e un file .txt che conterrà gli eppisodi scaricati.\
Finito di scaricarli tutti, il file .txt verrà automaticamente eliminato (serve solo per tenere traccia
di eventuali eppisodi non ancora scaricati).\
Al termine degli eppisodi, il programma finirà.

Per farlo andare dovrete inserire l'URL della pagina principale dell'anime sub ita che intendete scaricare, nota bene che potete inserire `più di un link alla volta`, l'importante è che all'ultimo link, premiat invio, poi di nuovo invio lasciando il campo:
"Inserisci anime da scaricare" `VUOTO!!`.
Vedi l video per il tutorial.


## Requisiti
"Leggi il file requirments.txt"


## Installazione

1. Clona il repository:
```bash
git clone https://github.com/rick0101/anime_bot_unity.git
```
```bash
cd anime_bot_unity
```
Se ricevi qualche errore prova a scaricare il file zip, sotto "codice"

2. Installare i pacchetti richiesti (UNA RIGA PER COMANDO):
```bash
python -m venv venv
```
```bash
./venv/Scripts/activate
```
```bash
pip install -r requirements.txt
```

3. Utilizzo
Esegui lo script:
```bash
python anime_scraping_unity.py
```
Inserisci ora 1 link per volta degli anime da scaricare, e premi invio. 
Quando avrai finito di inserire i links per gli anime, ripremi invio senza inserire nulla.

## AVVERTIMENTO

Se smette di funzionare, provate a scaricare la versione più recente di Chromedriver.\
Link al `driver Chrome:` https://googlechromelabs.github.io/chrome-for-testing/ \
Andate su Stable e dalla riga 6 alla riga 10 avete i collegamenti per scaricare Chromedriver in base al vostro sistema operativo (Questo bot funziona solo per Windows).

Per utilizzare lo script su OS linux, create prima una cartella chiamata "anime" nella seguente directory: `/home/USER/` dove al posto di USER ci sarà il nome del vostro PC. 
Questo perchè gli anime verranno aggiunti nella seguente directory finale `/home/USER/anime`, nel mio caso, il mio nome utente è "ricca" quindi risulterà: `/home/ricca/anime`.

Se avete scaricato solo alcuni eppisodi di un anime e poi interrompete, alla riapertura del programma verranno scaricati solo gli eppisodi mancanti.\
Il tutto è tenuto traccia dal file .txt presente nella cartella dell'anime, il quale, una volta arrivato alla fine, verrà automaticamente eliminato.


## TUTORIAL VIDEO




https://github.com/user-attachments/assets/3471c599-6829-4613-bc8b-91ff40ed44ea



https://github.com/user-attachments/assets/78cbf8db-c419-44da-b6aa-895633c487ba


