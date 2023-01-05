//
// Created by kk on 2023/1/5.
//
#include <stdio.h>
#include <string.h>

//定义各种异常的宏

#define COPY_SUCCESS 0
#define COPY_ILLEGAL_ARGUMENTS -1
#define COPY_SRC_OPEN_ERROR -2
#define COPY_SRC_READ_ERROR -3
#define COPY_DEST_OPEN_ERROR -4
#define COPY_DEST_WRITE_ERROR -5
#define COPY_UNKNOWN_ERROR -100

void getFileName(char *src, const char* article_id, int index);
int CopyFile(char const *src, char const *dest);

int main(){

    int ret = 0;
    FILE *f_src = NULL;
    FILE *f_des = NULL;
    char *file_src_path = "audio/article_0.aac";
    char file_des_path[256] = { 0 };

    const char* articleID = "7be17688-1ae2-11e8-b7f2-000c29ffef9b";

    for (int i = 0; i < 100; ++i){
        getFileName(file_des_path, articleID,i);
        ret = CopyFile(file_src_path, file_des_path);

        printf("copy result: %d\n", ret);
        char tips[256] = { 0 };
        strcpy(tips, "file: ");
        strcat(tips, file_des_path);
        strcat(tips, ret == 0 ? "copy success!" : " copy failed!");

        puts(tips);
    }

    return 0;
}

void getFileName(char *des, const char* article_id, int index) {
    strcpy(des, "audio/");
    strcat(des, article_id);
    strcat(des, "_");
    char str_index[256] = {0};
    sprintf(str_index, "%d", index);
    strcat(str_index, ".aac");
    strcat(des, str_index);
}

/**
 * 复制文件
 * @param src 被复制的文件
 * @param dest 新的文件副本
 * @return 成功返回 0，失败返回自定义的错误码
 */
int CopyFile(char const *src, char const *dest) {
    if (!src || !dest) {
        return COPY_ILLEGAL_ARGUMENTS;
    }

    FILE *src_file = fopen(src, "r");
    if (!src_file) { //打开被复制的文件失败
        return COPY_SRC_OPEN_ERROR;
    }

    FILE *dest_file = fopen(dest, "w");
    if (!dest_file) { //打开目标文件失败
        fclose(src_file); //并且要关闭 src file
        return COPY_DEST_OPEN_ERROR;
    }

    int result;

    while (1) {
        int next = fgetc(src_file);
        if (next == EOF) { // 以下细分了三种情况
            if (ferror(src_file)) {
                result = COPY_SRC_READ_ERROR;
            } else if (feof(src_file)) {
                result = COPY_SUCCESS;
            } else {
                result = COPY_UNKNOWN_ERROR;
            }
            break;
        }

        // 往 dest_file 文件写入数据
        if (fputc(next, dest_file) == EOF) {
            result = COPY_DEST_WRITE_ERROR;
            break;
        }
    }

    //关闭文件
    fclose(src_file);
    fclose(dest_file);

    return result;

}
