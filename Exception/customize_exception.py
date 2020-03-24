# coding = utf-8
# 测试自定义异常


class AgeError(Exception):      # 继承Exception

    def __init__(self, errorinfo):
        Exception.__init__(self)
        self.errorInfo = errorinfo

    def __str__(self):
        return str(self.errorInfo)+",年龄错误！应该在1-150之间"


##############测试代码#################


if __name__ == '__main__':
    age = int(input("please input you age:"))
    if age < 1 or age > 150:
        raise AgeError(age)
    else:
        print("正常的年龄：", age)
