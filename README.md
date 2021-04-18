<img src="Irs Webscraper GitHub ReadMe Cover.png" alt="IRS Webscraper" width="1200"/>

NOTES:

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

    - I really enjoyed making this script, and I look forward to sharing my thoughts on each line of code :)

    - More elaborate notes, just in video format via Loom:
    https://www.loom.com/share/92f4f051f7444004a4a24822ef1a06b4


HOW TO RUN SCRIPT:

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
    
    
    `Honeycomb🐝` provides a way to search for all your bookmarks instead of sifting through folder after folder. The app's mission is to change the way we locate a saved bookmark.

Requires [Honeycomb🐝 front end](https://github.com/markghaida/voronoi-frontend-) and [Honeycomb🐝 back end](https://github.com/markghaida/voronoi-back).

## Live Link & Demo

Visit the [Live Link](https://honeycomb-app.netlify.app/) 

Watch the [Demo](https://www.loom.com/share/c99014653d9b42ef8ad25c5ed7229a85)

## Technologies Used

`Honeycomb🐝` is built with a `React` front end, a `Ruby on Rails` and `PostgreSQL` back end, `Paper.js` for the honeycomb-like design, and `Kumarai Gem` to srape all websites for necessary metadata. All styling was done with custom CSS. The live link for `Honeycomb🐝` is deployed on [Netlify](https://honeycomb-app.netlify.app/) with [Heroku](https://honeycomb-app.herokuapp.com/bookmarks) for the back end.

## Features

The name ***Honeycomb*** comes from the design of how the bookmarks are displayed.  The design is actually a voronoi diagram which creates a honeycomb effect.  Users are both able to create bookmarks and search for a saved bookmark. Once a user comes across a website they would like to save, they simply have to copy the url and paste it into the search bar.  It is now saved.  Simply search for the site by typing the title of the bookmarked site.

### Create a Bookmark

Users are able to save a bookmark.  Once you navigate to a website that you are interested in saving for later; copy the url address, paste it in the search bar, and then wait a couple seconds.  That's it! It's bookmarked.

<img src="How to Save a Bookmark.gif" alt="login" width="800"/>

### Search For a Bookmark

Once a bookmark is saved, simply begin searching for the website's name.  Honeycomb scrapes the bookmark's h1 title, body text, and main image.

<img src="How to Search For a Bookmark.gif" alt="create request 3" width="800"/>

## License

The [MIT](https://choosealicense.com/licenses/mit/) License

Copyright (C) 2021 - [Mark Ghaida](https://github.com/markghaida) 



