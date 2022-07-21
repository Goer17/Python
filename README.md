# Personal Note For Python
# Python Part A



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

     对于ipython解释器则是直接输入exit：

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

  



## 函数



### 函数语法

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



### Python中的其他一些函数

#### Python中的随机数

- 导入随机数的模块：

```python
import random;
```



- 部分函数介绍：

```python
random.randint(a,b); #生成随机整数n并返回 (a <= n <= b)
```



#### print() 函数

- 在默认情况下，print() 函数在输出内容后会自动在末尾增加换行；

- 如果不希望末尾自动换行，可以在print() 函数的输出内容后增加：end = ""；

  ```python
  print("Hello world", end = "");
  ```






# Python Part B

