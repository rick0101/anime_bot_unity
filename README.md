# Script per scaricare anime

Questo script Python automatizza il processo di download di tutti gli episodi di una serie anime. E' per `WINDOWS`, ma può essere facilmente adattato anche per Linux, è necessario cambiare il chromedriver utilizzato da selenium.

1. Scrape della pagina principale per identificare ed estrarre collegamenti ai singoli episodi.
2. Scarica in sequenza ogni episodio in una directory specificata.
3. Gestisce potenziali interruzioni e riprende i download se necessario.


## Caratteristiche
Scraping automatico dei collegamenti agli episodi dalla pagina principale.
Download sequenziale degli episodi.
Ripresa dei download interrotti.


## Funzionamento
Il programma utilizza un simulatore browser per bypassare delle difese anti-scraping di alcuni siti.
Per prima cosa aggiunge ublock a chrome, ogni volta che avviate il programma (tranquilli che chrome usato da selenium e il vostro chrome sono 2 cose completamente separate. Tutto quello fatto su selenium non va a impattare il vostro chrome personale), 
questo è essenziale per evitare pubblicità e blocker che renderebbero impossibile predire il comportamento della pagina.
Fatto quello andrà a creare una cartella contenente il nome dell'anime nella vostra directory attuale, e un file .txt che conterrà gli eppisodi scaricati. Finito di scaricarli tutti, il file .txt verrà automaticamente eliminato (serve solo per tenere traccia
di eventuali eppisodi non ancora scaricati).
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
cd anime_bot_unity
```
Se ricevi qualche errore prova a scaricare il file zip, sotto "codice"

2. Installare i pacchetti richiesti (UNA RIGA PER COMANDO):
```bash
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

3. MODIFICA

`Apri "anime_scraping_unity.py" con blocco note, vai su modifica, poi su sostituisci, e sostituisci UTENTE con il tuo nome del pc.`


4. Utilizzo
Esegui lo script:
```bash
python anime_scraping_unity.py
```
Inserisci ora 1 link per volta degli anime da scaricare, e premi invio. 
Quando avrai finito di inserire i links per gli anime, ripremi invio senza inserire nulla.

## AVVERTIMENTO

Se smette di funzionare, prova a scaricare la versione più recente di Chromedriver in base al tuo sistema operativo.
Link al `driver Chrome:` https://googlechromelabs.github.io/chrome-for-testing/
Vai su Stable e dalla riga 6 alla riga 10 hai i collegamenti per scaricare Chromedriver in base al tuo sistema operativo.

Se avete scaricato solo alcuni eppisodi di un anime e poi interrompete, alla riapertura del programma verranno scaricati solo gli eppisodi mancanti.
Il tutto è tenuto traccia dal file .txt presente nella cartella dell'anime, il quale, una volta arrivato alla fine, verrà automaticamente eliminato.


## TUTORIAL VIDEO

https://github.com/user-attachments/assets/649006ab-c8a9-459f-a63e-f163ecd9030b


https://github.com/user-attachments/assets/78cbf8db-c419-44da-b6aa-895633c487ba



## Contributi


1. Effettuare il fork del repository.
2. Crea un nuovo ramo (git checkout -b feature-branch).
3. Applica le tue modifiche (git commit -am 'Aggiungi nuova funzionalità').
4. Push sul ramo (git push origin feature-branch).
5. Crea una nuova richiesta di pull.
