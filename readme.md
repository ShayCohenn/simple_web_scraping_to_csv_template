# Simple web scraping template

### ***Saves the data to a csv file
### ***Used for tracking precentages of stocks

## Installation

Create virtual enviroment
```bash
python -m virtualenv env
```
```bash
.\env\Scripts\activate
```
Copy the repository
```bash 
git clone https://github.com/ShayCohenn/simple_web_scraping_to_csv_template.git
```
Install the packages
```bash
pip install -r requirements.txt
```
Add your URL of the site you want to scrape, the html tag and the class name of the element you need.
```python
def scrape_percentage():
    data = requests.get('placeholder_url') # Put the link to the website here
    html_content = data.text
    soup = BeautifulSoup(html_content, 'lxml')

# 1 - Placeholder for the HTML tag you want to search
# 2 - Placeholder for the class name, can be swaped with id
    percentage_span = soup.find('placeholder1_html_tag', class_='placeholder2_classname')

```

To run:
```bash
python ./main.py
```
