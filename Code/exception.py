passwordTooShort = Exception("密码长度不够");

def input_password():
    """
    提示用户输入密码
    密码长度必须 >= 8
    """

    pwd = input("请输入密码");
    if len(pwd) >= 8:
        return pwd;
    
    raise passwordTooShort;

try:
    password = input_password();

except passwordTooShort:
    print("密码长度必须 >= 8");

except Exception as error_unknow:
    print("未知错误 %s" % error_unknow);