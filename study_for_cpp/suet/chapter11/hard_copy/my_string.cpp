#pragma
#include <iostream>
#include <cstring>

using namespace std;

class MyString{
private:
    int buf_len;
    char * characters;

public:
    MyString(int buf_len = 0, const char * data = NULL){
        cout << "Constructor(int, char*)" << endl;
        this->buf_len = 0;
        this->characters = NULL;
        create(buf_len, data);
    }

    // 自定义 copy 构造
    MyString(const MyString & ms){
        cout << "Constructor(MyString &)" << endl;
        this->buf_len = 0;
        this->characters = NULL;
        create(ms.buf_len, ms.characters);
    }

    // 自定义赋值运算符
    MyString & operator=(const MyString &ms){
        create(ms.buf_len, ms.characters);
        return *this;
    }

    ~MyString(){
        release();
    }

    bool create(int buf_len, const char* data){
        // 先释放对象原来的空间
        release();

        this->buf_len = buf_len;
        if (this-buf_len != 0) {
            this->characters = new char[this->buf_len]{};
        }
        if (data) {
            strncpy(this->characters, data, this->buf_len);
        }

        return true;
    }

    bool release(){
        this->buf_len = 0;
        if (this->characters != NULL){
            delete [] this->characters;
            this->characters = NULL;
        }
        return 0;
    }

    friend ostream & operator<<(ostream &os, const MyString& ms){
        os << "buf_len = " << ms.buf_len;
        os << ", characters = " << static_cast<void*>(ms.characters);
        os << " [" << ms.characters << "]";
        return os;
    }
};