# coding = utf-8
# 测试traceback模块
import traceback

# try:
#     print("step1")
#     num = 1/0
# except:
#     traceback.print_exc()

# 将异常信息输出到指定文件中
try:
    print("step1")
    num = 1/0
except:
    with open("d:/a.txt", "a") as f:
        traceback.print_exc(file=f)