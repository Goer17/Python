# Personal Note For Python

<center>
    <img src="https://typora-1313035735.cos.ap-nanjing.myqcloud.com/img/starry_sky.png" alt="starry_sky" style="zoom:50%;" />
</center>

# Part A



## 前置说明



### Python 简介

Python是一门强大的**解释性语言**，解释器由吉多开发，向全球开源。

**Python特点：**

- 完全**面向对象**；
- Python拥有一个强大的**标准库**；
- Python社区提供了大量的**第三方模板**。

**Python的优缺点：**

- 优点：
  1. 简单易学；
  2. 免费开源；
  3. 可扩展性强；
  4. 丰富的库；
  5. 面对对象；
  6. 跨平台性强。（解释性语言的特点）
- 缺点：
  1. 运行效率低；
  2. 国内市场小；
  3. 中文资料匮乏。



### 在终端利用解释器运行Python代码

eg:

- 在终端下运行test.py：

  ```python
  # test.py
  
  print("Hello world!");
  ```

- 终端指令（利用python的解释器打开）：

  ```cmd
  $ python test.py #利用2.x版本解释器
  ```
  
  ```cmd
  $ python3 test.py #利用3.x版本解释器
  ```

> **print**是**Python**的一个函数， 其作用是打印 “ ” 内部的内容。



### 交互式运行Python代码

- 在终端输入解释器名：

  eg:

  ```cmd
  $ python
  ```

  或

  ```cmd
  $ python3
  ```

  即可在Python的Shell直接输入Python的代码。

- 交互式运行的优缺点

  - 优点：
    - 适用于学习/验证Python的局部代码；
  - 缺点：
    - 代码不能保存；
    - 不适合运行太大的程序。

- 退出Shell，返回终端窗口：

  1. 在终端输入:

     ```cmd
     $ exit()
     ```

     对于 ipython 解释器则是直接输入exit：

     ```cmd
     $ exit
     ```

  2. 直接输入Ctrl + D。



### Python常见bug

1. 每行代码只负责完成一个动作；
2. Python格式相当严格，每行代码前都不要加空格；
3. Python 2.x 默认不支持中文。（Python 3.x 的解释器名为 **python3**）



## 程序注释



### 单行注释

```python
# 注释内容
```

### 多行注释

```python
"""

多行注释内容
...
...
...

"""
```

### TODO注释

```python
# TODO(name/email) ...要做的事
```

> TODO注释用于告诉开发者后续要做的事情



## 运算符



### 算数运算符简介

| 算数运算符 | 描述 | 实例           |
| ---------- | ---- | -------------- |
| +          | 加   | 20 + 10 == 30  |
| -          | 减   | 20 - 10 == 10  |
| *          | 乘   | 20 * 10 == 200 |
| /          | 除   | 10 / 20 == 0.5 |
| //         | 整除 | 9 // 2 == 4    |
| %          | 取余 | 9 % 5 == 4     |
| **         | 幂   | 2 ** 3 == 8    |

- 在Python中 “ + ” 和 “ * ” 还可以用来做字符串运算运算:

```python
# in:
print("I love " + "coding");
# out:
"I love coding"
```

```python
# in:
print("-" * 10);
# out:
"----------"
```



### 比较运算符

| 比较运算符 | 含义     |
| ---------- | -------- |
| ==         | 等于     |
| !=         | 不等于   |
| >          | 大于     |
| <          | 小于     |
| >=         | 大于等于 |
| <=         | 小于等于 |



### 逻辑运算符

| 逻辑运算符 | 说明 |
| ---------- | ---- |
| and        | 与   |
| or         | 或   |
| not        | 非   |



### 赋值运算符

| 赋值运算符 | 说明                       |
| ---------- | -------------------------- |
| =          | 简单赋值                   |
| +=         | c += a 等价于 c = c + a    |
| -=         | c -= a 等价于 c = c - a    |
| *=         | c *= a 等价于 c = c * a    |
| /=         | c /= a 等价于 c = c / a    |
| //=        | c //= a 等价于 c = c // a  |
| %=         | c %= a 等价于 c = c % a    |
| **=        | c ** = a 等价于 c = c ** a |



### 运算符优先级





## 变量





### 如何定义一个变量

> 变量名 = 值

eg:

```python
var = 2022;
password = "abc123456";
```



### 变量类型

- 数据类型可以分为**数字型**与**非数字型**；

