# 测试CSV文件的读取和写入

import csv

with open(r"陕西证书名单.csv","r") as f:
    a_csv = csv.reader(f)
#    print(list(a_csv))
    for row in a_csv:
        print(row)

with open(r"ee.csv", "w", encoding="utf-8") as f:
    b_csv = csv.writer(f)
    b_csv.writerow(["id", "name", "age"])
    for i in range(100):
        b_csv.writerow([1, "左航伟", "18"])
    c = [[1, "左航伟", "18"],[2, "王宇", "19"]]
    b_csv.writerows(c)