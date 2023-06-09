from bs4 import BeautifulSoup as bs
import requests

def get_manga_chapterlist(headers, url, dest):
    url_data = url.replace("manga", "chapterlist")

    url_data = requests.get(url_data, headers).text
    soup = bs(url_data, 'lxml')
    data = soup.prettify()

    url_data2 = requests.get(url, headers).text
    soup2 = bs(url_data2, 'lxml')
    data2 = soup2.prettify()

    chapter_list = dest + '/chapterlist_page.html'
    origin_list = dest + '/origin_page.html'

    with open(chapter_list, 'w', encoding='utf-8') as f:
        f.write(data)
    f.close()
    
    with open(origin_list, 'w', encoding='utf-8') as g:
        g.write(data2)
    g.close()