- 数字型：

  - 整型（int）
  - 浮点型（float）
  - 布尔型（bool）
  - 复数型（complex）

  > 在Python 2.x 中，整数根据保存数据的长度还可以分为：
  >
  > - 整型 （int）
  > - 长整型（long）

- 非数字型：

  - 字符串（str）
  - 列表（list）
  - 元组（tuple）
  - 字典（dictionary）

  > 在Python中，所有非数字型变量都支持以下特点：
  >
  > 1. 都是一个序列（sequence），也可以理解为容器；
  > 2. 取值 []；
  > 3. 遍历 for in；
  > 4. 计算长度、最小/最大值、比较、删除；
  > 5. 连接 + 和重复 *
  > 6. 切片

- type()函数得到变量具体类型：

  ```python
  type(var_name);
  ```

  

### 变量的输入

- input()函数

  ```python
  var_name = input("提示信息:XXX"); #记录用户输入的字符串
  ```



### 类型转换函数

| 函数     | 说明                |
| -------- | ------------------- |
| int(x)   | 将x转换为一个整数   |
| float(x) | 将x转换成一个浮点数 |



### 变量的格式化输出

| 格式化字符 | 含义               |
| ---------- | ------------------ |
| %s         | 字符串             |
| %d         | 有符号的十进制整数 |
| %f         | 浮点数             |
| %%         | 输出%              |



- 格式化语法

  ```python
  print("格式化字符串" % (变量1, 变量2, ...));
  ```



### 高级变量类型



#### 字符串

- 字符串用 " " 定义，若字符串中有 “ ” ，则字符串使用单引号定义；

  ```python
  str_name = "string";
  ```

- 字符串的常用操作：

  ```python
  #得到字符串长度
  len(str_name);
  #统计子字符串出现的位置与次数
  str_name.index(substr);
  str_name.count(substr);
  #判断类型
  str_name.isspace(); #是否只包含空格
  str_name.isalnum(); #是否包含至少一个字符且所有字符都是字母或数字
  str_name.isalpha(); #是否包含至少一个字符且所有字符都是字母
  str_name.isdecimal(); #是否只包含全角数字
  str_name.isdigit(); #是否包含全角数字或者其他unicode字符集的数字
  str_name.isnumeric(); #是否包含全角数字或汉字数字
  str_name.istitle(); #每个单词的首字母是否大写
  str_name.islower(); #判断所有字符是否都小写
  str_name,isupper(); #判断所有字符是否都大写
  str_name.startswith(substr); #判断是否以substr开始
  str_name.endswith(substr); #判断是否以substr结束
  #查找与替换类型
  str_name.find(substr, start = 0, end = len(str_name)); #检测substr的位置，若存在则返回开始的索引，否则返回-1
  str_name.rfind(substr, start = 0, end = len(str_name)); #同上，从右边开始寻找
  str_name.replace(old_str, new_str, num = str_name.count(old_str)); #替换旧字符串成新字符串
  #大小写转换
  str_name.capitalize(); #把字符串的第一个字符大写
  str_name.title(); #把字符串每个单词的首字母大写
  str_name.lower(); #把字符串的所有大写字符化为小写
  str_name.upper(); #把字符串的所有小写字符化为大写
  str_name.swapcase(); #翻转字符串的大小写
  #文本对齐
  str_name.ljust(); #左对齐
  str_name.rjust(); #右对齐
  str_name.center(); #居中
  #去除空白字符
  str_name.lstrip(); #左边截去
  str_name.rstrip(); #右边截去
  str_name.strip(); #截去两边的空白字符
  #拆分与连接
  str_name.split(divstr, num); #以divstr为分隔符对字符串进行拆分，拆分成num+1个子字符串，返回拆分后的列表
  str_name.join(seq); #以str_name作为分隔符，将seq的所有元素合并成一个新的字符串并返回
  ```

- 字符串的切片（对列表、元组同样适用）：

> 语法：
>
> 字符串[开始索引:结束索引:步长]
>
> 注：结束索引不会记录
>
> Python 提供的倒序索引：最后一个元素的索引为-1，向前依次递减



#### 列表

- 列表的定义：

  - List (列表) 是 Python 中最常用的数据类型，在其它语言通常叫数组；

  - 列表用 [] 定义；

    eg:

    ```python
    name_list = [1, 2, 3];
    
    name_list_null = []; #空列表
    ```

  - Python 中的列表存在边界检查，超出索引范围会报错。

