info = []; #成员信息列表

def printAllInfo():
    # 打印全部员工信息
    for item in info:
        print(item);

def addInfo():
    # 新增员工信息
    name = input("输入员工姓名：");
    age = int(input("输入员工年龄："));
    id = input("输入员工ID：");
    info.append({"name": name, "age": age, "id": id});
    print("添加员工 %s 成功" % name);

def delInfo(targetName):
    # 删除员工信息
    for item in info:
        if item["name"] == targetName:
            info.remove(item);
            print("删除员工 %s 成功" % targetName);
            break;
    else:
        print("没有找到员工 %s" % targetName);

def changeInfo(targetname):
    # 修改员工信息
    for item in info:
        if item["name"] == targetname:
            _name = input("更新员工姓名：");
            _age = int(input("更新员工年龄："));
            _id = input("更新员工ID：");
            item["name"] = _name;
            item["age"] = _age;
            item["id"] = _id;
            print("更新完成");
            break;
    else:
        print("没有找到员工 %s" % targetname);

def findInfo(targetName):
    # 查找员工信息
    for item in info:
        if item["name"] == targetName:
            print(item);
            break;
    else:
        print("没有找到员工 %s" % targetName);