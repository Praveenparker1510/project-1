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

Also we have save this all buses routes and links data in one csv file for later use.

2)EXTRACTING BUS DETAILS

#read the csv file
df = pd.read_csv("df_k.csv")
df

Summary:
pd.read_csv: Reads the CSV file df_k.csv into a Pandas DataFrame (df).
DataFrame : A table-like structure in Pandas that stores the contents of the CSV file with columns and rows.
You can use various optional parameters in read_csv() to customize how the CSV file is read.
Once the data is in a DataFrame, you can perform operations like inspection, cleaning, analysis, and manipulation on the data.

1.Initialize the WebDriver
driver_k = webdriver.Chrome()
2. Create Lists to Store Bus Details
Bus_names_k = []
Bus_types_k = []
Starting_Time_k = []
Ending_Time_k = []
Ratings_k = []
Total_Duration_k = []
Prices_k = []
Seats_Available_k = []
Route_names = []
Route_links = []
These are empty lists that will hold the extracted data from the bus website for later use (e.g., storing the names of buses, timings, prices, etc.).
Purpose of each list:
Bus_names_k: Stores the names of the buses.
Bus_types_k: Stores the types of buses (e.g., sleeper, semi-sleeper, etc.).
Starting_Time_k: Stores the starting times of the buses.
Ending_Time_k: Stores the ending times of the buses.
Ratings_k: Stores the ratings of the buses (if available).
Total_Duration_k: Stores the total travel duration of the buses.
Prices_k: Stores the fare prices of the buses.
Seats_Available_k: Stores the number of available seats.
Route_names: Stores the route names (e.g., "Hyderabad to Bangalore").
Route_links: Stores the links to the respective route pages.
3. Loop Through Each Route in the DataFrame
for i, r in df.iterrows():
    link = r["Route_link"]
    routes = r["Route_name"]
4. Navigate to the Route Link
driver_k.get(link)
time.sleep(2)
5. Click on Elements to Reveal Bus Details
elements = driver_k.find_elements(By.XPATH, "//a[contains(@href,'/bus/')]")
for element in elements:
    try:
        WebDriverWait(driver_k, 10).until(EC.element_to_be_clickable((By.XPATH, element.get_attribute('xpath'))))
        element.click()
        time.sleep(2)
    except Exception as e:
        print(f"Error clicking on element: {e}")
        continue
6. Click to View Bus Details
try:
    clicks = driver_k.find_element(By.XPATH, "//div[@class='button']")
    WebDriverWait(driver_k, 10).until(EC.element_to_be_clickable(clicks))
    clicks.click()
except Exception as e:
    print(f"Error clicking on the button: {e}")
    continue
7. Scroll and Load All Bus Details
def scroll():
    last_height = driver_k.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver_k.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(0.5)
        new_height = driver_k.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

scroll()
8. Extract Bus Details
bus_name = driver_k.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
bus_type = driver_k.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
start_time = driver_k.find_elements(By.XPATH, "//div[@class='dp-time f-19 d-color f-bold']")
end_time = driver_k.find_elements(By.XPATH, "//div[@class='bp-time f-19 d-color disp-Inline']")
total_duration = driver_k.find_elements(By.XPATH, "//div[@class= 'dur l-color lh-24']")

