import csv

def make_csv(chapterlist, namelist, destcsv):
    with open(chapterlist, 'r', encoding='utf-8') as file1, open(namelist, 'r', encoding='utf-8') as file2:
        file1_content = file1.readlines()
        file2_content = file2.readlines()

        file1_list = ''.join(file1_content)
        file1_list = file1_list.split('\n')
        del(file1_list[-1])
        
        file2_list = ''.join(file2_content)
        file2_list = file2_list.split('\n')
        del(file2_list[-1])

    with open(destcsv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['address', 'name'])  # 写入表头

    for i,u in zip(file1_list, file2_list):
        with open(destcsv, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([i, u])  # 写入数据