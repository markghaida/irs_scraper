from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
from selenium import webdriver 
from pathlib import Path
from os import path
import os
import time
import json 
import sys  
import platform
import re
driver = webdriver.Chrome(executable_path=binary_path)
driver.get("https://apps.irs.gov/app/picklist/list/priorFormPublication.html") 
file_path = os.path.dirname(os.path.realpath(__file__))

if platform.system() == "Darwin" or platform.system() == "Linux":
    clear = lambda: os.system('clear')
elif platform.system() == "Windows":
    clear = lambda: os.system('cls')

print(platform.system())

def initial_inputs():  
    clear()
    form_name = input("Which form would you like to view? (e.g. Form 1040)  ")
    clear()
    form_name = form_name.title()
    year_range = input(f"Enter a range of years to get all {form_name}s during that timeframe (format --> '2008-2010')  ")
    clear()
    while not re.match(r'\d\d\d\d-\d\d\d\d', year_range):
        print("Incorrect format. Please try again")
        year_range = input(f"Enter a range of years to get all {form_name}s during that timeframe (format --> '2008-2010')  ")

    if re.match(r'\d\d\d\d-\d\d\d\d', year_range):
        years = year_range.split("-")
        if years[0] > years[1]:
            start_year = years[1]
            end_year = years[0]
        else:
            start_year = years[0]
            end_year = years[1]

    print(f'Downloading all {form_name}s from {year_range}')

    locate_elements(form_name, start_year, end_year)

def locate_elements(form_name, start_year, end_year):    
    global driver
    search_input = driver.find_element_by_id("searchFor")
    submit_button = driver.find_element_by_name("submitSearch")
    search_input.send_keys(form_name)
    submit_button.click()
    try:
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.find_element_by_xpath("//th[@class='NumResultsDisplayed']/a[text()='200']").click()
        main = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.ID, "main"))
        )
        odd_forms = main.find_elements_by_xpath( "//tr[@class='odd']")
        even_forms = main.find_elements_by_xpath( "//tr[@class='even']")
        all_forms = odd_forms + even_forms
        for form in all_forms:
            if form.find_element_by_class_name("LeftCellSpacer").text == form_name:
                form_year = form.find_element_by_class_name("EndCellSpacer").text
                if int(form_year) >= int(start_year) and int(form_year) <= int(end_year):
                    pdf_url = form.find_element_by_tag_name("a").get_attribute("href")
                    download_directory = f'{file_path}/{form_name}'
                    os.chdir(file_path)
                    if os.path.isdir(download_directory):
                        os.chdir(download_directory)
                    else:
                        os.mkdir(download_directory)
                        os.chdir(download_directory)
                    option_attributes = webdriver.ChromeOptions()
                    option_attributes.add_experimental_option("prefs", {
                        "download.default_directory": download_directory, #specifying the directory
                        "download.prompt_for_download": False, #downloads immediately
                        "download.directory_upgrade": True,
                        "plugins.always_open_pdf_externally": True 
                    })
                    driver = webdriver.Chrome(executable_path=binary_path, options=option_attributes)  
                    driver.get(pdf_url)
                    old_name = pdf_url.split("/")[-1]
                    new_name = f'{form_name} - {form_year}.pdf'
                    while not os.path.isfile(old_name):
                        time.sleep(1)
                    if os.path.isfile(old_name):
                        os.chdir(download_directory)
                        os.rename(old_name, new_name) 
                        driver.quit()
    finally:
        print("DONE")
    time.sleep(5)
    driver.quit()

initial_inputs() 