try:
    rating = driver_k.find_elements(By.XPATH, "//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
except Exception as e:
    print(f"Error retrieving ratings: {e}")
    rating = []
9. Extract Price and Available Seats
price = driver_k.find_elements(By.XPATH, "//div[@class='fare d-block']")
seats = driver_k.find_elements(By.XPATH, "//div[contains(@class, 'seat-left ')]")
10. Append Data to Lists
for bus in bus_name:
    Bus_names_k.append(bus.text)
    Route_links.append(link)
    Route_names.append(routes)
    
for bus_type_elements in bus_type:
    Bus_types_k.append(bus_type_elements.text)
for start_time_elements in start_time:
    Starting_Time_k.append(start_time_elements.text)
for end_time_elements in end_time:
    Ending_Time_k.append(end_time_elements.text)
for total_duration_elements in total_duration:
    Total_Duration_k.append(total_duration_elements.text)
for ratings in rating:
    Ratings_k.append(ratings.text)
for price_elements in price:
    Prices_k.append(price_elements.text)
for seats_elements in seats:
    Seats_Available_k.append(seats_elements.text)
11. Completion Message
print("SUCCESSFULLY COMPLETED")
12. Quit the WebDriver
driver_k.quit()

Summary:
This Python script uses Selenium to scrape bus details from a website, given a list of route links and names stored in a DataFrame (df). Here's an overview of its steps:
Initialize WebDriver: Opens a Chrome browser using the webdriver.Chrome() to control the browser programmatically.
Create Empty Lists: Sets up empty lists to store bus details, such as bus names, types, start and end times, ratings, prices, seat availability, and route details.
Iterate Over Routes: Loops through each row in the DataFrame (df), which contains route links and route names.
Navigate to Each Route Link: Opens the route link in the browser and waits for 2 seconds for the page to load.
Click Bus Links: Finds and clicks on bus links to open the details of each bus. If the element is not clickable, it handles the exception and moves to the next.
View Bus Details: Clicks a button to reveal bus details (if present), using WebDriverWait to ensure the button is clickable.
Scroll to Load All Data: Scrolls the page to load all available bus details, ensuring all content is visible.
Extract Bus Details: Extracts various bus details (bus names, types, timings, ratings, prices, and seat availability) from the webpage using find_elements and stores them in the respective lists.
Append Data to Lists: Appends the extracted data (like bus names, start and end times, ratings, etc.) to the previously created lists.
Print Success Message: After scraping all data, prints "SUCCESSFULLY COMPLETED".
Quit WebDriver: Closes the browser and ends the WebDriver session.

#Data Preparation (Creating a Dictionary):

A Python dictionary called data is created where:
Keys: Represent the column names in the resulting DataFrame (e.g., 'Bus_Name', 'Bus_Type', 'Starting_Time', etc.).
Values: Correspond to lists that contain the data for each column. For example:
Each key-value pair in the dictionary represents a column in the DataFrame, with the values being the data for that column.
data = {
    'Bus_Name': Bus_names_k,
    'Bus_Type': Bus_types_k,
    'Starting_Time': Starting_Time_k,
    'Ending_Time': Ending_Time_k,
    'Total_Duration': Total_Duration_k,
    'Price': Prices_k,
    'Seats_Available': Seats_Available_k,
    'Ratings': Ratings_k,
    'Route_Link': Route_links,
    'Route_Name': Route_names
}

Convert the Dictionary to a Pandas DataFrame:

The pd.DataFrame(data) function from the Pandas library is used to convert the dictionary into a DataFrame. A DataFrame is a 2D labeled structure, similar to a table, where each key in the dictionary becomes a column and each list in the dictionary becomes the data within that column.

df_Kerela_Busdetails = pd.DataFrame(data)
Result: This creates a DataFrame with the following columns:

'Bus_Name'
'Bus_Type'
'Starting_Time'
'Ending_Time'
'Total_Duration'
'Price'
'Seats_Available'
'Ratings'
'Route_Link'
'Route_Name'
The DataFrame is structured like this:

Bus_Name	Bus_Type	Starting_Time	Ending_Time	Total_Duration	Price	Seats_Available	Ratings	Route_Link	Route_Name
Bus1	Sleeper	10:00 AM	05:00 PM	7h	₹1000	20	4.5	link1	Hyderabad to Bangalore
Bus2	Semi-Sleeper	12:30 PM	06:45 PM	6h 15m	₹1200	15	4.0	link2	Bangalore to Chennai
Bus3	Sleeper	03:15 PM	09:30 PM	6h 15m	₹1100	25	4.2	link3	Mumbai to Pune
Purpose:

The DataFrame now holds all the bus-related details in a structured, tabular format. This DataFrame can easily be analyzed, manipulated, or exported to other formats like CSV, Excel, or database tables for further use.
Key Benefits of Using a DataFrame:
Structured Data: The data is now in a format that is easy to manipulate, filter, or analyze using Pandas' powerful functions.
Tabular Representation: Each list (e.g., Bus_names_k, Bus_types_k) becomes a column in the DataFrame, making it easier to visualize and process.
Further Processing: You can easily apply operations like sorting, filtering, or aggregations on this DataFrame, or you can save it to a CSV file for later use.

SAVE THIS DATAFRAME INTO CSV FILE

AND ALSO WE WANT TO EXTRACT ALL STATES BUSES DETAILS LIKE THIS AND SAVE INTO CSV FILES

3)SQL CONNECTION

