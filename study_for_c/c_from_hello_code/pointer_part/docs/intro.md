### 指针概念

- cpu
- 内存
- 内存总线

#### cpu

- 算数逻辑单元
- 控制单元
- 寄存器组

#### 内存

- 晶体管
- 字节：8个晶体管
- 内存地址（房间号）： 4个字节(32位程序) 或者 8个字节(64位程序)

##### 数据类型居住的房间

- char: 	1
- short: 	2
- int:		4
- long:		4
- float:	4
- long long:    8
- double:   8

**表达房间：**

房间号 + 房间数

- 房间号：首地址
- 房间数：占用存储空间大小

指针类型的值就是数据类型的首地址。