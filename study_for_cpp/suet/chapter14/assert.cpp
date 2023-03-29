#include <iostream>
//#define NDEBUG
#include <cassert>

int main(int argc, char ** argv){

    assert(argc == 2); // 要求程序输入 2 个参数，否则程序终止
    std::cout << "This is an assert example." << std::endl;

    return 0;
}