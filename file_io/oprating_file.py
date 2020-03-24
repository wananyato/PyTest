# 给文件中插入内容！
f = open(r"h:\test.txt", "w", encoding="utf-8")
# s = input("请输入测试内容(输入内容将会写入test文件中)：")
f.write("左航伟\n小宇宙\n我爱你\n")
f.close()