import requests
from bs4 import BeautifulSoup
import sys

# Crawler Links Function
def crawl_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = []
            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    links.append(href)
            return links
        else:
            print("Erro: Não foi possível acessar a URL.")
            return[]
    except Exception as e:
        print(f"Error: {e}")
        return[]
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python script.py <url>")
        sys.exit(0)

    url = sys.argv[1]
    links = crawl_links(url)
    print(f"Links encontrados em {url}:")
    for link in links:
        print(link)
