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


def run ():
    urll = []

    while True:
        url_s = input("Inserisci i link animeSaturn da scaricare:")
        if url_s == "":
            break
        urll.append(url_s)
    
    
    for url in urll:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service (executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

        # add ublock extension
        driver.get("https://chromewebstore.google.com/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=it")
        time.sleep(2)
        keyboard = Controller()

        # print(driver.find_element(By.CLASS_NAME, "content-container").text.strip())
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
        # keyboard.press(Key.tab)
        # keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(2)

        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
       
        time.sleep(10)
        # -------------

        # creazione cartella con nome anime proprio
        driver.get(url)
        title = driver.find_element(By.CLASS_NAME, "title").text.strip().replace(":", "_").replace("!","").replace("?", "").replace("à", "a").replace("ò", "o").replace("ù", "u").replace("è", "e").replace("\n", "").replace(" ", "_")
        # print(title + "\n\n")

        # scraper = cloudscraper.create_scraper()
        # page_raw = scraper.get (url)

        # soup = BeautifulSoup(page_raw.text, "html.parser")
        # title = soup.find(class_ = "title").text.strip().replace(":", "_").replace("!","").replace("?", "").replace("à", "a").replace("ò", "o").replace("ù", "u").replace("è", "e").replace("\n", "").replace(" ", "_")


        dir = str(title.replace("\n", ""))
        # creare una nuova cartella con il titolo dell'anime
        cartellaDaVerificare=Path(dir)

        if not cartellaDaVerificare.is_dir():
            os.mkdir(dir)
            with open (dir + "\\" + title + ".txt", "w") as f:
                f.write("")
            # os.system("chmod ugo+rwx " + dir + "/")                      # permessi di scrittura modifica e lettura


        # inizio scraping
        try:
            driver.find_element(By.XPATH, "/html/body").click()
        except:
            pass
        # time.sleep(1)

        #time.sleep(1)
        if len(driver.window_handles) > 1:
            keyboard = Controller()
            keyboard.press(Key.ctrl)
            keyboard.press('w')
            keyboard.release(Key.ctrl)
            keyboard.release('w')
        

        # prendere il numero di epidsodi:      /html/body/div/main/div/div[3]/div[2]/b/b/div[1]/div/div/div[4]    
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


        time.sleep(1)
        # print (pages)


        with open (dir + "/" + title + ".txt", "r") as f:
            lista_gia_scaricati = f.readlines()


        
        for i in tqdm (range (1, pages+1)):

            if len(driver.window_handles) > 1:
                keyboard = Controller()
                keyboard.press(Key.ctrl)
                keyboard.press('w')
                keyboard.release(Key.ctrl)
                keyboard.release('w')

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
            if len(driver.window_handles) > 1:
                keyboard = Controller()
                keyboard.press(Key.ctrl)
                keyboard.press('w')
                keyboard.release(Key.ctrl)
                keyboard.release('w')
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

            # keyboard.press(Key.ctrl)
            # keyboard.press('w')
            # keyboard.release(Key.ctrl)
            # keyboard.release('w')
            # time.sleep(1)

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
            link = str(link_raw).split("https://")[1].split("\"")[0].replace("amp;", "")
            link = "https://" + link
            # print(link)

            

        
            html = requests.get(link)
            s = BeautifulSoup(html.content, "html.parser" )
            link_download = str(s).split("window.downloadUrl = '")[1].split("'")[0]
            nome_file_scaricato = link_download.split("filename=")[1]
            # print(nome_file_scaricato)

            if "%2C" in nome_file_scaricato:
                nome_file_scaricato = nome_file_scaricato.replace("%2C", ",")
            if "%3A" in nome_file_scaricato:
                nome_file_scaricato = nome_file_scaricato.replace("%3A", "_")
        

            if nome_file_scaricato + "\n" in lista_gia_scaricati:
                # if  finish_time - start_time > 19.9:
                #     driver.find_element(By.XPATH, "/html/div").click()
                #     #time.sleep(1)
                #     keyboard = Controller()
                #     keyboard.press(Key.ctrl)
                #     keyboard.press('w')
                #     keyboard.release(Key.ctrl)
                #     keyboard.release('w')
                #     start_time = time.time()
                continue

            if len(driver.window_handles) > 1:
                keyboard = Controller()
                keyboard.press(Key.ctrl)
                keyboard.press('w')
                keyboard.release(Key.ctrl)
                keyboard.release('w')
            time.sleep(1)
            driver.get(link_download)
            
            # print(driver.find_element(By.CLASS_NAME, "description").text)
  
            # keyboard.press(Key.ctrl)
            # keyboard.press('w')
            # keyboard.release(Key.ctrl)
            # keyboard.release('w')
            # time.sleep(1)

            try:
                nome_file_scaricato = nome_file_scaricato.replace("%3F%21", "_!")
            except:
                pass
            print(nome_file_scaricato)
            
            # bool = True
            # while bool:
            #     try:
            #         shutil.move(r"C:\Users\UTENTE\Downloads" + nome_file_scaricato , dir)
            #         time.sleep(1)
            #         print("Provo spostare")
            #         bool = False
            #     except:
            #         print("Non sposto")
            #         time.sleep(5)
                    

            while not exists(r"C:\Users\UTENTE\Downloads" + "\\" + nome_file_scaricato ):  ########## MODIFICARE CON VOSTRO NOME UTENTE ########################
                time.sleep(5)

            # creazione file di salvataggio e scrittura
            
            with open (dir + "\\" + title + ".txt", "a") as f:
                f.write(nome_file_scaricato + "\n")
            
            try:
                shutil.move(r"C:\Users\UTENTE\Downloads" + "\\" + nome_file_scaricato , dir)
                time.sleep(1)
            except:
                os.system("rm " + r"C:\Users\UTENTE\Downloads" + "\\" + nome_file_scaricato)

            try:
                driver.find_element(By.XPATH, "/html/div").click()
                #time.sleep(1)
                keyboard = Controller()
                keyboard.press(Key.ctrl)
                keyboard.press('w')
                keyboard.release(Key.ctrl)
                keyboard.release('w')
                time.sleep(1)
            except:
                pass

            if i == pages:
                os.system("rm " + dir + "\\" + title + ".txt")
            


run ()
