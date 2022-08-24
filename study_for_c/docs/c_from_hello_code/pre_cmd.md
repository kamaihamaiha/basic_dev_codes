## 预处理指令

[代码](../../c_from_hello_code/43_pre_cmd/main.c)

- [一个例子](#例子要求)
- [预处理指令说明](#预处理指令说明)
- [格式](#格式)
- [带参数的`#define`](#宏函数)
- [取消宏定义](#取消宏定义)

### 例子要求

一个商品单价 3元，求买一件商品、买两件商品、买三件商品分别需要多少钱？

---
### 预处理指令说明
- 源代码中以 `#` 开头的，如 `#define` 并不是 C语言中的语句，而是**预处理指令**。
- 在代码编译前，预处理器会先处理预处理指令
    - 并根据预处理指令的意义修改 C语言的源代码
    - 修改后的代码另存为中间文件或者直接输入到**编译器**
- 代码当作文本替换    
    
### 格式
- `#define 宏 替换体`
- 宏：命名规则需要遵循标识符命名规则
- 替换体：不仅限于值，形式丰富。替换后，代码需要能够正常编译

**比如：**

- 替换前
    ```c
    #define PRICE 3
    
    ...
    total = num * PRICE;
    ...
    ```
- 替换后
    ```c
     ...
     total = num * 3;
     ...
    ```
  
### 宏函数
带参数的`#define`

- [一般用法](#一般用法)
- [宏函数建议](#宏函数建议)
- [宏函数内两个有用的运算符](#宏函数内两个有用的运算符)

#### 一般用法
`#define 宏(参数1, 参数2, ..., 参数n) 替换体`

**替换前：** 
```c
#define MEAN(a, b) (a + b)/2

int ret;
ret = MEAN(2, 4);
```

**替换后：**
```c
#define MEAN(a, b) (a + b)/2

int ret;
ret = (2 + 4)/2;
```

#### 宏函数建议

- 参数应当作为一个整体，优先运算
- 宏函数展开后的表达式应当作为一个整体
- 如果替换体内多次使用同一个参数，不要用自增、自减表达式

因此宏函数：`#define SQUARE(x) x*x` 改写成：`#define SQUARE(x) ((x)*(x))`

#### 宏函数内两个有用的运算符

[代码](../../c_from_hello_code/43_pre_cmd/main_2.c)

- [一个`#`](#一个井号)
- [两个`#`](#两个井号)
  

##### 一个井号
- 替换体：加`#`
  ```c
   #define test(s) #s
   
   // 替换后为
   test("s")
  
  ```
- 举例：
  ```c
  #define HELLO(love) "I " love " You"
  #define HELLO2(love) "I " #love " You"
  
  // 结果分别为
  I love You
  I "love" You
  ```

##### 两个井号

*不加井号*
  ```c
  #define LOCATION(country, city) country city
  
  LOCATION(China HK);
  
  // 展开的结果为
  China HK;
  ```

*加井号*
  ```c
  #define LOCATION(country, city) country ## city
  
  LOCATION(China HK);
  
  // 展开的结果为
  ChinaHK;
  ```

### 取消宏定义

`#undef`
```c
#define NUM
#undef NUM
```