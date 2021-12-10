import requests
from bs4 import BeautifulSoup


def scraping():
    response = requests.get('https://teratail.com/questions/373284')
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').get_text()
    return title
