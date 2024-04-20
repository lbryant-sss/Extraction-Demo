# COVID-19 Data Extraction with Python

This Python project demonstrates two techniques for data extraction: using APIs and web scraping with Selenium.

## API Data Extraction

This script utilizes the `requests` library to fetch data from the [COVID-19 API](https://covid-api.com/api/).

**Dependencies:** pandas, requests, pprint

**Steps:**

1. Imports necessary libraries.
2. Defines the API endpoint URL.
3. Sends a GET request to the API using `requests.get`.
4. Checks the response status code and reason phrase.
5. Parses the JSON response using `json.loads`.
6. Pretty-prints the extracted data using `pprint.PrettyPrinter`.
7. Identifies the data type using `type()`.

**Note:** This snippet retrieves a high-level summary of COVID-19 data. The API offers various endpoints for more granular data exploration.

## Web Scraping with Selenium

This script demonstrates web scraping with Selenium to extract specific data from a website. Here, it retrieves the last price displayed on Yahoo Finance's stock lookup page.

**Dependencies:** selenium, beautifulsoup4

**Steps:**

1. Imports required libraries: selenium for browser automation and beautifulsoup4 for HTML parsing.
2. Initializes a ChromeDriver instance.
3. Defines the target URL.
4. Navigates the browser to the target URL.
5. Retrieves the HTML source code using `driver.page_source`.
6. Quits the browser instance.
7. Parses the HTML using BeautifulSoup.
8. Locates the desired element (last price) using element class and attributes.
9. Prints the extracted data (last price).

**Note:** This is a basic example. Real-world web scraping might require more sophisticated techniques to handle 
dynamic content and avoid breaking websites' terms of service.

## Further Exploration:

- Explore the COVID-19 API documentation for specific data points.
- Implement error handling for API requests and web scraping.
- Clean and transform the extracted data for further analysis.
- Save the extracted data to a file (CSV, Excel) for later use.

This project showcases how to extract data from various sources using Python libraries. Feel free to 
adapt and extend this code for your specific data extraction needs.
