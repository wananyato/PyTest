with open(r"d:/20190613232904.jpg", "rb")as souce:
    with open("test.jpg", "wb") as dest:
        for a in souce.readlines():
            dest.write(a)
print("图片拷贝完成！")