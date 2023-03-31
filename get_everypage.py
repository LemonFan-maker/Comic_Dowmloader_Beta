from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import os, threading, time

def read_files_in_folder(folder):
        with open(os.path.join(folder, 'file.txt'), 'r', encoding='utf-8') as g:
            url = g.read()
        headers = {
            "origin": "https://baozimh.org",
            "user-agent": UserAgent().random
        }
        
def run_threads_on_folders():
    with open('./temp/dir_files.lst', 'r', encoding='utf-8') as f:
        data = f.readlines()
        file1_list = ''.join(data)
        file1_list = file1_list.split('\n')
        del(file1_list[-1]) 
            
    threads = []

    for folder in file1_list:
        t = threading.Thread(target=read_files_in_folder, args=(folder,))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':

    start_t = time.time()
    run_threads_on_folders()
    stop_t = time.time()
    print(float(stop_t)-float(start_t))