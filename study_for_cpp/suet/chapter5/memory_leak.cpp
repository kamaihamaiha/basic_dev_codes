#include <iostream>

using namespace std;
void foo(){
    int *p = (int*) malloc(4 *sizeof(int));
    return; // 每次调用就会造成新的 16bit 的内存泄漏
}
int main(){
    int *p = (int*) malloc(4 * sizeof(int ));
    p = (int*) malloc(8 * sizeof(int));

    free(p);
    // the first memory will not be freed

    // 申请 1TB 内存，看看会崩吗
    for (int i = 0; i < 1024; ++i){
        p = (int*) malloc(1024 * 1024 * 1024);
    }
    cout << "程序没有崩!" << endl;
    return 0;
}