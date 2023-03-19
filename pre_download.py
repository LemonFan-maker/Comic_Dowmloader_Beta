from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import requests, re
from make_new import make_csv

# headers = {
#         "origin": "https://baozimh.org",
#         "user-agent": UserAgent().random
# }

def get_one_manga(url, headers, save_url, save_number, dest_addr):
    data = requests.get(url, headers=headers)
    data.encoding='utf-8'
    data = data.text
    soup = bs(data, 'lxml')
    all_item = soup.select("#post-1985862 > div > div > div > div > div.gb-container.gb-container-1c32c60b > div")
    
    for items in all_item:
        img = items.find_all('img', attrs={'class':'lazyload'})

        last_number = [titles.get('title') for titles in img]
        pattern = "章节内容\s"
        last_number = last_number[-1]
        last_number = int(re.sub(pattern, "", last_number))

        last_url = [imgs.get('data-src') for imgs in img]

        for i in last_url:
            with open(save_url, 'a', encoding='utf-8') as f:
                f.write(i)
                f.write('\n')
            f.close()

        for u in range(1, last_number+1):
            with open(save_number, 'a', encoding='utf-8') as g:
                g.write(str(u))
                g.write('\n')
            g.close()
            
    make_csv(save_url, save_number, dest_addr)
