# WebScraping
This is a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page using Jupyter Notebook, BeautifulSoup, Pandas, Requests/Splinter, mongo and Flask.
A singlePython dictionary containing all of the scraped data from above is returned to a flask application, which then populates the mongo database.
I've created a template HTML file called `index.html` that reads the mars data dictionary and display all of the data in the appropriate HTML elements which in turn is rendered on a browser.