- 列表的常用操作：

  ```python
  #查找
  name_list.index(val); #查找特定值的下标
  #增加数据
  name_list.append(obj); #末尾增加数据
  name_list.insert(index, obj); #在指定索引插入数据
  name_list.insert(add_list); #将一个新的列表新增在原列表后面
  #删除数据
  name_list.remove(val); #删除指定数据（删除索引最小的那个）
  name_list.pop(); #将列表末尾的数据删除
  name_list.pop(index); #将列表指定索引的数据删除
  name_list.clear(); #清空列表
  del name_list[index]; #删除列表指定索引的数据
  #统计数据
  len(name_list); #返回列表的长度
  name_list.count(val); #返回指定值出现的次数
  #排序
  name_list.sort(); #升序排列
  name_list.sort(reverse = True); #降序排列
  name_list.reverse(); #翻转/逆序
  ```

  

#### 元组

- 元组（Tuple）与列表类似，不同之处在于**元组的元素不能修改**；
  - 元组表示多个元素组成的序列；
  - 元组在 Python 开发中有特定的应用场景；
- 用于储存一串信息，数据之间使用 " , " 分隔；
- 元组用 " () " 定义；
- 元组的索引从0开始。

```python
tuple_name = ("Zhang San", 18, 1.80);
tuple_name = (); #定义空元组
```

> 如果元组只有一个元素，括号还要增加一个逗号。

```python
tuple_name = (2022); #此时tuple_name会被识别为int类变量
tuple_name = (2022, ); #此时tuple_name会被识别为元组类变量
```

- 元组的常用操作：

  ```python
  tuple_name.index(val);
  tuple_name.count(val);
  len(tuple_name);
  #起作用均与列表一致
  ```

- 元组和列表之间的转换：

  ```python
  list(tuple_name); #把元组转换成列表
  tuple(list_name); #把列表转换成元组
  ```



#### 字典

- 字典是 Python 除列表之外最灵活的数据类型；

- 字典同样可以用来储存多个数据；

- 字典是无须的对象集合；

- 字典通过 " {} " 定义：

  ```python
  dict_name = {
      "key_1": val_1,
      "key_2": val_2,
      "key_3": val_3,
      #...
      #key是索引，val是数据，每个key是唯一的
  };
  ```

- 字典的常用操作：

  ```python
  #取值
  dict_name["key"];
  #修改数据，若key不存在，则新建键值对
  dict_name.setdefault("key", val);
  #删除
  dict_name.pop("key");
  #清空键值对
  dict_name.clear();
  #统计键值对数量
  len(dict_name);
  #合并字典，重复的键值对会被覆盖
  dict_1.update(dict_2);
  ```
  
  

### 公共方法

-  Python 内置函数：

  | 函数      | 描述                                         | 备注                           |
  | --------- | -------------------------------------------- | ------------------------------ |
  | len(item) | 计算容器的元素个数                           | 无                             |
  | del(item) | 删除变量                                     | del也可以作为关键字使用        |
  | max(item) | 返回容器元素的最大值                         | 如果是字典，只针对key比较      |
  | min(item) | 返回容器元素的最小值                         | 如果是字典，只针对key比较      |
  | cmp(item) | 比较两个值，小于返回-1，等于返回0，大于返回1 | **Python 3.x 取消了cmp()函数** |

  > **Python 3.x 可以直接使用比较运算符取代cmp()函数；**

- 切片：

  方法同字符串，字典是无序容器，不能切片。

- 高级变量运算符：

  | 运算符                       | Python实例            | 结果         | 描述               | 支持的类型               |
  | ---------------------------- | --------------------- | ------------ | ------------------ | ------------------------ |
  | +                            | [1, 2] + [3, 4]       | [1, 2, 3, 4] | 合并               | 字符串、列表、元组       |
  | *                            | ["Hi"]  * 2           | ["Hi", "Hi"] | 重复               | 字符串、列表、元组       |
  | in                           | 3 in (1, 2, 3)        | Ture         | 判断元素是否存在   | 字符串、列表、元组、字典 |
  | not in                       | 4 not in (1, 2, 3)    | True         | 判断元素是否不存在 | 字符串、列表、元组、字典 |
  | 比较运算符(>、>=、==、<、<=) | (1, 2, 3) < (2, 2, 3) | True         | 元素比较           | 字符串、列表、元组       |

  > 对于字典而言，in运算符只能判断字典的key；
  >
  > 对于列表而言，+= 运算符本质上是调用了extend()方法。



