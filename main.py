import os
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime

# ----------- GET DATA ------------

def scrape_percentage():
    data = requests.get('') # Put the link to the website here
    html_content = data.text
    soup = BeautifulSoup(html_content, 'lxml')

# 1 - Placeholder for the HTML tag you want to search
# 2 - Placeholder for the class name, can be swaped with id
    percentage_span = soup.find('1', class_='2')

    if percentage_span:
        return percentage_span.text
    else:
        return "Percentage information not found."
    
# --------- SAVE TO CSV ---------

def save_to_csv(data, filename):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
    df = pd.DataFrame({'Time': [current_time], 'Percentage': data})

    if not os.path.exists(filename):
        df.to_csv(filename, index=False)
    else:
        if os.path.getsize(filename) == 0:
            df.to_csv(filename, index=False)
        else:
            df.to_csv(filename, mode='a', index=False, header=False)

while True:
    percentage = scrape_percentage()
    print(percentage)  
    save_to_csv([percentage], 'result.csv')
    time.sleep(2)
