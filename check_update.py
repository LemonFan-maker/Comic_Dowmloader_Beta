import pandas as pd
import csv

def loading_new_html(headers, url, dest):
    from make_html import get_manga_chapterlist
    get_manga_chapterlist(headers=headers, url=url, dest=dest)
    from get_chapterlist import get_chapterlist
    get_chapterlist(dest='./temp/new')
    from make_new import make_csv
    make_csv(chapterlist='./temp/new/chapter.lst', namelist='./temp/new/chapter_name.lst', destcsv='./temp/new/combine.csv')
    # 对比
    df1 = pd.read_csv('./temp/new/combine.csv')
    df2 = pd.read_csv('./temp/combine.csv')

    # 对比两个文件，并找出不同的地方
    df_diff = pd.concat([df1,df2]).drop_duplicates(keep=False)

    # 将不同的地方保存为一个新文件
    df_diff.to_csv('./temp/diff.csv', index=False)

    # 读取csv数据
    with open('./temp/diff.csv', 'r', encoding='utf-8') as csv_file:
        data = csv_file.readlines()
        reader = csv.reader(data)
        #next(reader)
        for row in reader:
            # 获取目录名称和文件内容
            file_name = row[1]
            url_address = row[0]
        if len(file_name) == 4 and len(url_address) == 7:
            print('没有可用更新')
        else:
            print('有更新力!')

#loading_new_html(headers=headers, url=urls, dest='./temp/new')