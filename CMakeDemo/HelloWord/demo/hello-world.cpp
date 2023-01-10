#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

string say_hello(){
    return string("Hello CMake!");
}

int main(int argc, char** argv){
    cout << say_hello() << endl;
    return EXIT_SUCCESS;
}


