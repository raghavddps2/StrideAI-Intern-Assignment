
  <h3 align="center">Task 1 - NYSE Scraper to collect data points</h3>

  <p align="center">
    This is the 1st Task as a part of Stride.AI Internship
    <br />
  </p>
</p>


### Installation


1. Clone the repository
```sh
git clone https://github.com/raghavddps2/Assignment.git
```
2. Navigate to the projects folder
```sh
cd Assignment/Task1
```
3. Install Python packages
```sh
pip3 install requirements.txt
```
4. For the line below to work, please set the drivers for either chrome/firefox on the path.
```sh
driver = webdriver.Firefox(options=options)
```

5. Run the python file
```sh
python3 findStockDetails.py
```

### How to test for any new stock.

1. Simply pass the new stock name to the function findStockDetails and it will give the name,last_traded_time and the price in the response.

2. Example
```
print(findStockDetails("Wells Fargo & Company"))

Result:
    {'actual_name': 'WELLS FARGO & COMPANY (WFC)', 'last_trade_time': 'Last Trade Time: 09/16/2020 17:47:52', 'price_value': '25.71'}
```

Example screenshot - With the Results Scraped.


<a href="https://ibb.co/7GGsCPx"><img src="https://i.ibb.co/fCCjFfV/Screenshot-from-2020-09-17-03-34-39.png" alt="Screenshot-from-2020-09-17-03-34-39" border="0"></a>



