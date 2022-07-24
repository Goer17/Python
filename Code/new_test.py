class Dog:
    def bark(self):
        print("汪汪汪");

class XiaoTianQuan(Dog):
    def bark(self):
        super().bark();
        print("%%%%%%");


xtq = XiaoTianQuan();

xtq.bark();