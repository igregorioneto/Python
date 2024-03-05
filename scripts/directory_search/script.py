import requests, sys

def directory_search(site_url, wordlist_path):
    try:
        with open(wordlist_path, 'r') as f:
            wordlist = f.read().splitlines()

        for directory in wordlist:
            url = f"{site_url}/{directory}"
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Diretório encontrado: {url}")
            else:
                print(f"Diretório não encontrado: {url}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 script.py <site_url> <wordlist_path>")
        sys.exit(1)

    site_url = sys.argv[1]
    wordlist_path = sys.argv[2]

    directory_search(site_url, wordlist_path)