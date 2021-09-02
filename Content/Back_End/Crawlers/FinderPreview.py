from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import gc


### Code permettant de test le résultat d'un crawl avant de l'implémenter dans le progamme
### à utiliser comme programme stand alone

def run():
    #Instatiation du crawler
    base_url = "https://www.genybet.fr/"
    liste_des_courses = []

    fireFoxOptions = Options()
    fireFoxOptions.add_argument("--headless")

    driver = webdriver.Firefox(options=fireFoxOptions,executable_path='geckodriver.exe')

    driver.get(base_url)
    
    html = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(html, 'html.parser')

    #Trouve toutes les courses du jour
    for champ in soup.findAll("div", {"class": "timeline-container"}):
        for course in champ.findAll("a"):
            try:
                liste_des_courses.append(str(course.get("href")))
            except Exception as e:
                print(e)
                pass
            
    driver.quit()
    gc.collect()

    return liste_des_courses