### 变量的引用

- id()函数：

  > 查看变量的地址

  ```python
  id(var_name); #返回变量的地址
  ```

- 在 Python 中，变量的命名类似于便签纸贴在数据上，**给一个变量赋值本质上是修改了数据的引用**；

  eg:

  ```python
  var_1 = 1;
  var_2 = 1;
  print(id(var_1), " ", id(var_2), " ", id(1));
  var_1 = 2;
  print(id(var_1), " ", id(var_2), " ", id(2));
  ```

  > out:
  >
  > 1974013722864   1974013722864   1974013722864
  > 1974013722896   1974013722864   1974013722896

- 在 Python 中**函数实参都是通过引用调用的，函数返回的变量也是引用**；

- Python 中**无法通过在函数内直接赋值改变全局变量的值**；

  eg:

  ```python
  var_test = 1;
  
  def fun():
      var_test = 0; #这里相当于定义了一个局部变量，与全局的var_test不是一个东西
  
  fun();
  print(var_test);
  ```

  > out:
  >
  > 1

  若要在函数内部修改全局变量的值，考虑使用 global 关键词；

  eg:

  ```python
  var_test = 1;
  
  def fun():
      global var_test;
      var_test = 0;
  
  fun();
  print(var_test);
  ```

  > out:
  >
  > 0

- 可变类型与不可变类型：

  - 不可变类型（内存中的数据不能被修改）：
    - 数字类
    - 字符串
    - 元组
  - 可变类型（内存中的数据可以被修改）：
    - 列表
    - 字典

  > 注意：**字典的 key 只能使用不可变类型的数据。**

## 基本语法



### 判断

- 单个 if 语句

```python
if #要判断的条件:
	#条件成立时执行的代码
```

> if 语句以及缩进部分构成一个**完整的代码块**



- if - else 语句


```python
if #要判断的条件:
	#条件成立时执行的代码
else
	#条件不成立时执行的代码
```



- elif 语句

```python
if #条件1:
	#执行代码1
elif #条件2:
	#执行代码2
elif #条件3:
	#执行代码3
	...
else
	#上述条件都不成立则执行的代码
```



### 循环

- while 循环：

```python
while #条件:
	#条件成立时执行的代码
```

- for 循环：

  > 在 Python 中，可以使用for循环遍历所有非数字型类型的变量：字符串、列表、元组以及字典。

```python
for item in obj:
    #执行代码
else:
    #不通过break退出循环，循环结束后执行的代码
```



### pass关键词

> 如果在开发程序时不希望立刻编写分支内部的代码，可以使用pass关键词，pass表示一个占位符，能够确保程序的正确性。

- eg：

  ```python
  if #条件:
  	pass; #此处不需要执行代码
  else:
      #执行代码
  ```

  



## 函数与模块



### 函数

- 定义函数格式如下：

  ```python
  def function_name(var1, var2):
      """
      函数注释
      """
  	#函数封装的代码
  	...
      
      return val; #返回值（可以没有）
  ```

  > 可以返回多个值：
  >
  > return val1, val2, ...；
  >
  > 相当于返回一个元组；
  >
  > 同时可以用多个变量接收返回值：
  >
  > eg：var1, var2, ... = function()；

- 使用模块中的函数：
  （有些类似于 c / cpp 中的头文件）

  > 每一个以拓展名 .py 结尾的 Python 源代码文件都是一个模块；
  >
  > 在模块中定义的全局变量、函数都是模块能直接提供给外界的工具。

  ```python
  import module_name;
  #调用模块
  
  module_name.function(var1, var2, ...);
  module_name.var;
  #调用模块的函数或变量
  ```

- 多值参数：

  - 有时一个函数要处理的参数个数不确定，此时就需要使用多值参数；
  - Python 中有两种多值参数：
    - 参数名前加一个 * 可以接收元组
    - 参数名前加两个 * 可以接收字典
  - 一般在给多值参数命名时，习惯使用以下两个名字：
    - *args -- 存放元组参数
    - **kwargs -- 存放字典参数

```python
def demo(num, *args, **kwargs):
    #执行代码
```