#IMPORTING WANTED PACKAGES
pandas is for data manipulation and analysis.
mysql.connector is for connecting and working with MySQL databases.
numpy is used for numerical operations, especially with arrays and matrices.

Reading CSV Files into DataFrames:

pd.read_csv() is used to load data from each CSV file into a Pandas DataFrame. Each DataFrame corresponds to bus details from a specific region.
df_Buses_Kerela = pd.read_csv("df_Kerela_Busdetails.csv")
df_Buses_Andhra = pd.read_csv("df_Andhra_Busdetails.csv")
df_Buses_Telungana = pd.read_csv("df_Telungana_Busdetails.csv")
df_Buses_Goa = pd.read_csv("df_Goa_Busdetails.csv")
df_Buses_Rajasthan = pd.read_csv("df_Rajasthan_Busdetails.csv")
df_Buses_SouthBengal = pd.read_csv("df_SouthBengal_Busdetails.csv")
df_Buses_Haryana = pd.read_csv("df_Haryana_Busdetails.csv")
df_Buses_Assam = pd.read_csv("df_Assam_Busdetails.csv")
df_Buses_UttarPradesh = pd.read_csv("df_UttarPradesh_Busdetails.csv")
df_Buses_WestBengal = pd.read_csv("df_WestBengal_Busdetails.csv")
Each CSV file is expected to contain bus-related data like bus names, types, timings, ratings, prices, etc., in tabular format.
The CSV files are named according to the respective regions (Kerela, Andhra, Telangana, Goa, Rajasthan, etc.).
Concatenating the DataFrames:

pd.concat() is used to concatenate all the individual DataFrames into one Final DataFrame (Final_df).
The ignore_index=True parameter is used to reindex the resulting DataFrame, ensuring that the index is continuous across all rows (rather than preserving the original indices from the individual DataFrames).

Final_df = pd.concat([df_Buses_Kerela, df_Buses_Andhra, df_Buses_Telungana, df_Buses_Goa, 
                      df_Buses_Rajasthan, df_Buses_Haryana, df_Buses_Assam, 
                      df_Buses_SouthBengal, df_Buses_WestBengal, df_Buses_UttarPradesh], ignore_index=True)
This concatenation combines all the bus details into one large table (DataFrame) that now includes data from all the regions.
Viewing the Final DataFrame:

After concatenation, the DataFrame Final_df will contain all the rows and columns from the individual region-specific DataFrames. Each row will represent a bus, and the columns will include details such as bus names, types, starting/ending times, prices, ratings, and more.
Final_df
Key Points:
pd.read_csv(): Reads CSV files into a Pandas DataFrame.
pd.concat(): Concatenates multiple DataFrames into one.
ignore_index=True: Resets the index in the final concatenated DataFrame to ensure a continuous index across all data.
Outcome:
The code merges data from multiple CSV files containing bus details from different regions into a single DataFrame (Final_df). This consolidated DataFrame can then be used for further analysis, reporting, or processing.

#DATA CLEANING
WE HAVE SEE THE DATAS FOR DATA CLEANING THIS CODE GIVES MORE DETAILS FOR FURTHER PROCESSING 
Final_df.info()
is used to display summary information about the DataFrame Final_df. Specifically, it provides a concise overview of the DataFrame's structure and contents, which is useful for understanding the data and performing initial exploratory data analysis (EDA).

What to Look for in info() Output:
Missing Data: Check for columns with non-null counts less than the total number of rows. This indicates missing or incomplete data.
Data Types: Ensure that the columns have appropriate data types. For example, Price might be stored as object (string) but should ideally be a numerical type (e.g., float64).
Memory Usage: For large datasets, this helps understand how much memory the DataFrame is consuming. This might prompt you to optimize the DataFrame by reducing its size or changing data types (e.g., using category instead of object for string columns with repetitive values).
Purpose:
Final_df.info() is used as an initial inspection of the data to:

Ensure all columns contain the expected types of data.
Identify if there is missing data in any column.
Get an overview of the structure and size of the DataFrame.

