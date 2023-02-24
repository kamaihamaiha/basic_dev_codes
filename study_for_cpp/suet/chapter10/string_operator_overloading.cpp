#include <iostream>
#include <string>

using namespace std;


int main (){

    string s("Hello ");
    s += "C";
    s.operator+=(" and CPP");

    cout << s << endl;

    return 0;
}