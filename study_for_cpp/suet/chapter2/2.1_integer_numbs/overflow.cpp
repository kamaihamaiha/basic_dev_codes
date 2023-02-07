#include <iostream>

using namespace std;

int main(){

    int num1 = 56789;
    int num2 = num1;

    cout << "num1 = " << num1 << endl;
    cout << "num2 = " << num2 << endl;

    unsigned int ret = num1 * num2;
    cout << "num1 * num2 = " << ret << endl;
    return 0;
}