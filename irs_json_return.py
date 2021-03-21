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

if platform.system() == "Darwin" or platform.system() == "Linux":
    clear = lambda: os.system('clear')
elif platform.system() == "Windows":
    clear = lambda: os.system('cls')

def get_forms():
    global driver
    clear()
    inp = input("Which forms would you like to view? Please separate by a comma (e.g. Form 1040, Form W-2, Publ 1)  ")
    print("Retreiving JSON for:", inp.title())
    form_list = inp.split(", ")
    json_list = []
    for current_form in form_list:
        search = driver.find_element_by_id("searchFor")
        submit = driver.find_element_by_name("submitSearch")
        form_dictionary = {}
        search.clear()
        search.send_keys(current_form.title())
        submit.click()
        try:
            driver.implicitly_wait(6)
            time.sleep(3)
            driver.find_element_by_xpath("//th[@class='NumResultsDisplayed']/a[text()='200']").click()   
            main = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "main"))
            )
            odd_forms = main.find_elements_by_xpath( "//tr[@class='odd']")
            even_forms = main.find_elements_by_xpath( "//tr[@class='even']")
            all_forms = odd_forms + even_forms
            year_list = []
            for form_name in all_forms:
                form_number = form_name.find_element_by_class_name("LeftCellSpacer").text      
                if form_number == current_form.title():
                    year_list.append(form_name.find_element_by_class_name("EndCellSpacer").text)
                    form_dictionary["form_number"] = form_number
                    form_dictionary["form_title"] = form_name.find_element_by_class_name("MiddleCellSpacer").text 
            form_dictionary["min_year"] = min(year_list)
            form_dictionary["max_year"] = max(year_list)
            json_list.append(json.dumps(form_dictionary))
        finally:
            print(f"finished grabbing JSON for {current_form.title()}")
    clear()
    print(json_list)
    time.sleep(5)
    driver.quit() 
    return json_list

get_forms() 