#CONVET PRICES INTO NUMERIC

1. Remove "INR" from the Price Column:
Final_df["Price"] = Final_df["Price"].str.replace("INR", "")
2. Convert the Price Column to a Numeric (Float) Type:
Copy code
Final_df["Price"] = Final_df["Price"].astype(float)
3. Fill Missing Values in the Price Column:
Final_df["Price"].fillna(0)
4.Improvement: Reassign fillna():
Final_df["Price"] = Final_df["Price"].fillna(0)

Summary:
Remove Currency: First, the "INR" string is removed from the Price column.
Convert to Numeric: Then, the Price column is converted to a numeric data type (float) for further analysis.
Handle Missing Values: Finally, any missing or NaN values in the Price column are replaced with 0.
This process ensures that the Price column is now ready for mathematical operations and analysis, with all values properly formatted as numbers and missing data handled.

#CONVERT RATINGS IN NUMERIC

1. Remove the "New" Text from the Ratings Column:
Final_df["Ratings"] = Final_df["Ratings"].str.replace("New", "")
2. Remove Leading and Trailing Spaces:
Final_df["Ratings"] = Final_df["Ratings"].str.strip()
3. Extract the First Value in the Rating (if it Contains Multiple Values):
Final_df["Ratings"] = Final_df["Ratings"].str.split().str[0]
4. Convert the Ratings to Numeric:
Final_df["Ratings"] = pd.to_numeric(Final_df["Ratings"], errors="coerce")
5. Fill Missing or NaN Values with 0:
Final_df["Ratings"].fillna(0, inplace=True)

Summary:
Remove "New" Text: The "New" string is removed from the Ratings column.
Strip Whitespaces: Any leading or trailing spaces are removed from the ratings.
Extract First Rating Value: If the rating contains multiple values (like "4.5/5"), only the first part is retained.
Convert to Numeric: The ratings are converted to numeric (float) data types.
Handle Missing Data: Any missing (NaN) values in the Ratings column are filled with 0.
Purpose:
The goal of this code is to clean and standardize the Ratings column, converting it into a numeric format (float) and handling any missing or invalid values. This is essential for performing numerical operations (such as finding averages or sorting by ratings) in subsequent analysis.

#REPLACING THE NAN INTO NULL VALUES
Final_df = Final_df.replace({np.nan: None})

Summary:
Purpose: The line Final_df.replace({np.nan: None}) is used to replace all NaN values in the DataFrame with None, making missing values more general and compatible with Python's handling of null values.
When to Use: This is useful when you want to ensure that all missing values are represented by None, particularly if you plan to work with databases or if you need a more general representation of missing data beyond just numeric types (i.e., for all types of data: numeric, strings, etc.).
Outcome: The DataFrame Final_df will no longer contain any NaN values but will have None in their place, which is sometimes preferred for consistency or compatibility with other systems.

WE HAVE STORE THE CLEANED DATA INTO NEW CSV FILE FOR LATER USAGE.

#CREATE A MYSQL DATABASE FOR SQL CONNECTION

1. Connecting to MySQL Database (mysql.connector.connect):
conn = mysql.connector.connect(host="localhost", user="root", password="", database="RED_BUS_DETAILS")
2. Creating a Cursor Object (conn.cursor):
my_cursor = conn.cursor(buffered=True)
3. Creating a Database (my_cursor.execute):
my_cursor.execute("CREATE DATABASE IF NOT EXISTS RED_BUS_DETAILS")

Summary:
The code starts by connecting to the MySQL server (localhost) using the root user credentials with no password.
A cursor object is created from the connection, allowing interaction with the MySQL server.
The script then attempts to create a new database named RED_BUS_DETAILS. If this database already exists, the IF NOT EXISTS clause ensures no error occurs.
Important Considerations:
Security: In real-world scenarios, it's essential to avoid using the root user without a password for security reasons. You should use a user with the appropriate permissions for the task at hand.
Error Handling: While this code does not include error handling, it is generally a good practice to wrap database operations in a try-except block to handle potential issues (e.g., connection errors, SQL errors, etc.).
Database Creation: Creating a database should only be done once. After the database is created, you can then start creating tables, inserting records, and performing queries within it.
This code is a simple setup to establish a connection, ensure a database exists, and create it if it doesn't, making it a common starting point for working with databases in python using sql

