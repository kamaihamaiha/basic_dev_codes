#include <iostream>
#include "mul.h"

using namespace std;

int main(){
    int a, b;
    int result;

    cout << "pick two integers:" << endl;

    cin >> a;
    cin >> b;

    result = mul(a, b);

    cout << "Result: " << result << endl;

    return 0;
}