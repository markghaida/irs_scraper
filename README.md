<img src="Irs Webscraper GitHub ReadMe Cover.png" alt="IRS Webscraper" width="1200"/>

## Environment

<br>

    - Version of Python: 3.9.2

    - Version of pip: 21.0.1
        - if not installed, enter these commands on terminal in the same directory as "irs_scraper":
            - 1. curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            - 2. python get-pip.py

    - Required Version of Google Chrome: 89.0.4389.90

    - Required version of ChromeDriver: 89.0.4389.23 (included in requirements.txt)

    - Only other dependency is "selenium" (included in requirements.txt)

    - Ensure that when running any of the two utilities, the terminal is on the same
    window as the chrome browser.  There can be interferences with the script while not 
    on the same window

    - make sure to be in the "irs_scraper" directory when performing any commands 
    regarding the script

    - The script takes input parameters via the command line.  Make sure to follow the prompts on the screen, 
    and the specified formats when inputting text!

    - For Part 1, JSON is outputted via terminal. Keep in mind, Python returns JSON as a string, so the outputted format is still
    congruent with the instructions, despite there being single quotes wrapped around each dictionary.

<br>

## How to Run Script

<br>

    1. unzip file attached 

    2. open terminal 

    3. cd into the unzipped folder "irs_scraper" in terminal 

    4. when inside "irs_scraper" directory, install all requirements for this script
    by running the command: pip install -r requirements.txt

        - *if pip not installed, refer back to the notes above on installation*

    5. while still in the "irs_scraper" directory, to run the first utility ("irs_json_return.py"), 
    	run command: python3 irs_json_return.py

    6. The chrome window should open, and make sure to remain on that window until the script is complete.

    7. while still in the "irs_scraper" directory, to run the second utility ("irs_form_dlnd.py"), 
    	run command: python3 irs_form_dlnd.py

    8. The chrome window should open, and make sure to remain on that window until the script is complete.

<br>
    