```python
#实例：
def sum_nums(*args):
    #对任意个参数的求和函数
    sum_total = 0;
    for item in args:
        sum_total += item;
    
    return sum_total;
```



### 模块

- 每一个拓展名以 .py 结尾的源代码文件都是一个模块；

- 模块名也是一个标识符，需要符合标识符的命名规则；

- 模块定义的全局变量、函数、类都可以直接提供给外界；

- 模块的导入方式：

  1. import 导入：

     ```python
     import module_1, module_2;
     ```

     ```python
     import module_1;
     import module_2;
     ```

     > 使用 as 指定别名

     ```python
     import module as alias;
     ```

     > 模块别名最好采用大驼峰命名法

  2. from ... import 导入：

     ```python
     from module import tool; #使用模块的局部工具
     ```

     > 局部导入后不需要通过模块名调用工具；
     >
     > 如果从两个不同的模块中导入了同名的成员，那么后导入的成员会覆盖掉先导入的成员，若发生冲突，可以采用 as 取别名来解决。

     ```python
     from module_1 import tool as tool_1;
     from module_2 import tool as tool_2;
     ```

     > 一次性导入所有工具：

     ```python
     from module import *;
     ```

- 模块搜索顺序：

  1. 当前目录

  2. 系统目录

     > Python 中每一个模块都有一个内置属性 file 可以查看模块的完整路径

     ```python
     print(module.__file__); #打印模块路径
     ```

- 在模板导入时，文件内所有没有任何缩进的代码都会被执行一遍；

  > 而一般的开发人员在模块下会有一些测试代码，如何在导入模块时不执行这些代码？
  >
  > —— 利用内置属性 name
  >
  > 直接执行模块时，name 属性为 main，被导入时 name 为模块名。

  eg：

  ```python
  #所有可利用工具，全局变量、函数、类
  
  if __name__ == "__main__":
      #测试代码
  ```

  Python 文件常见格式：

  ```python
  #导入模块
  #定义全局变量
  #定义类
  #定义函数
  
  def main():
      #main函数的执行代码
      
  #根据__name__判断是否执行以下代码
  
  if __name__ == "__main__":
      main();
  ```

  

### 包

- 包是一个包含多个模块的特殊目录；
- 目录下有一个特殊的文件  `__init__.py`；
- 包名的命名方式和变量名一致；
- 使用 `import 包名` 可以一次性导入导入包的**所有模块**。



- `__init__.py` 文件中指定对外界提供的模块列表 ；

  eg：

  ```python
  #从当前目录导入模块列表
  from . import tool;
  import module;
  # ...
  ```



### Python中的常用函数

#### `print()` 函数

- 在默认情况下，print() 函数在输出内容后会自动在末尾增加换行；

- 如果不希望末尾自动换行，可以在print() 函数的输出内容后增加：end = ""；

  ```python
  print("Hello world", end = "");
  ```



#### `eval() `函数

- 将字符串当成有效表达式计算并返回计算结果；

  eg：

  ```python
  print(eval("1 + 1"));
  ```

  > out：
  >
  > 2



### Python中的常用模块

#### 随机数模块 `random`

- 导入随机数的模块：

```python
import random;
```



- 工具介绍：

```python
random.randint(a,b); #生成随机整数n并返回 (a <= n <= b)
```



#### 游戏设计模块 `pygame`

- 导入 `pygame` 模块：

  ```python
  import pygame;
  ```



