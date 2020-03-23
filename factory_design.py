# 测试工厂模式


class CarFactory:

    def create_car(self, brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"


class Benz:
    pass


class BMW:
    pass


class BYD:
    pass


factory = CarFactory()
c1 = factory.create_car("宝马")
c2 = factory.create_car("奔驰")
c3 = factory.create_car("比亚迪")
c4 = factory.create_car("奥迪")

print(c1)
print(c2)
print(c3)
print(c4)