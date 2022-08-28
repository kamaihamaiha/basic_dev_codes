## 文件

[代码](../../c_from_hello_code/49_file/main.c)

- [创建并打开文件](#创建并打开文件)
  - `fopen()`
- [输出字符串到文件]()
    - `fprintf()`
- 关闭文件
    - `fclose()`
- [文本模式与二进制模式](#文本模式与二进制模式)    
    - "wb"
    - "rb"
    - "a": 追加模式
- 读取文件函数
    - `fscanf()`
- 获取一个字符
    - `fgetc()`
    - 调用后，指针会移动到下一个字符位置，重复调用会逐个字符读取
- 获取一行字符
    - `fgets()`
    - 调用后，指针会移动到下一行字符位置，重复调用会逐行读取
- 写入一个字符
    - `fputc()`
- `EOF`: End Of File
  - stdio.h 定义的一个宏
- 判断文件是否结束
    - `feof()`
- 判断文件是否错误
    - `ferror()`
- 从文件中读取字符串函数
    - `fgets()`
- [文件缓存](#文件缓存)  
- [文件偏移](#文件偏移)  
- 获取当前文件指针位置  
  - `ftell()`
- 将文件指针回到文件最开始
  - `rewind()`
- [更新文件](#更新文件)  
- [将数值以二进制的形式保存](#将数值以二进制的形式保存)
  - `fwrite()`
- [读取文件中的二进制数据](#读取文件中的二进制数据)
  - `fread()`

### 创建并打开文件

#### 库函数

- `FILE *fopen(const char * filename, const char * mode);`
    - `filename`: 文件路径，相对路径或绝对路径
    - `mode`: 操作模式
      - w: 写模式
        - 如果文件不存在，则创建一个文件；如果文件存在，则清空文件内容
      - r: 读模式
    - 如果操作成功，返回 `FILE` 类型的数据（记录文件信息的结构）
    
##### 举例：

```c
// 在当前目录下，创建名为 data.txt 的文件
fopen("data.txt", "w");
```

### 文本模式与二进制模式

#### 文本模式

对文件输入输出的数据当作一行行的文本来处理。换行时，会根据系统自动将 换行符替换成 \r \n

#### 二进制模式

- `fopen("data.txt", "wb");`
- `fopen("data.txt", "rb");`

### 文件缓存

文件操作函数，是有文件缓存的。要刷新缓存后，才会真正将数据更新到文件。

#### 刷新缓存
- 当调用 `fclose()` 
-  程序结束时
- 主动调用 `fflush()`

#### 文件偏移

- `fseek(FILE * stream, long offset, int origin)`: 用于移动文件指针
  - offset: 文件指针偏移量
  - origin: 从什么位置开始偏移
    - SEEK_SET: 文件开头
    - SEEK_CUR: 当前文件位置
    - SEEK_END: 文件结尾
  
### 更新文件

比如要把文件中的大写字母 `H` 改为小写字母 `h`，那么文件要可读可写。

- 文件模式：
  - 'w+': 更新模式，可读可写。但是，会清空文件原有内容
  - 'r+': 更新模式，可读可写。
  
#### 读写操作转化

- 写 => 读: 必须调用 `ffush`、`fseek`、`rewind` 中的一个
- 读 => 写: 必须调用 `fseek`、`rewind` 中的一个

### 将数值以二进制的形式保存

- `fwrite()`
  - `size_t fwrite(const void *buffer, size_t size, size_t count, FILE *stream);`
  - `*buffer`: 待写入文件首地址
  - `size`: 每一块数据大小
  - `count`: 一共有多少块数据
  - 返回值: 成功写入了多少块数据
  
### 读取文件中的二进制数据

- `size_t fread(void *buffer, size_t size, size_t count, FILE *stream);`

