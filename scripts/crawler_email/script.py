import requests
from bs4 import BeautifulSoup
import re
import sys

def crawl_emails(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = set(re.findall(email_pattern, soup.get_text()))
            return emails
        else:
            print("Erro: Não foi possível acessar a URL")
            return set()
    except Exception as e:
        print(f"Erro: {e}")
        return set()
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    emails = crawl_emails(url)
    if emails:
        print(f"E-mails encontrados em {url}:")
        for email in emails:
            print(email)
    else:
        print(f"Nenhum e-mail encontrado em {url}")
       
    sys.exit(1)