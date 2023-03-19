from bs4 import BeautifulSoup as bs
from lxml import etree
import re

def get_chapterlist():
    soup = bs(open('./temp/chapterlist_page.html', 'r', encoding='utf-8'), 'lxml')
    data = soup.find_all('a', attrs={'class':'wp-manga-chapterlist'})

    for i in data:
        with open('./temp/chapter.lst', 'a', encoding='utf-8') as f:
            f.write(str(i['href']))
            f.write('\n')
        f.close()
        
    with open('./temp/chapter.lst', 'r', encoding='utf-8') as r:
        data = r.readlines()
    
    list = ''.join(data)
    list = list.split('\n')
    del(list[-1])

    # 获取章节名称并保存文件
    for i in soup.find_all('a', attrs={'class':'wp-manga-chapterlist'}):
        src = re.search('id="(.*?)"', str(i)).group(1)
        sele = '//*[@id="' + src + '"]/text()'
        selector = etree.parse('./temp/chapterlist_page.html', etree.HTMLParser())
        rst2 = selector.xpath(sele)
        rst2 = rst2[0]
        name = str(rst2).replace('\n', '')
        name = str(name).replace('\r', '')
        name = str(name).replace(' ', '')
        with open('./temp/chapter_name.lst', 'a', encoding='utf-8') as f:
            f.write(str(name))
            f.write('\n')
        f.close()