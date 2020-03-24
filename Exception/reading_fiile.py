# coding = utf-8
# 测试读文件时finally的作用
try:
    open_file = open("d:/ab.txt", "r")
    content = open_file.readline()
    print(content)
except BaseException as e:
    print(e)
    print("文件未找到")
finally:
    print("run in finally,关闭资源。")
    try:
        open_file.close()
    except BaseException as e:
        print(e)
print("程序执行结束")

