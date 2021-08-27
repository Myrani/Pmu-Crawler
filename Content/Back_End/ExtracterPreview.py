from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def run():
    #Instatiation du crawler
    participantDict = {}

    fireFoxOptions = Options()
    fireFoxOptions.add_argument("--headless")

    driver = webdriver.Firefox(options=fireFoxOptions,executable_path='geckodriver.exe')
    driver.get("https://www.genybet.fr/courses/partants-pronostics/1254328")
    
    html = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    #Trouve toute la data des participants
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
            
    return participantDict

for key,value in run().items():
    print(key,value)
