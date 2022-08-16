## 字符串与字符指针

[代码](../section_9/main.c)

- 字符串常量不可修改

### 字符串初始化

```c
char str1[5] = {'h', 'e', 'l', 'l', 'o'}; // ❌
char str2[5] = "Hello"; // ❌
char str3[] = {'h', 'e', 'l', 'l', 'o'};; // ❌
```