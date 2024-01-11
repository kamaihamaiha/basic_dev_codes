### 第二章

1. 程序调试方法

#### 程序调试方法

**LLDB**
1. 查看汇编代码：Debug 窗口 -> LLDB 窗口 -> 输入：disassemble -> 回车
2. 设置汇编代码是 intel 平台的：
    - 临时设置：settings set target.x86-disassembly-flavor intel
    - 永久生效：在用户目录下创建 <font color="red">.lldbinit</font>,把上面的指令写进去。
      - MacOS: `/Users/<UserName>`
      - Linux: `/Home/<UserName>`
      - Windows: `C:\Users\<UserName>`
   
#### 扩展

- 小端序(Little Endian): 高位数存于高地址
- 大端序(Big Endian): 高位数存于低地址
