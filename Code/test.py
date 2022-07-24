class Person:
    
    def __init__(self, _name, _gender, _age):
        self.name = _name;
        self.gender = _gender;
        self.age = _age;
        print("%s来了" % self.name);
    
    def __del__(self):
        print("%s去了" % self.name);
        
    def __str__(self):
        return "我是%s" % self.name;
    
    def grow(self):
        self.age += 1;

test = Person("张三", "男", 30);
print(test);
print(test.age);
test.grow();
print(test.age);