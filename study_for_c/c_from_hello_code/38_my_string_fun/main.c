#include <stdio.h>
#include <string.h>

// 计算字符串的长度
size_t m_strlen(const char *str);

// 拼接字符串
char * m_strcat(char * des, const char *sour);


// test fun
void test1();

int main(){

//  test1();

  char *des = "Hello";
  char sour[] = "world";
  char *str = m_strcat(des, sour);
  puts(str);

}
void test1(){
  size_t len;
  char str[] = "HelloWorld!";
  len = m_strlen(str);
  printf("%d\n", len);

  len = m_strlen("");
  printf("%d\n", len);
  len = m_strlen(NULL);
  printf("%d\n", len);
}
size_t m_strlen(const char *str){
  if (str == NULL) return 0;
  size_t len = 0;
  while (*str != '\0') {
    len++;
    str++; // 指针前进
  }
  return len;
}

// mac osx 下运行报错：bus error。可能是编译器不允许修改字符串的值
char * m_strcat(char * des, const char *sour){
  // 先做异常校验
  if (des == NULL) return NULL;
  if (sour == NULL) return des;

  // 先把目标指针的首地址保存，用于函数返回值
  char *ret = des;

  // 目标指针 des 移动到最后
  while (*des != '\0') {
    des++;
  }

  // 开始逐一把 sour 的值追加到 des 后面
  while (*sour != '\0') {
    *des = *sour;
    des++;
    sour++;
  }
  // 标记字符串结束
//  *des = '\0';
  return ret;
}