- 工具介绍：

  - `init()` 函数：

    > 初始化

    ```python
    pygame.init(); #初始化
    ```

  - `quit()` 函数：

    > 退出绘图程序

    ```python
    pygame.quit(); #退出绘图程序
    ```

  - `Rect` 类：

    > 用于描述矩形区域

    ```python
    rect = pygame.Rect(x, y, width, height); #创建对象
    
    # rect.size返回(width, height)的元组
    ```

  - `pygame.display` 模块：

    > 用于创建、管理游戏窗口

    | 方法                        | 说明               |
    | --------------------------- | ------------------ |
    | `pygame.display.set_mode()` | 初始化游戏显示窗口 |
    | `pygame.display.update()`   | 刷新屏幕内容后显示 |

    - `set_mode` 方法详解：

      ```python
      set_mode(resolution = (0, 0), flags = 0, depth = 0);
      ```

      > resolution 指定屏幕的宽和高，默认创建窗口大小和屏幕大小一致；
      >
      > flags 参数指定屏幕的附加选项，例如是否全屏等等；
      >
      > depth 参数表示颜色的位数，默认自动匹配。
      >
      > 返回值：返回游戏的窗口。

      eg：

      ```python
      screen = pygame.display.set_mode((400,700)); #创建游戏窗口
      ```

  - 利用 `pygame` 绘制图像：

    1. 使用 `pygame.image.load()` 加载图像数据；
    2. 使用游戏窗口对象，调用 `blit()` 方法将图像绘制到指定位置；
    3. 调用 `pygame.display.update()` 方法更新整个屏幕的显示。

    eg：

    ```python
    import pygame
    
    pygame.init();
    
    screen = pygame.display.set_mode((480,700));
    
    bg = pygame.image.load("./images/background.png");
    
    screen.blit(bg, (0, 0)); #第二个参数也可以是Rect类
    
    pygame.display.update();
    
    input("按任意键继续...");
    
    pygame.quit();
    ```

  - `pygame.time.Clock` 游戏时钟类控制循环速度：

    1. 创建一个 `pygame.time.Clock` 时钟类对象；
    2. 调用时钟类对象的 `tick` 方法。

    eg：

    ```python
    timer = pygame.time.Clock();
    
    while True:
        clock.tick(frequency); #刷新频率
        #游戏循环代码
    ```

    

  


# Part B

- **面向对象编程 —— Object Oriented Programming（OOP）**



## 类和对象



### 类

#### 基本概念和语法

- 类的三要素：
  - **类名（类的命名最好采用大驼峰命名法）**
  - **属性**
  - **方法**
  
- 类的定义：

  ```python
  class NameClass:
      
      def __init__(self, var, ...):
          #初始化方法
          self.var_1 = val_1;
          self.var_2 = val_2;
          #设定初始属性
          #...
          
      def __del__(self):
          #销毁方法
          
      def __str__(self):
          #自定义print输出方法
          #...
          return stringEnd; #返回格式化字符串
      
      def fun_1(self, var, ...):
          #方法1
          
      def fun_2(self, var, ...):
          #方法2
  ```

  eg:

  ```python
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
  ```




#### 定义私有属性和私有方法

- 在属性或方法前加上 "__" 就是私有属性或私有方法；

  ```python
  self.__var = val; #私有属性只能在类内访问
  
  def __fun(self, var, ...):
      #私有方法
  ```

- 私有属性或方法的调用：

  ```python
  obj._ClassName__var;
  obj._ClassName__fun();
  ```

  > 因此在 Python 中没有绝对的私有




#### 实例属性和类属性

- 实例属性：即具体对象的属性，通过初始化方法定义，定义对象的过程叫做实例化，其属性称为实例属性；

- 类属性：某个类的属性，在类内通过直接赋值定义，可以通过 **类名.属性** 的方式调用。

  > 在 Python 中类也是一种特殊的对象，定义类的时候生成，有且仅有一份；
  >
  > 可以类比 C++ 中的静态属性。

eg:

```python
class Person:
    count = 0; #类属性，记录定义的人数
    
    def __init__(self, _name):
        self.name = _name; #实例属性
        Person.count += 1; #每初始化一个Person的实例对象类属性count就加一
```



#### 实例方法和类方法

- 实例方法：即具体对象的方法，在类内使用一般方式定义；

- 类方法：某个类的方法，需要修饰器 @classmethod 来标识；

  ```python
  @classmethod
  def fun(cls, var, ...):
      #类方法，可以用cls访问类的类属性，也可以调用其他的类方法
  ```



#### 静态方法

- 在开发时，如果在一个类内需要一个方法，这个方法：

  - 既不需要访问实例属性或者调用实例方法；
  - 也不需要访问类属性或者调用类方法。

  此时，我们可以将该方法封装成一个静态方法。

- 语法：

  ```python
  @staticmethod
  def fun():
      #静态方法
  ```

  > 静态方法的一般调用方式：
  >
  > **类名.方法**



#### new方法

- 使用 类名（）的方式创建对象时，Python 的解释器首先会调用内置的new方法为对象分配空间，其作用有：

  - 在内存中为对象分配空间
  - 返回对象的引用

- 重写 new 方法：

  ```python
  class NameClass(object):
      
      def __new__(cls, *args, **kwargs):
      #创建方法时，new方法会被自动调用
      #执行代码
      
      return super().__new__(cls);
  ```