#TABLE CREATION

1. SQL Query: CREATE TABLE IF NOT EXISTS
CREATE TABLE IF NOT EXISTS bus_details(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Bus_Name VARCHAR(255) NOT NULL,
    Bus_Type VARCHAR(255) NOT NULL,
    Starting_Time VARCHAR(255) NOT NULL,
    Ending_Time VARCHAR(255) NOT NULL,
    Total_Duration VARCHAR(255) NOT NULL,
    Price FLOAT NULL,
    Seats_Available VARCHAR(255) NOT NULL,
    Ratings FLOAT NULL,
    Route_Link VARCHAR(255) NULL,
    Route_Name VARCHAR(255) NULL
)

Summary :
Table Creation: The table bus_details is created to store information about buses, including their name, type, timings, price, seats, ratings, and route details.
Handling Existing Tables: If the table already exists in the database, it will not be created again due to the IF NOT EXISTS clause.
Column Specifications: The table has various columns with different data types and constraints (NOT NULL, NULL, AUTO_INCREMENT), ensuring that the data stored in the table is consistent and properly structured.
Primary Key: The ID column serves as the unique identifier for each bus, ensuring that each row can be uniquely referenced.
Outcome:
After running this SQL query, the bus_details table is created in the connected MySQL database.
The script prints "TABLE CREATED SUCCESSFULLY" to confirm the creation of the table.
Note:
Data Integrity: The use of NOT NULL ensures that essential information (like bus name, type, timings, and seats) is always provided when inserting new bus records.
Future Inserts: After the table is created, you can insert records into this table with details about each bus, and the data will be structured according to these columns.

#INSERT THE DATA TO SQL DATABASE TABLE

1. SQL Query to Insert Data:
insert_query = """INSERT INTO bus_details(
                    Bus_Name,
                    Bus_Type,
                    Starting_Time,
                    Ending_Time,
                    Total_Duration,
                    Price,
                    Seats_Available,
                    Ratings,
                    Route_Link,
                    Route_Name)
                  VALUES(%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s )"""


2. Inserting Data Row by Row:
try:
    for index, row in Final_df.iterrows():
        my_cursor.execute(insert_query, (
            row["Bus_Name"],
            row["Bus_Type"],
            row["Starting_Time"],
            row["Ending_Time"],
            row["Total_Duration"],
            row["Price"],
            row["Seats_Available"],
            row["Ratings"],
            row["Route_Link"],
            row["Route_Name"]
        ))
3. Committing the Transaction:
conn.commit()
4. Error Handling:
except mysql.connector.Error as e:
    # If there's an error, print it and roll back the transaction
    print(f"Error: {e}")
    conn.rollback()
5. Closing the Connection and Cursor:
finally:
    # Close the cursor and connection
    my_cursor.close()
    conn.close()
Summary:
SQL Insert Query: The SQL query is prepared with placeholders to insert a row into the bus_details table.
Data Insertion Loop: The script iterates through each row of the Final_df DataFrame and inserts the data into the bus_details table using the my_cursor.execute() method.
Commit Changes: After all the rows are inserted, the conn.commit() command is issued to save the changes.
Error Handling: If an error occurs during the insertion, the transaction is rolled back to avoid partial inserts.
Closing Connections: Finally, the database cursor and connection are closed to ensure no resources are left open.
Important Considerations:
Batch Insertions: This script inserts data row by row. For very large datasets, batch insertion (using executemany) can be more efficient, as it reduces the number of round trips to the database.
Error Handling: It's crucial to handle database errors properly to avoid data corruption or incomplete inserts.

4)STREAMLIT PROJECTION FOR RED BUS

1. Importing Libraries:
import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time
2. Reading the CSV File (df_k.csv):
df_k = pd.read_csv("df_k.csv")
3. Extracting Route Names into a List:
Lists_k = []
for i, r in df_k.iterrows():
    Lists_k.append(r["Route_name"])

Summary:
Libraries: Various libraries are imported for data processing (pandas), database interaction (mysql.connector), creating web apps (streamlit), and data visualization (plotly.express).
Data Reading: The csv file is read into a pandas DataFrame 
Extract Route Names: A loop iterates through each row of the csv file, extracting the bus route names from the Route_name column and appending them to the list.

