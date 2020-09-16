'''
    @Author: Raghav Maheshwari
    @Tools used - Selenium

    Details:

        1. This is a simple scraper that is used to scrap the actual name in the listing and the last traded
           time from the New York Stock Exchange website
        2. Selenium is used to automate the process.  
        3. I have used the firefox web driver, please uncomment line 26 and line 19 if you are using chrome.
            and comment line 19 and line 28
        4. The remaining flow
            1. Seaches for the stock on the url: https://www.nyse.com/listings_directory/stock
            2. Extracts the specific url for the stock and scrapes the actual_name and the last_traded_time.

'''
#Importing selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
import time

#Specyfing these options so that the browser doesn't open.
options = Options()
options.add_argument('--headless')

#For firefox
driver = webdriver.Firefox(options=options)
#For chrome
# driver = webdriver.Chrome(options=options)


def findStockDetails(name):
    #This is the url, where we will search the stock sent in the parameters
    url = 'https://www.nyse.com/listings_directory/stock'
    
    driver.get(url)

    #This finds the search box
    search_box = driver.find_element_by_xpath('//*[@id="instrumentFilter"]')
    #Sleep for 1 second for it to load
    time.sleep(1)
    #Type the name into the search bar
    search_box.send_keys(name)
    #Again sleep for around 2 seconds for the results to refresh
    time.sleep(3)
    #look at the first row of table
    firstResult = driver.find_elements_by_xpath("//table/tbody/tr/td")

    #If the number of elements in the list is 1,simply stock was not found
    if(len(firstResult) == 1):
        no_result_message = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[1]/table/tbody/tr/td[1]')
        return {"error":no_result_message.text}

    #Extracting the link for the stock.
    stock_link_element = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[1]/table/tbody/tr/td[1]/a')
    
    #Extracting the href attribute and this is the url, we should hit next.
    urlStock = stock_link_element.get_attribute('href')
    driver.get(urlStock)
    while(True):
        try:
            # If no error, this implies that the page has loaded.
            driver.find_element_by_class_name('d-dquote-time')
            break
        except:
            # This implies that the data is not loaded yet, as the webiste has dynamic components (Dynamic Rendering)
            # To prove it, we can see the Network Tab in the Inspect Element.
            pass
    try:
        #Extracting the actual name and the last_traded_time in the Quotes Section
        actual_name = driver.find_element_by_class_name('d-dquote-symbol').text
        last_trade_time = driver.find_element_by_class_name('d-dquote-time').text
        price_value = driver.find_element_by_class_name('d-dquote-x3').text
        return {"actual_name": actual_name, "last_trade_time":last_trade_time, "price_value": price_value}
    except:
        return {"error":"Some error occured/Data Not Available"}

#Example - 1: 'Wells Fargo & Company'
print(findStockDetails("Wells Fargo & Company"))

#Example - 2: 'Citigroup INC'
print(findStockDetails("Citigroup INC"))

#Example - 3: 'Unknown Stock' - Edge case (It will give appropriate message)
print(findStockDetails("Unknown Stock"))




