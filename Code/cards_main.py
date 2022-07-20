import cards_tools;

while True:
    print("0.显示所有信息")
    print("1.新增");
    print("2.删除");
    print("3.修改");
    print("4.查找");
    print("5.退出程序");
    action = int(input("选择功能："));
    if action == 0:
        cards_tools.printAllInfo();
    elif action == 1:
        cards_tools.addInfo();
    elif action == 2:
        targetName = input("输入目标姓名：");
        cards_tools.delInfo(targetName);
    elif action == 3:
        targetName = input("输入目标姓名：");
        cards_tools.changeInfo(targetName);
    elif action == 4:
        targetName = input("输入目标姓名：");
        cards_tools.findInfo(targetName);
    elif action == 5:
        print("退出程序成功");
        break;