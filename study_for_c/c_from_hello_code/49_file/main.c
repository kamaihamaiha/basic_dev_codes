#include <stdio.h>
#include <stdlib.h>

void writeFile();
void writeFile2();
void readFile();
void updateFile();
void writeArrayToFile();
void writeArrayToFileWithBinary();
void readArrayToFileWithBinary();

void readValueFormFile();

int main(){

//  writeFile();
//  writeFile2();
//  readFile();

//  updateFile();

//  writeArrayToFile();

  writeArrayToFileWithBinary();

  readArrayToFileWithBinary();

//  readValueFormFile();
  return 0;
}

void writeFile() {
  // 创建并打开文件
  FILE *pFile = fopen("data.txt", "w");
  if (pFile == NULL) {
    return;
  }

  // 输出字符串到文件
  fprintf(pFile, "%s\n", "Hello!");

  // 使用完后，关闭文件
  fclose(pFile);

}

/**
 * 用到 fputc() 函数
 *
 */
void writeFile2() {
  // 创建并打开文件
  FILE *pFile = fopen("data.txt", "a"); // a: append 追加模式
  if (pFile == NULL) {
    return;
  }

  char str[] = "HelloWorld\n";
  char *p = str;
  while (*p != '\0') {
    fputc(*p, pFile);
    p++;
  }

  fclose(pFile);
}

/**
 * 用到 fgets() 函数
 */
void readFile(){

  FILE *pFile = fopen("main.c", "r");
  if (pFile == NULL) return;

  char buffer[100];
  while (fgets(buffer, 100, pFile) != NULL) {
    printf("%s", buffer);
  }

  fclose(pFile);
}

void updateFile() {
  FILE *pFile = fopen("data.txt", "r+");
  if (pFile == NULL) return;

  char ch;
  while (1) {
    ch = fgetc(pFile);
    if (ch == EOF) {
      // 文件结束
      printf("file is end\n");
      break;
    }

    if (ch == 'H') {
      fseek(pFile, -1, SEEK_CUR); // 把文件指针向前移动一个字节，再进行修改
      ch = fputc('h', pFile);
      if (ch == EOF) {
        printf("file is end\n");
        break;
      }
    }
  }
}

void writeArrayToFile() {
  int arr[] = {1, 2, 3, 4, 5, 6, 7};

  FILE *pFile = fopen("data.txt", "r+");
  if (pFile == NULL) return;

  for (int i = 0; i < 7; ++i) {
    fprintf(pFile, "%d\n", arr[i]);
  }
  fclose(pFile);
};

void writeArrayToFileWithBinary(){
  int arr[] = {1, 2, 3, 4, 5, 6, 7};

  FILE *pFile = fopen("data.txt", "w");
  if (pFile == NULL) return;
  int ret = fwrite(arr, sizeof(arr), 1, pFile);
  if (ret == 1) {
    printf("write binary data succeed!\n");
  }
  fclose(pFile);
}

void readArrayToFileWithBinary() {
  FILE *pFile = fopen("data.txt", "r");
  if (pFile == NULL) return;
  int nums[7] = {0};
  int ret = fread(nums, sizeof(nums), 1, pFile);
  if (ret == 1) {
    printf("read binary data succeed!\n");
  }
  for (int i = 0; i < 7; ++i) {
    printf("%d\n", nums[i]);
  }

  fclose(pFile);
}

// 读取文件中的字符，转化为 int 类型保存到数组
void readValueFormFile() {
  FILE *pFile = fopen("data.txt", "r");
  if (pFile == NULL) return;
  int nums[7] = {0};
  for (int i = 0; i < 7; ++i) { // 这里也可以用 while 循环，判断 fscanf() 的返回值，如果不是 EOF 则继续读取
    fscanf(pFile, "%d", &nums[i]);
  }

  // 然后打印数组的元素
  for (int i = 0; i < 7; ++i) {
    printf("%d\n", nums[i]);
  }

  fclose(pFile);
}