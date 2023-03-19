import urllib, csv
import urllib.request,urllib.response
from fake_useragent import UserAgent

def download(dest_csv):
    with open(dest_csv, 'r', encoding='utf-8') as csv_file:
        data = csv_file.readlines()
        reader = csv.reader(data)
        next(reader)
        for row in reader:
            # 获取目录名称和文件内容
            file_name = row[1]
            url_address = row[0]
            print(url_address)
            parts = dest_csv.rsplit('/', 1)
            data = parts[0] + "/" + file_name+'.jpg'
            print(data)
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', UserAgent().random),('origin', 'https://baozimh.org')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(url_address, filename=data)
    csv_file.close()