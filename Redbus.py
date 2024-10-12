#importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time

#Kerela Bus
Lists_k = []
df_k = pd.read_csv("df_k.csv")
for i,r in df_k.iterrows():
    Lists_k.append(r["Route_name"])

#Andhra Bus
Lists_A = []
df_A = pd.read_csv("df_A.csv")
for i,r in df_A.iterrows():
    Lists_A.append(r["Route_name"])

#Telungana Bus
Lists_T = []
df_T = pd.read_csv("df_T.csv")
for i,r in df_T.iterrows():
    Lists_T.append(r["Route_name"])

#Goa Bus
Lists_G = []
df_G = pd.read_csv("df_G.csv")
for i,r in df_G.iterrows():
    Lists_G.append(r["Route_name"])

#Rajasthan Bus
Lists_R = []
df_R = pd.read_csv("df_R.csv")
for i,r in df_R.iterrows():
    Lists_R.append(r["Route_name"])

#SouthBengal Bus
Lists_SB = []
df_SB = pd.read_csv("df_SB.csv")
for i,r in df_SB.iterrows():
    Lists_SB.append(r["Route_name"])

#Haryana Bus
Lists_H = []
df_H = pd.read_csv("df_H.csv")
for i,r in df_H.iterrows():
    Lists_H.append(r["Route_name"])

#Assam Bus
Lists_AS = []
df_AS = pd.read_csv("df_AS.csv")
for i,r in df_AS.iterrows():
    Lists_AS.append(r["Route_name"])

#UttarPradesh Bus
Lists_UP = []
df_UP = pd.read_csv("df_UP.csv")
for i,r in df_UP.iterrows():
    Lists_UP.append(r["Route_name"])

#WestBengal Bus
Lists_WB = []
df_WB = pd.read_csv("df_WB.csv")
for i,r in df_WB.iterrows():
    Lists_WB.append(r["Route_name"])

#Setting up streamlit page
slt.set_page_config(layout="wide")

web = option_menu(menu_title="🚌OnlineBus",
                  options=["Home","📍States and Routes"],
                  icons=["house","info-circle"],
                  orientation="horizontal")
#Home page setting
if web == "Home":
    slt.image("C:/Users/sridh/Downloads/redbus1-768x509 (1).jpg",width=200)
    slt.title("RedBus Data Scraping With Selenium & Dynamic Filtering Using Streamlit")
    slt.subheader(":blue[Domain:] Transportation")
    slt.subheader(":blue[Objective:] ")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
    slt.markdown("Selenium: Selenium WebDriver is a powerful Automation tool widely used for web application testing. Selenium allows you to simulate human interactions with a web page,such as clicking buttons,filling out forms and navigating through pages,to collect the desired data... ")
    slt.markdown('''Pandas: Pandas library to transform the dataset from CSV format into a structured DataFrame.
                  Pandas helps data manipulation,cleaning,and preprocessing,ensuring that data was ready for analysis.''')
    slt.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamlessbintegration of the transformed dataset 
                 and the data was efficiently inserted into relevant tables for storage and retrieval.''')
    slt.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    slt.subheader(":blue[Skill-take:]")
    slt.markdown("Selenium , Python, Pandas, MySQL, mysql-connector-python, Streamlit.")
    
#Staes and Routes page setting
if web =="📍States and Routes":
    S = slt.selectbox("Lists of States", ["Kerela","Andhra","Telungana","Goa",
                                            "Rajasthan","SouthBengal","Haryana","Assam","UttarPradesh","WestBengal"])
    
    select_fare = slt.radio("Choose bus fare range", ("50-1000","1000-2500","2500 and above"))

    #Kerela bus fare filtering
    if S =="Kerela":
        K = slt.selectbox("List of routes",Lists_k)

        if select_fare == "50-1000":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 50 and 1000 and Route_name = "{K}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "1000-2500":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 1000 and 2500 and Route_name = "{K}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "2500 and above":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price > 2500 and Route_name = "{K}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

     #Andhra bus fare filtering
    if S =="Andhra":
        A = slt.selectbox("List of routes",Lists_A)

        if select_fare == "50-1000":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 50 and 1000 and Route_name = "{A}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "1000-2500":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 1000 and 2500 and Route_name = "{A}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "2500 and above":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price > 2500 and Route_name = "{A}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

    #Telungana bus fare filtering
    if S =="Telungana":
        T = slt.selectbox("List of routes",Lists_T)

        if select_fare == "50-1000":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 50 and 1000 and Route_name = "{T}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "1000-2500":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 1000 and 2500 and Route_name = "{T}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "2500 and above":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price > 2500 and Route_name = "{T}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

    #Goa bus fare filtering
    if S =="Goa":
        G = slt.selectbox("List of routes",Lists_G)

        if select_fare == "50-1000":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 50 and 1000 and Route_name = "{G}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "1000-2500":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 1000 and 2500 and Route_name = "{G}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "2500 and above":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price > 2500 and Route_name = "{G}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
            
    #Rajasthan bus fare filtering
    if S =="Rajasthan":
        R = slt.selectbox("List of routes",Lists_R)

        if select_fare == "50-1000":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 50 and 1000 and Route_name = "{R}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "1000-2500":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 1000 and 2500 and Route_name = "{R}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "2500 and above":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price > 2500 and Route_name = "{R}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
    
    #SouthBengal bus fare filtering
    if S =="SouthBengal":
        SB = slt.selectbox("List of routes",Lists_SB)

        if select_fare == "50-1000":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 50 and 1000 and Route_name = "{SB}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "1000-2500":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 1000 and 2500 and Route_name = "{SB}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "2500 and above":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price > 2500 and Route_name = "{SB}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

    #Haryana bus fare filtering
    if S =="Haryana":
        H = slt.selectbox("List of routes",Lists_H)

        if select_fare == "50-1000":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 50 and 1000 and Route_name = "{H}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "1000-2500":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 1000 and 2500 and Route_name = "{H}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "2500 and above":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price > 2500 and Route_name = "{H}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

    #Assam bus fare filtering
    if S =="Assam":
        AS = slt.selectbox("List of routes",Lists_AS)

        if select_fare == "50-1000":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 50 and 1000 and Route_name = "{AS}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "1000-2500":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 1000 and 2500 and Route_name = "{AS}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "2500 and above":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price > 2500 and Route_name = "{AS}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)   

    #UttarPradesh bus fare filtering
    if S =="UttarPradesh":
        UP = slt.selectbox("List of routes",Lists_UP)

        if select_fare == "50-1000":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 50 and 1000 and Route_name = "{UP}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "1000-2500":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 1000 and 2500 and Route_name = "{UP}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "2500 and above":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price > 2500 and Route_name = "{UP}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)        

    #WestBengal bus fare filtering
    if S =="WestBengal":
        WB = slt.selectbox("List of routes",Lists_WB)

        if select_fare == "50-1000":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 50 and 1000 and Route_name = "{WB}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "1000-2500":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price Between 1000 and 2500 and Route_name = "{WB}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

        if select_fare == "2500 and above":
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query = f'''select * from bus_details
                    where Price > 2500 and Route_name = "{WB}"
                    order by Price desc'''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Starting_Time","Ending_Time","Total_Duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)    

