from bs4 import BeautifulSoup as bs
import os, csv

def get_manga_name():
    soup = bs(open('./temp/origin_page.html',encoding='utf-8'), 'lxml')
    data = soup.find_all('span', attrs={'class':'last'})

    name = str(data[0].text).replace('\n','')
    name = str(name).replace(' ','')
    
    os.mkdir(str(name))
    return name

def make_sub_dir(name):
    # 读取CSV文件
    with open('./temp/combine.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        # 跳过CSV文件的第一行（表头）
        next(reader)
        # 遍历CSV文件的每一行
        for row in reader:
            # 获取目录名称和文件内容
            dir_name = row[1]
            url_content = row[0]
            dir_name = './'+name+'/'+dir_name
            # 创建目录
            with open('./temp/dir_files.lst', 'a' ,encoding='utf-8') as f:
                f.write(dir_name)
                f.write('\n')
            f.close()
            os.makedirs(dir_name, exist_ok=True)
            # 在目录下创建文件并写入内容
            with open(os.path.join(dir_name, 'file.txt'), 'w', encoding='utf-8') as file:
                file.write(url_content)