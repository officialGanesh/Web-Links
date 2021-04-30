
import requests ,lxml
from bs4 import BeautifulSoup as bs

def Find_links():

    try:
        
        r = requests.get('https://in.linkedin.com/')
        r.raise_for_status

        soup = bs(r.text,'lxml')
        print(soup.title.text)

        links = set((soup.find_all('a')))

        for link in links:
            print(link.get('href'))

    except Exception as e:
        print("Something Went Wrong 💢")


if __name__ == "__main__":

    Find_links()
    print("Code Completed 🔥")