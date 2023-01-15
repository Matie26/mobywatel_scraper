from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from css_selectors import selectors
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import json


def get_element(driver, css_selector):
    return WebDriverWait(driver, timeout=5).until(
        lambda d: d.find_element(By.CSS_SELECTOR, css_selector)
    )


def save_data(data):
    # make pretty string from dict and output as txt
    data_string = json.dumps(data, indent=4, sort_keys=True)
    text_file = open("dane.txt", "w")
    text_file.write(data_string)
    text_file.close()
    print("Data saved to file: dane.txt")

    # make df from dict
    df = pd.DataFrame.from_dict(data, orient="index", columns=["WARTOSC"])
    df.reset_index(inplace=True)
    df.rename(columns={"index": "POLE"}, inplace=True)

    # make matplotlib table from df
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis("tight")
    ax.axis("off")
    the_table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        loc="center",
        cellLoc="left",
        colColours=["moccasin", "moccasin"],
        colWidths=[0.33, 0.33],
    )

    # save table as pdf
    pp = PdfPages("dane.pdf")
    pp.savefig(fig, bbox_inches="tight")
    pp.close()
    print("Data saved to file: dane.pdf")


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://serwis.epuap.gov.pl/mlpz/login?ORIGIN=nforms_EServices")
    WebDriverWait(driver, 180).until(
        lambda driver: driver.current_url == "https://www.mobywatel.gov.pl/mObywatel"
    )
    driver.get("https://www.mobywatel.gov.pl/mObywatel/twoje-dane")

    data = {}
    for section in selectors:
        button = get_element(driver, selectors[section][0])
        button.click()
        for field in selectors[section][1]:
            try:
                data[field] = get_element(driver, selectors[section][1][field]).text
            except Exception as e:
                print(e)
                data[field] = "error"
    driver.quit()

    save_data(data)
