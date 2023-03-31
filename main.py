from mkdir import get_manga_name, make_sub_dir
from make_html import get_manga_chapterlist
from make_new import make_csv
from get_chapterlist import get_chapterlist
from pre_download import get_one_manga
from download import download

from fake_useragent import UserAgent
import os, shutil, threading

urls = 'https://baozimh.org/manga/qingkongcheng-dongmanke/'
headers = {
        "origin": "https://baozimh.org",
        "user-agent": UserAgent().random
}

os.mkdir('temp')
os.mkdir('temp/new')

# 保存html到本地解析
get_manga_chapterlist(url=urls, headers=headers, dest='./temp')

# 获取漫画名称并创建文件夹
name = get_manga_name()

# 获取章节目录
get_chapterlist(dest='./temp')

# 创建csv文件
make_csv('./temp/chapter.lst', './temp/chapter_name.lst', './temp/combine.csv')

# 创建章节目录
make_sub_dir(name=name)

with open('./temp/dir_files.lst', 'r', encoding='utf-8') as f:
    data = f.readlines()
    dest_folders = ''.join(data)
    dest_folders = dest_folders.split('\n')
    del(dest_folders[-1])
f.close()

# 漫画解析
filepaths = [item + '/file.txt' for item in dest_folders]
savedest = [item + '/download.txt' for item in dest_folders]
save_url = [item + '/pic_address.txt' for item in dest_folders]
save_number = [item + '/pic_number.txt' for item in dest_folders]
dest_addr = [item + '/dest_csv.csv' for item in dest_folders]
dest_addr = list(dest_addr)

for i in dest_addr:
    with open('./temp/dest_addr.txt', 'a', encoding='utf-8') as f:
        f.write(i)
        f.write('\n')
    f.close()

processes_v1 = os.cpu_count()**8
thread_pool_v1 = threading.BoundedSemaphore(value=processes_v1)

def process_manga(txtfile, headers, save_url, save_number, dest_addr):
	thread_pool_v1.acquire()
	with open(txtfile, 'r', encoding='utf-8') as f:
		data = f.read()
	get_one_manga(data, headers, save_url, save_number, dest_addr)
	f.close()
	thread_pool_v1.release()

thread_list_v1 = []
for filepaths, save_url, save_number, dest_addr in zip(filepaths,save_url, save_number, dest_addr):
	t = threading.Thread(target=process_manga, args=(filepaths, headers, save_url, save_number, dest_addr))
	thread_list_v1.append(t)

for t in thread_list_v1:
    t.start()

for t in thread_list_v1:
    t.join()

print('解析完成!')

# 漫画下载
with open('./temp/dest_addr.txt', 'r', encoding='utf-8') as r:
    data = r.readlines()
    list = ''.join(data)
    list = list.split('\n')
    del(list[-1])
    r.close()

for i in list:
    try:
        download(i)
    except:
        print('ERRRRRR!')
        download(i)

print('下载完成!')
# shutil.rmtree('temp')