WE WANT TO READ AND EXTRACT ALL CSV FILE AND SAVE IT TO LISTS

#SETTING UP STREAMLIT PAGE:

1. Streamlit Page Configuration
slt.set_page_config(layout="wide")
2. Navigation Menu
web = option_menu(menu_title="🚌OnlineBus",
                  options=["Home", "📍States and Routes"],
                  icons=["house", "info-circle"],
                  orientation="horizontal")
3. Home Page Setup
if web == "Home":
    slt.image("C:/Users/sridh/Downloads/redbus1-768x509 (1).jpg", width=200)
    slt.title("RedBus Data Scraping With Selenium & Dynamic Filtering Using Streamlit")
    slt.subheader(":blue[Domain:] Transportation")
    slt.subheader(":blue[Objective:] ")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data...")
    slt.markdown("Selenium: Selenium WebDriver is a powerful Automation tool widely used for web application testing...")
    slt.markdown('''Pandas: Pandas library to transform the dataset from CSV format into a structured DataFrame...''')
    slt.markdown('''MySQL: With help of SQL to establish a connection to a SQL database...''')
    slt.markdown("Streamlit: Developed an interactive web application using Streamlit...")
    slt.subheader(":blue[Skill-take:]")
    slt.markdown("Selenium, Python, Pandas, MySQL, mysql-connector-python, Streamlit.")
4. States and Routes Page Setup
if web == "📍States and Routes":
    S = slt.selectbox("Lists of States", ["Kerela", "Andhra", "Telungana", "Goa", "Rajasthan", "SouthBengal", "Haryana", "Assam", "UttarPradesh", "WestBengal"])
    
    select_fare = slt.radio("Choose bus fare range", ("50-1000", "1000-2500", "2500 and above"))
5. Bus Fare Filtering

if S == "Kerela":
    K = slt.selectbox("List of routes", Lists_k)

    if select_fare == "50-1000":
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        query = f'''select * from bus_details
                    where Price Between 50 and 1000 and Route_name = "{K}"
                    order by Price desc'''
        my_cursor.execute(query)
        out = my_cursor.fetchall()
        df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Starting_Time", "Ending_Time", "Total_Duration",
                                        "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
        slt.write(df)
6. Additional Fare Filters
if select_fare == "1000-2500":
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="RED_BUS_DETAILS")
    my_cursor = conn.cursor()
    query = f'''select * from bus_details
                where Price Between 1000 and 2500 and Route_name = "{K}"
                order by Price desc'''
    my_cursor.execute(query)
    out = my_cursor.fetchall()
    df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Starting_Time", "Ending_Time", "Total_Duration",
                                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
    slt.write(df)
7. Fare Range Above 2500
if select_fare == "2500 and above":
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="RED_BUS_DETAILS")
    my_cursor = conn.cursor()
    query = f'''select * from bus_details
                where Price > 2500 and Route_name = "{K}"
                order by Price desc'''
    my_cursor.execute(query)
    out = my_cursor.fetchall()
    df = pd.DataFrame(out, columns=["ID", "Bus_name", "Bus_type", "Starting_Time", "Ending_Time", "Total_Duration",
                                    "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"])
    slt.write(df)

Summary:
Streamlit Layout: The app has two pages: "Home" for project details and "📍States and Routes" for interactive bus route filtering based on fare range.
Dynamic Filtering: On the "States and Routes" page, users can:
Select a state (e.g., Kerala).
Choose a fare range (e.g., "50-1000").
View the filtered results of bus routes based on the selected criteria.
SQL Queries: The app queries the MySQL database to fetch and display the relevant bus details based on the user’s choices (state, route, fare range).
Interaction: The user interface is interactive, providing dropdowns for states and routes and radio buttons for fare ranges, allowing dynamic data filtering.

WE WANT TO DO ALL STATES BUSES DETAILS FOR STREAMLIT PAGE CONNECTION SAME LIKE THE PREVIOUS ONE.

BY ALL COMPLETING THIS, WE HAVE CREATE NEW TERMINAL AND TYPE STREAMLIT RUN REDBUS.PY IN THE COMMAND PROMPT

THE CODE EXECUTES SUCCESSFULLY











