from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import gc



### Code permettant de test le résultat d'un crawl avant de l'implémenter dans le progamme
### à utiliser comme programme stand alone




def run():
    #Instatiation du crawler
    participantDict = {}
    currentRaceName = ""

    url = "https://www.genybet.fr/courses/partants-pronostics/1255804"
    fireFoxOptions = Options()
    fireFoxOptions.add_argument("--headless")

    driver = webdriver.Firefox(options=fireFoxOptions,executable_path='geckodriver.exe')
    driver.get(url)
    
    html = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(html, 'html.parser')

        #Trouve toutes les courses du jour
    
    for raceName in soup.findAll("h3",{"class" : "reunion-description"}):
        currentRaceName = raceName.text

    naming = True
    currentName = ""
    for tab in soup.findAll("table",  {"class":["table", "condensed", "striped", "ca" ]}):
        for participant in tab.findAll("tr"):
            
            for spec in participant.findAll("td"):
                try:
                    if naming :
                        currentName = str(spec.text).replace('\n','').replace('\t','')    
                        participantDict[currentName] = []
                        naming = False
                    else:
                        participantDict[currentName].append(str(spec.text).replace('\n','').replace('\t',''))
                except Exception as e:
                    print(e)
                    pass

            naming = True
        #Les renvoies

    participantDict = {key:value for key, value in participantDict.items() if len(value) > 5}
        
        
    driver.quit()
        
    gc.collect()
 
    return [currentRaceName,participantDict]

runResult = run()

print(runResult[0])
del runResult[1][""]
for key,value in runResult[1].items():
    print(key,value)
