1) SCRAPING DATA

#IMPORTING WANTED MODULES
1.from selenium import webdriver
2. from selenium.webdriver import ActionChains
3. from selenium.webdriver.common.by import By
4. from selenium.webdriver.common.keys import Keys
5. from selenium.common.exceptions import TimeoutException, NoSuchElementException
6. import time
7. import pandas as pd
8. from selenium.webdriver.support.ui import WebDriverWait
9. from selenium.webdriver.support import expected_conditions as EC

Summary
In short, this script imports various modules to:
Open and control a web browser with Selenium (webdriver).
Interact with web elements (e.g., clicks, typing, dragging) using ActionChains.
Locate elements on a webpage (By).
Handle key events (Keys).
Manage exceptions related to timeouts or missing elements.
Introduce delays (time.sleep) to wait for elements to load.
Store and manipulate data in a structured way (pandas).
Wait for specific conditions on the webpage to be met (WebDriverWait, expected_conditions).
These libraries and modules work together to automate web browsing tasks, commonly used in web scraping or browser automation.

#open the browser
driver_A=webdriver.Chrome()
#load the webpage
driver_A.get("https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile")
time.sleep(3)
4. driver_A.maximize_window()

Summary of Actions
Open the Browser: webdriver.Chrome() opens a new Chrome browser instance.
Load the Webpage: driver_A.get("https://www.redbus.in/...") loads the specified URL.
Wait for 3 Seconds: time.sleep(3) pauses the execution for 3 seconds to give the webpage time to load completely.
Maximize the Browser Window: driver_A.maximize_window() maximizes the browser window to ensure full-screen mode.
# Retrieve bus links and route

1. WebDriverWait Setup
wait = WebDriverWait(driver_A, 20)
2. Function Definition
3. Loop to Handle Pagination (5 Pages)
for i in range(1, 6):
    paths = driver_A.find_elements(By.XPATH, path)
4. Extracting Bus Route Links (URLs)
for links in paths:
    d = links.get_attribute("href")
    ANDHRA_LINKS.append(d)
5. Extracting Bus Route Names
for route in paths:
    ANDHRA_ROUTES.append(route.text)
6. Handling Pagination (Next Page)
try:
    pagination = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="DC_117_paginationTable"]')))
    next_button = pagination.find_element(By.XPATH, f'//div[@class="DC_117_pageTabs " and text()="{i + 1}"]')
    time.sleep(3)  
    next_button.click()
7. Handling the End of Pagination (Break Condition)
except NoSuchElementException:
    print(f"No more pages to paginate at step {i}")
    break
except NoSuchElementException:: If the pagination element is not found (i.e., there are no more pages), the NoSuchElementException is caught.
8. Returning the Data
return ANDHRA_LINKS, ANDHRA_ROUTES
10. Calling the Function
ANDHRA_LINKS, ANDHRA_ROUTES = Andhra_Route_Link("//a[@class='route']")

Summary of the Process
Setup WebDriverWait: Prepare to wait for elements to load with a timeout of 20 seconds.
Function Andhra_Route_Link(path):
Iterate through Pages: A loop handles pagination, scraping 5 pages of bus routes.
Extract Links and Route Names: For each page, the function extracts both the URLs (links) and the text (names) of the bus routes.
Navigate to the Next Page: The script clicks the "Next" button to go to the next page, waiting for the pagination elements to load.
Handle End of Pagination: The function gracefully handles when there are no more pages by catching the NoSuchElementException.
Return Data: After scraping all the pages, the function returns the list of bus route links and names.

#stores that datas in dataframe
df_A=pd.DataFrame({"Route_name":ANDHRA_ROUTES,"Route_link":ANDHRA_LINKS})
df_A

Summary
This lines creates a Pandas DataFrame where:
"Route_name" column contains the names of the bus routes.
"Route_link" column contains the links to those routes.
The resulting df_A is a tabular structure that you can work with, perform analysis on, or save/export in various formats (like CSV, Excel, etc.).

#change DataFrame to csv
path = r"C:/Users/sridh/OneDrive/Desktop/redbus/routes_link/df_A.csv"
df_A.to_csv(path,index=False)

Summary:
Path to save the CSV: The variable path holds the directory path where you want to save the CSV file. It uses the raw string format (r"...") to handle the backslashes in the file path properly.

Saving DataFrame:  saves the Pandas DataFrame  at the specified path without including the index.

#Like this one state bus routes and links we have to extract all the states buses routes and bus links details.

#concat all the bus link and route names in one dataframe
df=pd.concat([df_A,df_k,df_T,df_G,df_R,df_H,df_SB,df_AS,df_UP,df_WB],ignore_index=True)
df

Summary:
pd.concat() combines multiple DataFrames vertically (stacking them on top of each other).
ignore_index=True reindexes the resulting DataFrame to ensure that the index is continuous across all rows.
The result is a single DataFrame containing all the rows from the original DataFrames with a clean, sequential index.

also we have save this all buses routes and links data in one csv file for later use.
