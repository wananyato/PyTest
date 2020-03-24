# coding = utf-8
# 测试with上下文管理（with不是用来取代try的）

# try:
#     f = open("d:/ab.txt", "r")
#     content = f.readline()
#     print(content)
# except BaseException as e:
#     print(e)
#     print("文件未找到")
# finally:
#     print("run in finally")
#     try:
#         f.close()
#     except BaseException as e:
#         print(e)
with open("d:/a.txt") as f:
    content = f.readline()
    print(content)

print("end of program!")