- 单例设计模式的 new 方法实现：

  > 定义一个类属性 instance ，初始值为None，重写 new 方法：

  <center>
  <img src="https://typora-1313035735.cos.ap-nanjing.myqcloud.com/img/image-20220726112733364.png" alt="image-20220726112733364" style="zoom:67%;" />
      <br>
      单例模式__new__方法逻辑图
  </center>
  
  
  ```python
  class NameClass:
      
      #定义类属性记录单例对象引用
      instance = None;
      
      def __new__(cls, *args, **kwargs):
          
          if cls.instance == None:
              cls.instance = super().__new__(cls);
          
          return cls.instance;
  ```



### 对象

- 对象的创建：

  ```python
  obj = NameClass(); #无参构造
  obj = NameClass(var_1, var_2, ...); #有参构造
  ```

  > 对象的创建依然是引用，但是同种创建方式创建的多个对象依然会分配相应多份内存

  ```python
  class test:
      def func(self):
          pass;
  
  obj_1 = test();
  obj_2 = test();
  print(id(obj_1), ' ', id(obj_2));
  ```

  > out:
  >
  > 2974684409104   2974684409056

- Python 可以直接在类外给对象添加属性；

  eg:

  ```python
  obj.name = "clara"; #直接给obj添加了一个name的属性
  ```


### 继承

#### 单继承

- 语法：

  ```python
  class son(father):
      #子类会继承父类的属性和方法
  ```

  > 也称 son 类称为 father 类的派生类，father 类为 son 类的基类

- 继承时方法的重写：

  > 当父类的方法不能满足子类的需求时，可以对其方法进行**重写（override）**；
  >
  > 若子类方法与父类方法同名，则会覆盖父类方法。

  eg:

  ```python
  class father:
      def fun(self, var, ...):
          #父类的方法
      
  class son(father):
      def fun(self, var, ...):
          #子类的fun方法会覆盖父类的fun方法
  ```

  > 若要调用父类的方法，则采用 super 类实现：

  ```python
  obj = son();
  obj.fun(); #调用子类的fun方法
  super().fun(); #子类内调用父类的fun方法
  ```




#### 多继承

- 语法：

  ```python
  class son(father_1, father_2, ...):
      #子类继承多个父类的属性与方法
  ```

  > 注意事项：
  >
  > 若父类之间存在同名的属性或方法，应该尽量避免使用多继承。 



### 多态

- 不同的子类对象调用相同的父类方法，产生不同的结果，称为多态；

- 原理：子类对父类方法的重写；

  ```python
  class father(object):
      
      def fun(self, var, ...):
          #父类的fun方法
  
  class son(father):
      
      def fun(self, var, ...):
          #对父类方法重写
  ```

  

## 异常



### 异常的概念

- 程序在运行时，如果 Python 解释器遇到一个错误，会停止程序的执行，并提示一些错误信息，这就是**异常**；
- 程序停止执行并且提示错误信息这个动作，我们称为：**抛出（raise）异常**。



### 异常的捕获

- 在程序开发中，如果某些代码的执行不能确定是否正确，可以增加 try 来捕获异常；

- 语法格式：

  ```python
  try:
      #尝试执行的代码
  
  except:
      #出现错误的处理
  ```

- 根据错误的类型捕获异常：

  ```python
  try:
      #尝试执行的代码
      
  except error_1:
      #针对错误类型1的执行代码
      
  except (error_2, error_3):
      #针对错误类型2和类型3的执行代码
      
  except Exception as result:
      # print("未知错误 %s" % result)
      #针对未知类型的错误的执行代码
  ```

  > Python 解释器抛出异常时，最后一行错误信息的第一个单词就是错误类型

- 异常捕获的完整语法：

  ```python
  try:
      #尝试执行的代码
      
  except error_1:
      #针对错误类型1的执行代码
      
  except (error_2, error_3):
      #针对错误类型2和类型3的执行代码
      
  except Exception as result:
      # print("未知错误 %s" % result)
      #针对未知类型的错误的执行代码
      
  else:
      #没有异常的执行代码
      
  finally:
      #无论是否有异常都会执行的代码
  ```

  eg：

  ```python
  try:
      num = int(input("请输入非0整数："));
      result = 1 / num;
  
  except ValueError:
      print("请输入整数");
  
  except ZeroDivisionError:
      print("整数不能为0");
  
  except Exception as error_unknow:
      print("未知错误 %s" % error_unknow);
  
  else:
      print(result);
  
  finally:
      pass;
  ```

  

