#include <iostream>

using namespace std;

void div2(int);

int main(){
    div2(1024);
    return 0;
}

void div2(int value){
    cout << "Entering value: " << value << endl;
    if (value > 1) {
        div2(value / 2);
    } else {
        cout << "---------------------" << endl;
    }
    cout << "Leaving value: " << value << endl;
}