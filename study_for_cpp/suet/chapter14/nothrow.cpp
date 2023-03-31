#include <iostream>

using namespace std;

int main(){

    size_t len = 90000000000L;
    int *p = NULL;

    try {
        cout << "Trying to allocate a big block of memory" << endl;
        p = new int[len];
        cout << "No Exception." << endl;
    } catch (std::bad_alloc & ba) {
        cout << "bad_alloc exception: " << ba.what() << endl;
    }

    if (p) {
        delete []p;
    } else {
        cout << "So bad, null pointer." << endl;
    }

    return 0;
}