### 异常的传递

- 当函数或方法执行出现异常时，会将异常传递给调用一方；

- 如果传递到主程序，仍然没有异常处理，程序才会被终止。

  eg：

  ```python
  def demo():
      return int(input("请输入一个整数："));
  
  try:
      print(demo());
      
  except ValueError:
      print("请输入整数");
      
  except Exception as error_unknow:
      print("未知错误 %s" % error_unknow);
  ```

  

### 主动抛出异常

- 在开发时，如果满足特定业务需求时，希望主动抛出异常，可以：

  1. 创建一个 Exception 的对象；
  2. 使用 raise 关键词抛出异常对象。

  eg：

  ```python
  passwordTooShort = Exception("密码长度不够"); #创建异常对象
  
  def input_password():
      """
      提示用户输入密码
      密码长度必须 >= 8
      """
  
      pwd = input("请输入密码");
      if len(pwd) >= 8:
          return pwd;
      
      raise passwordTooShort; #抛出异常对象
  
  try:
      password = input_password();
  
  except passwordTooShort:
      print("密码长度必须 >= 8");
  
  except Exception as error_unknow:
      print("未知错误 %s" % error_unknow);
  ```




## 文件



### 操作文件的函数和方法

| 函数或方法 | 说明                           |
| ---------- | ------------------------------ |
| `open`     | 打开文件，并且返回文件操作对象 |
| `read`     | 将文件内容读取到内存           |
| `write`    | 将指定内容写入文件             |
| `close`    | 关闭文件                       |

- `open` 函数的第一个参数是要打开的文件名；

  - 如果文件存在，返回文件操作对象
  - 如果文件不存在，会抛出异常

- `read` 方法可以一次性读入并返回文件的所有内容；

- `close` 方法负责关闭文件。

  > 注意：
  >
  > 方法执行后，会把文件指针移动到文件的末尾。

  eg：

  ```python
  file = open("FILE_NAME"); #打开文件
  
  text = file.read(); #读取文件
  
  file.close(); #关闭文件
  ```

  

#### `open` 函数打开文件方式



```python
file = open("FILE_PATH", "method");
```

| 访问方式 | 说明                                                     |
| -------- | -------------------------------------------------------- |
| r        | 只读                                                     |
| w        | 只写                                                     |
| a        | 追加                                                     |
| r+       | 读写，文件存在则将文件指针指向开头，文件不存在则抛出异常 |
| w+       | 读写，文件存在则覆盖，文件不存在则新建文件               |
| a+       | 读写，文件存在则将文件指针指向文件末尾，不存在则新建文件 |



#### `readLine` 方法

- `readLine` 方法可以一次读取一行内容并且将文件指针移动到下一行，准备再次读取。

  > 如何读取大文件：

  ```python
  file = open("FILE_PATH");
  
  while True:
      
      text = file.readLine(); #一次读取一行
      
      if not text:
          break; #读取结束退出
      
      print(text, end = "");
      
  file.close(); #关闭文件
  ```



### 文件或目录的常用管理操作

- 如果要对目录或文件执行一些常规操作，需要导入 `os` 模块；

- **文件操作：**

  | 方法名   | 说明       | 试例                                 |
  | -------- | ---------- | ------------------------------------ |
  | `rename` | 重命名文件 | `os.rename("FILE_NAME", "NEW_NAME")` |
  | `remove` | 删除文件   | `os.remove("FILE_NAME")`             |

- **目录操作：**

  | 方法名       | 说明           | 示例                            |
  | ------------ | -------------- | ------------------------------- |
  | `listdir`    | 目录列表       | `os.listdir("CONTENT_NAME")`    |
  | `mkdir`      | 创建目录       | `os.mkdir("CONTENT_NAME")`      |
  | `rmdir`      | 删除目录       | `os.rmdir("CONTENT_NAME")`      |
  | `getcwd`     | 获取当前目录   | `os.getcwd`                     |
  | `chdir`      | 修改工作目录   | `os.chdir("CONTENT_NAME")`      |
  | `path.isdir` | 判断是否是文件 | `os.path.isdir("CONTENT_PATH")` |

  
