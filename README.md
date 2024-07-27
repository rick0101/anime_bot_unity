# Script per scaricare anime

Questo script Python automatizza il processo di download di tutti gli episodi di una serie anime. E' per WINDOWS, ma può essere facilmente adattato anche per Linux, è necessario cambiare il chromedriver utilizzato da selenium.

1. Scrape della pagina principale per identificare ed estrarre collegamenti ai singoli episodi.
2. Scarica in sequenza ogni episodio in una directory specificata.
3. Gestisce potenziali interruzioni e riprende i download se necessario.


## Caratteristiche
Scraping automatico dei collegamenti agli episodi dalla pagina principale.
Download sequenziale degli episodi.
Ripresa dei download interrotti.


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

Cerca "UTENTE" su VSCode (linea 397, 406, 409, previa ultieriore modifica) e modifica la parola "UTENTE" con il vostro nume utente del vostro PC.

3. Utilizzo
Esegui lo script:
```bash
python anime_scraping_unity.py
```

## AVVERTIMENTO

Se smette di funzionare, prova a scaricare la versione più recente di Chromedriver in base al tuo sistema operativo.
Link al driver Chrome: https://googlechromelabs.github.io/chrome-for-testing/
Vai su Stable e dalla riga 6 alla riga 10 hai i collegamenti per scaricare Chromedriver in base al tuo sistema operativo.


## Contributi

1. Effettuare il fork del repository.
2. Crea un nuovo ramo (git checkout -b feature-branch).
3. Applica le tue modifiche (git commit -am 'Aggiungi nuova funzionalità').
4. Push sul ramo (git push origin feature-branch).
5. Crea una nuova richiesta di pull.
