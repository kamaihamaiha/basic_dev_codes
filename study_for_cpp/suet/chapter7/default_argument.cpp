#include <iostream>
#include <cmath>

using namespace std;

float norm(float x, float y, float z);
float norm(float x, float y, float z = 0);
float norm(float x, float y = 0, float z);

int main(){

    cout << norm(3.0) << endl;
    cout << norm(3.0, 4.0) << endl;
    cout << norm(3.0, 4.0, 5.0) << endl;
    return 0;
}

float norm(float x, float y, float z){
    return sqrt(x * x + y * y + z * z);
}