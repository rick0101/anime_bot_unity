from bs4 import BeautifulSoup
from tqdm import tqdm
import time
import os
import shutil
from pathlib import Path
from pynput.keyboard import Key, Controller
import requests
import datetime
from os.path import exists

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# aggiungo uBlock (estensione) a chrome
def key_pressing_uBlock(driver):
    driver.get("https://chromewebstore.google.com/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=it")
    time.sleep(2)
    keyboard = Controller()
    try:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(2)
    except:
        pass  
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

# prelevo il numero di puntate dell'anime
def pagine (driver):
    try:
        driver.find_element(By.XPATH, "/html/body").click()
    except:
        pass
    try:
        add = 0
        pages = driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[4]").text.splitlines()
        if pages[0] == "0":
            add +=1
        for q in pages:
            if "." in q:
                add += 1                                           
        pages = int(driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[4]").text.splitlines()[-1]) + add
        if "-" in pages:
            pages = int(driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[4]").text.splitlines()[-2]) + 1 + add
        pages = int(pages)
    except:
        pass
    try:
        add = 0
        pages = driver.find_element(By.XPATH,"/html/body/div/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[4]").text.splitlines()
        if pages[0] == "0":
            add +=1
        for q in pages:
            if "." in q:
                add += 1
        pages = int(driver.find_element(By.XPATH,"/html/body/div/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[4]").text.splitlines()[-1]) + add
        if "-" in pages:
            pages = int(driver.find_element(By.XPATH,"/html/body/div/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[4]").text.splitlines()[-2]) + 1 + add
        pages = int(pages)
    except:
        pass

    try:
        add = 0
        pages = driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[2]/div[2]/b/b/div[1]/div/div/div[4]").text.splitlines()
        if pages[0] == "0":
            add +=1
        for q in pages:
            if "." in q:
                add += 1
        pages = int(driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[2]/div[2]/b/b/div[1]/div/div/div[4]").text.splitlines()[-1]) + add
        if "-" in pages:
            pages = int(driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[2]/div[2]/b/b/div[1]/div/div/div[4]").text.splitlines()[-2]) + 1 + add
        pages = int(pages)
    except:
        pass
    try:
        add = 0
        pages = driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[5]").text.splitlines()
        if pages[0] == "0":
            add +=1
        for q in pages:
            if "." in q:
                add += 1
        pages = int(driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[5]").text.splitlines()[-1]) + add
        if "-" in pages:
            pages = int(driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[5]").text.splitlines()[-2]) + 1 + add
        pages = int(pages)
    except:
        pass
    try:
        add = 0
        pages = driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[3]/div[2]/div[1]/div/div/div[4]").text.splitlines()
        if pages[0] == "0":
            add +=1
        for q in pages:
            if "." in q:
                add += 1
        pages = int(driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[3]/div[2]/div[1]/div/div/div[4]").text.splitlines()[-1]) + add
        if "-" in pages:
            pages = int(driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div[3]/div[2]/div[1]/div/div/div[4]").text.splitlines()[-2]) + 1 + add
        pages = int(pages)
    except:
        pass
    return pages

# controllo quante schede aperte ci sono e chiudo quelle aperte in più
def check_open_pages (driver):
    if len(driver.window_handles) > 1:
        keyboard = Controller()
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release(Key.ctrl)
        keyboard.release('w')

# torno su (per bypassare anti-scraping) scroll fisico pagina
def scroll_up ():
    keyboard = Controller()
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.up)
    keyboard.release(Key.up)

# ottengo il link grezzo per il download
def get_link_raw (pages, driver, i):
    try:
        if pages > 100:                                         
            driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[5]/div[" + str(i) + "]").click()
        else:
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[4]/div[" + str(i) + "]").click()
            except:
                pass
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/div[1]/div/div/div[4]/div["+ str(i) + "]").click()
            except:
                driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[2]/b/b/div[1]/div/div/div[4]/div[" + str(i) + "]").click()
    except:
        scroll_up()
        try:
            if pages > 100:
                driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[5]/div[" + str(i) + "]").click()
            else:
                try:
                    driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[4]/div[" + str(i) + "]").click()
                except:
                    pass
                try:
                    driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/div[1]/div/div/div[4]/div["+ str(i) + "]").click()
                except:
                    driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[2]/b/b/div[1]/div/div/div[4]/div[" + str(i) + "]").click()
        except:
            try:
                driver.find_element(By.XPATH, "/html/div").click()
            except:
                pass
            if pages > 100:
                driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[5]/div[" + str(i) + "]").click()
            else:
                try:
                    driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[4]/div[" + str(i) + "]").click()
                except:
                    pass
                try:
                    driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/div[1]/div/div/div[4]/div["+ str(i) + "]").click()
                except:
                    pass
                try:
                    driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[2]/b/b/div[1]/div/div/div[4]/div[" + str(i) + "]").click()
                except:
                    pass
    check_open_pages(driver)
    try:    
        driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[2]/div/div/iframe").click()
    except:
        pass
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/iframe").click()
    except:
        pass
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[2]/b/b/div[1]/div/div/div[2]/div/div/iframe").click()
    except:
        pass

    try:    
        driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[2]/div/div/iframe").click()
    except:
        pass
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/iframe").click()
    except:
        pass
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[2]/b/b/div[1]/div/div/div[2]/div/div/iframe").click()
    except:
        pass
    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys(Keys.SPACE)
    actions.perform()

    try:
        link_raw = (driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[2]/div/div/iframe").get_attribute('outerHTML'))
    except:
        pass
    try:
        link_raw = (driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/iframe").get_attribute('outerHTML'))
    except:
        pass
    try:
        link_raw = (driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[2]/b/b/div[1]/div/div/div[2]/div/div/iframe").get_attribute('outerHTML'))
    except:
        pass

    return link_raw

# correggo il nome se "sporco"
def aggiusta_nome (nome):
    if "%2C" in nome:
        nome_file_scaricato = nome.replace("%2C", ",")
        try:
            nome_file_scaricato = nome.replace("%3F%21", "_!")
        except:
            pass
        return nome_file_scaricato
    if "%3A" in nome:
        nome_file_scaricato = nome.replace("%3A", "_")
        try:
            nome_file_scaricato = nome.replace("%3F%21", "_!")
        except:
            pass
        return nome_file_scaricato
    return nome

#creazione cartella nome anime
def creazione_cartella (cartellaDaVerificare, title):
    if not cartellaDaVerificare.is_dir():
        os.mkdir(dir)
        with open (dir + "\\" + title + ".txt", "w") as f:
            f.write("")
        # os.system("chmod ugo+rwx " + dir + "/")                      # permessi di scrittura modifica e lettura (solo per linux)



def run ():
    urll = []

    while True:
        url_s = input("Inserisci i link animeSaturn da scaricare: ")
        if url_s == "":
            break
        urll.append(url_s)
    
    
    for url in urll:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service (executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

        # ---chromium estensione---
        key_pressing_uBlock(driver)
       
        time.sleep(10)
        # -------------


        # creazione cartella con nome anime proprio
        driver.get(url)
        title = driver.find_element(By.CLASS_NAME, "title").text.strip().replace(":", "_").replace("!","").replace("?", "").replace("à", "a").replace("ò", "o").replace("ù", "u").replace("è", "e").replace("\n", "").replace(" ", "_")
        # print(title + "\n\n")
        dir = str(title.replace("\n", ""))
        
        # creare una nuova cartella con il titolo dell'anime
        cartellaDaVerificare=Path(dir)
        creazione_cartella(cartellaDaVerificare, title)
        


        # inizio scraping

        # chiususra pagine aperte per pubblicità     
        check_open_pages(driver)
        
        # prendere il numero di epidsodi: 
        pages = pagine(driver)

        time.sleep(1)
        # print (pages)

        with open (dir + "/" + title + ".txt", "r") as f:
            lista_gia_scaricati = f.readlines()
        
        for i in tqdm (range (1, pages+1)):

            # chiususra pagine aperte per pubblicità 
            check_open_pages(driver)

            # link della puntata 
            link_raw = get_link_raw(pages, driver, i)
            
            link = str(link_raw).split("https://")[1].split("\"")[0].replace("amp;", "")
            link = "https://" + link
            # print(link)

        
            html = requests.get(link)
            s = BeautifulSoup(html.content, "html.parser" )
            link_download = str(s).split("window.downloadUrl = '")[1].split("'")[0]
            nome_file_scaricato = link_download.split("filename=")[1]
            # print(nome_file_scaricato)

            # pulisco il nome
            nome_file_scaricato = aggiusta_nome (nome_file_scaricato)

            # se è già stato scaricato l'eppisodio, skip al prossimo
            if nome_file_scaricato + "\n" in lista_gia_scaricati:
                continue

            check_open_pages(driver)


            time.sleep(1)
            driver.get(link_download)

            
            print(nome_file_scaricato)
            
            # FInchè non ha finito il download, aspetta 5 secondi... 
            name = os.getlogin()
            while not exists(r"C:\\Users\\"+name+"\Downloads\\"+ nome_file_scaricato): 
                time.sleep(5)

            # creazione file di salvataggio e scrittura
            with open (dir + "\\" + title + ".txt", "a") as f:
                f.write(nome_file_scaricato + "\n")
            # sposto l'eppisodio scaricato nella cartella creata "dir" con il nome dell'anime
            try:
                shutil.move(r"C:\\Users\\"+name+"\Downloads\\"+ nome_file_scaricato, dir)
                time.sleep(1)
            except:
                # se è già presente, la elimito dalla cartella downloads
                os.system(r"C:\\Users\\"+name+"\Downloads\\"+ nome_file_scaricato)

            # arrivato alla fine, elimino il file .txt creato per tenere traccia di dove ero arrivato
            if i == pages:
                os.system("rm " + dir + "\\" + title + ".txt")
            


run ()
