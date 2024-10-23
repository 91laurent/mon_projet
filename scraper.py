
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Exemple : extraire tous les titres h1
    titles = soup.find_all('h1')
    
    for title in titles:
        print(title.text)

if __name__ == "__main__":
    scrape_website('https://example.com')  # Remplacez par l'URL que vous souhaitez scraper
