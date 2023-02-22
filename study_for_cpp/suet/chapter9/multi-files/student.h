#pragma
#include <cstring>

using namespace std;

class Student{
private:
    char name[4];
    int born;
    bool male;

public:
    void setName(const char* s){
        strncpy(name, s, sizeof(name));
    }

    void setBorn(int b){
        born = b;
    }


    // only declarations, the definitions are out of the class
    void setGender(bool isMale);
    void printInfo();
};
