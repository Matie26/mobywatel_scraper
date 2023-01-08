from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import json
 
def get_element(driver, css_selector):
    return  WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CSS_SELECTOR, css_selector))
 
css_selectors = {
    "profil_zaufany": ("button.icon-button:nth-child(2)", {
        "mail": ".data-list > div:nth-child(1) > span:nth-child(1)",
        "tel": ".data-list > div:nth-child(2) > span:nth-child(1)"
    }),
    "rejestr_danych_kontakotowych": ("button.icon-button:nth-child(3)", {
        "kontakt_tel": ".data-list > div:nth-child(1) > span:nth-child(1)",
        "kontakt_mail": ".data-list > div:nth-child(2) > span:nth-child(1)"
    }),
    "rejestr_pesel": ("button.icon-button:nth-child(4)", {
        "imiona": "div.border-top-line:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
        "nazwisko": "div.border-top-line:nth-child(2) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)",
        "nazwisko_rodowe": "div.border-top-line:nth-child(2) > div:nth-child(2) > div:nth-child(3) > span:nth-child(1)",
        "stan_cywilny": "div.border-top-line:nth-child(2) > div:nth-child(2) > div:nth-child(4) > span:nth-child(1)",
        "data_urodzenia": "div.ng-star-inserted:nth-child(5) > span:nth-child(1)",
        "miejsce_urodzenia": "div.ng-star-inserted:nth-child(6) > span:nth-child(1)",
        "kraj_urodzenia": "div.ng-star-inserted:nth-child(7) > span:nth-child(1)",
        "oznaczenie_aktu_urodzenia": "div.ng-star-inserted:nth-child(8) > span:nth-child(1)",
        "urzad_wydajacy_akt": "div.ng-star-inserted:nth-child(9) > span:nth-child(1)",
        "plec": "div.ng-star-inserted:nth-child(10) > span:nth-child(1)",
        "pesel": "div.ng-star-inserted:nth-child(11) > span:nth-child(1)",
        "obywatelstwo": "div.ng-star-inserted:nth-child(12) > span:nth-child(1)",
        "imie_ojca": "div.border-top-line:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
        "nazwisko_rodowe_ojca": "div.border-top-line:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)",
        "imie_matki": "div.border-top-line:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > span:nth-child(1)",
        "nazwisko_rodowe_matki": "div.border-top-line:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(4) > span:nth-child(1)"
    }),
    "rejestr_dowodow_osobistych": ("button.icon-button:nth-child(5)", {
        "numer_dowodu_osobistego": "div.data-list:nth-child(3) > div:nth-child(1) > span:nth-child(1)",
        "organ_wydajacy": "div.data-list:nth-child(3) > div:nth-child(2) > span:nth-child(1)",
        "status_dowodu": "span.fw-bold",
        "data_waznosci_dowodu": "div.data-list:nth-child(3) > div:nth-child(5) > span:nth-child(1)",
        "status_warstwy_elektronicznej_dowodu": "div.ng-star-inserted:nth-child(6) > span:nth-child(1)",
    }),
    "dane_zameldowania": ("button.icon-button:nth-child(6)", {
        "miejscowosc": ".data-list > div:nth-child(1) > span:nth-child(2)",
        "wojewodztwo": ".data-list > div:nth-child(2) > span:nth-child(2)",
        "powiat": ".data-list > div:nth-child(3) > span:nth-child(2)",
        "gmina": ".data-list > div:nth-child(4) > span:nth-child(2)",
        "kod_pocztowy": "div.ng-star-inserted:nth-child(5) > span:nth-child(2)",
        "ulica": "div.ng-star-inserted:nth-child(6) > span:nth-child(2)",
        "numer_domu": "div.ng-star-inserted:nth-child(7) > span:nth-child(2)",
        "numer_lokalu": "div.ng-star-inserted:nth-child(8) > span:nth-child(2)",
        "data_zameldowania_na_pobyt_staly": "div.ng-star-inserted:nth-child(9) > span:nth-child(2)"
    })
}
 
if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://serwis.epuap.gov.pl/mlpz/login?ORIGIN=nforms_EServices")
    WebDriverWait(driver, 180).until(lambda driver: driver.current_url == "https://www.mobywatel.gov.pl/mObywatel")
    driver.get("https://www.mobywatel.gov.pl/mObywatel/twoje-dane")
 
    data = {}
    for section in css_selectors:
        button = get_element(driver, css_selectors[section][0])
        button.click()
        for field in css_selectors[section][1]:
            try: 
                data[field] = get_element(driver, css_selectors[section][1][field]).text
            except Exception as e:
                print(e)
                data[field] = 'error'
                
    #make pretty string from dict and output as txt
    data_string = json.dumps(data, indent = 4, sort_keys = True)
    text_file = open('dane.txt', 'w')
    text_file.write(data_string)
    text_file.close()
    
    #make df from dict
    df = pd.DataFrame.from_dict(data, orient = 'index', columns = ['WARTOSC'])
    df.reset_index(inplace = True)
    df.rename(columns = {'index':'POLE'}, inplace = True)
    
    #make matplotlib table from df
    fig, ax = plt.subplots(figsize = (12,4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText = df.values, colLabels = df.columns, loc = 'center', cellLoc = 'left', colColours =    ['moccasin', 'moccasin'], colWidths = [0.33, 0.33])
    
    #save table as pdf
    pp = PdfPages('dane.pdf')
    pp.savefig(fig, bbox_inches = 'tight')
    pp.close()
