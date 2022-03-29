from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os
import re
import pandas as pd
import csv
import numpy as np


pd.options.display.float_format = '{:.6f}'.format

# Instantiate options
opts = Options()
opts.add_argument('headless')
# opts.add_argument(" — headless") # Uncomment if the headless version needed
#opts.binary_location = "C:\Users\atrni\PycharmProjects\pythonProject\chromedriver"

# Set the location of the webdriver
#chrome_driver = os.getcwd() + "C:\Users\atrni\PycharmProjects\pythonProject\chromedriver"

# Instantiate a webdriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)


def everything():
    # ##############################################################
    # MIN
    # ##############################################################
    # SWAP
    # ##############################################################
    # SCRAPING
    # ##############################################################

    # Load the HTML page
    driver.get("https://app.minswap.org/")
    #wait for initial load
    time.sleep(5)
    #scroll to bottom to load all pairs
    driver.execute_script("window.scrollTo(0, 2080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 3080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 4080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 5080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 6080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 7080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 8080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 9080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 10080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 11080)")
    time.sleep(5)


    soup = BeautifulSoup(driver.page_source, 'html.parser')
    with open("minswap.txt", 'wt', encoding='utf-8') as html_file:
        for line in soup.prettify():
            html_file.write(line)

    min_df1 = []
    min_df2 = []
    min_df3 = []

    #this extracts price data
    with open("min_testing.txt", "w", encoding='utf-8') as f:
        #find the pair
        for line in soup.find_all('div', class_="text-left font-medium"):
            alex = str(line.get_text())
            if True:
                f.write(str(alex))
                min_df1.append(str(alex))
        #first part of price
        for line in soup.find_all('div', class_="flex items-center justify-end whitespace-nowrap text-gray-500 dark:text-dark-500"):
            alex = str(line.get_text())
            if True:
                f.write(str(alex))
                min_df2.append(str(alex))
        # #second part of price
        # for line in soup.find_all('div', class_="sc-gHjyzD JfMLN"):
        #     alex = str(line.get_text())
        #     if True:
        #         f.write(str(alex))
        #         min_df3.append(str(alex))

    #print(str(len(min_df1)) + ":" + str(min_df1))
    #print(str(len(min_df2)) + ":" + str(min_df2))


    min_price = min_df2[::5]
    #print(str(len(min_price)) + ":" + str(min_price))

    min_names = [e[6:] for e in min_df1]
    min_price = [e[:-2] for e in min_price]
    #print(min_names)

    df_min = pd.DataFrame(min_price, index =min_names,columns =['min_price'])

    #print(df_min)


    ##############################################################
    #SUNDAE
    ##############################################################
    #SWAP
    ##############################################################
    #SCRAPING
    ##############################################################
    driver.get("https://exchange.sundaeswap.finance/#/")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, 2080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 3080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 4080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 5080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 6080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 7080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 8080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 9080)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 10080)")
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')


    #this extracts price data
    with open("sspricedata.txt", "w", encoding='utf-8') as f:
        for line in soup.find_all('div', class_="sc-dkPtRN sc-cjrPHo bBDfiw eAWPvP"):
            alex = str(line)
            if 'Price' in alex:
                f.write(str(alex)+"\n")



    # ss_df1 = pd.DataFrame()
    # ss_df2 = pd.DataFrame()
    # ss_df3 = pd.DataFrame()

    ss_df1 = []
    ss_df2 = []
    ss_df3 = []

    #this extracts price data
    with open("ss_testing.txt", "w", encoding='utf-8') as f:
        #find the pair
        for line in soup.find_all('span', class_="sc-avest fdmmzY"):
            alex = str(line.get_text())
            if True:
                f.write(str(alex))
                ss_df1.append(str(alex))
        #first part of price
        for line in soup.find_all('div', class_="sc-gHjyzD JfMLN"):
            alex = str(line.get_text())
            if True:
                f.write(str(alex))
                ss_df2.append(str(alex))
        #second part of price
        for line in soup.find_all('div', class_="sc-gHjyzD JfMLN"):
            alex = str(line.get_text())
            if True:
                f.write(str(alex))
                ss_df3.append(str(alex))
    #
    # print(str(len(ss_df1)) + ":" + str(ss_df1))
    # print(str(len(ss_df2)) + ":" + str(ss_df2))
    #print(str(len(ss_df3)) + ":" + str(ss_df3))

    ss_price = ss_df2[::4]
    ss_TVL1 = ss_df2[1::4]
    ss_TVL2 = ss_df2[2::4]
    ss_volume = ss_df2[3::4]

    #print(str(len(ss_price)) + ":" + str(ss_price))

    ss_names = [e[:-4] for e in ss_df1]
    ss_price = [e[:-2] for e in ss_price]


    df_ss = pd.DataFrame(ss_price, index =ss_names,columns =['ss_price'])
    df_min['min_price'] = df_min['min_price'].astype('float')
    df_ss['ss_price'] = df_ss['ss_price'].astype('float')
    #df_ss['TVL1'] = ss_TVL1
    df_ss['ADA TVL'] = ss_TVL2
    df_ss['ADA TVL'] = df_ss['ADA TVL'].str.replace(',', '')
    df_ss['ADA TVL'] = df_ss['ADA TVL'].astype('float')


    df_master = pd.merge(df_ss, df_min, left_index=True, right_index=True)
    df_master['difference'] = df_master['ss_price']-df_master['min_price']
    df_master['difference'] = df_master['difference'].abs()
    df_master['minimum'] = df_master[['ss_price','min_price']].min(axis=1)
    df_master['arbitrage %'] = (df_master['difference']/df_master['minimum'])*100

    comparison_column = np.where(df_master["min_price"] > df_master["ss_price"], "SS", "MIN")
    df_master["Buy On"] = comparison_column
    df_master = df_master.sort_values(by=['arbitrage %'], ascending=False)


    #filtering out pools that are too small
    df_master= df_master[df_master['arbitrage %'] < 1000] #you wish
    df_master= df_master[df_master['arbitrage %'] > 5] #not worth it
    df_master = df_master[df_master['ADA TVL'] > 40000] #pool too small
    df_master = df_master[df_master.index != "CARDS"]  # remove CARDS for now, min pool is too small to be useful

    df_master.to_csv('Output.csv', index = True)


    if df_master.empty:
        print("No Matches")
    else:
        print(df_master)
    print("===================" + str(datetime.now()) + "===================")
    return


i=0
while i < 100000:
    everything()
    time.sleep(60)





#


# # with open("sample2.txt", "r", encoding='utf-8') as f:
# #     for line in f:
# #         print(line)
#
# #soup2 = BeautifulSoup(str(line), 'html.parser').find_all('small', class_="sc-ilfuhL sc-JEhMO eRzXzy tUXGU")
#
# with open("sundaeswap.html", "w", encoding='utf-8') as f:
#     for line in soup.prettify():
#         f.write(str(line))
# #
# # with open("sundaeswap.txt", "w", encoding='utf-8') as f:
# #     for line in soup.prettify():
# #         f.write(str(line))
#
#
#     #
#     # print(h1.find("a")['href'])
#
#
# # #This is where the pair names are stored
# # for h1 in soup.find_all('span', class_="sc-avest fdmmzY"):
# #     print(h1)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# with open('sundaeswap.txt', encoding="utf8") as f:
#     if 'WMT/ADA' in f.read():
#         print("true")
#
# with open('sundaeswap.html', encoding="utf8") as f:
#     if 'WMT/ADA' in f.read():
#         print("true")


