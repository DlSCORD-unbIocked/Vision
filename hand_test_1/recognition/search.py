import webbrowser
import requests
from bs4 import BeautifulSoup

def search_web(query):
    search_url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(search_url)

def search_wikipedia(query):
    search_url = "https://wikipedia.org/w/index.php?search=" + query.replace(" ", "+")
    webbrowser.open(search_url)

def search_news(query):
    search_url = "https://news.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(search_url)

def search_youtube(query):
    search_url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
    webbrowser.open(search_url)

    search = 'tree'

def watch_youtube(query):
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

    html = requests.get('https://www.youtube.com/results?search_query='+ query.replace(" ", "+"), headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    print(html)
    for link in soup.find_all('a'):
        print(link.get('href'))
        if '/watch?v=' in link.get('href'):
            print(link.get('href'))
            # May change when Youtube Website may get updated in the future.
            video_link = link.get('href')


if __name__ == "__main__":

    watch_youtube("tree")