from bs4 import BeautifulSoup
import urllib3
import datetime

companyTicker = 'Yes'
print("Instructions:\n")
print("TURN CAPS LOCK ON \n", "Enter NO to quit\n", "Enter company ticker (TSLA) to view the stock information \n")

while(companyTicker != 'NO'):

    date = (datetime.datetime.now())
    companyTicker = input("Enter the company you would like to search: \n")

    http = urllib3.PoolManager()
    bloom_SandP = "https://www.cnbc.com/quotes/?symbol="+companyTicker+"&qsearchterm="+companyTicker


    response = http.request('GET', bloom_SandP)

    soup = BeautifulSoup(response.data, 'html.parser')

    # Take out the <span or whatever html tag> of name and get its value
    name_box = soup.find('span', attrs={'class': 'name'})
    if (name_box == None):
        print("Error")
        continue
    name = name_box.text.strip()



    price_box = soup.find('span', attrs={'class': 'last'})
    price = price_box.text.strip()

    pChange_box = soup.find('div', attrs={'class': 'change'})
    pChange = pChange_box.text.strip()


    print(name)
    print(price)

    #The output was a bit clustered even with .strip() thus I sliced the string to get an ideal result.
    print(pChange[-7:])
    print(date.year, ",", date.month, ",", date.day)

