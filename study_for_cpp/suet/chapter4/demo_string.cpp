#include <iostream>
#include <cstring>

using namespace std;

int main(){

    // Array-style string

    char rabbit[10] = {'P', 'e', 't', 'e', 'r'};
    char bad_pig[10] = {'p', 'e', 'p', 'p', 'a' ,' ', 'p', 'i', 'g', '\0'};
    char bad_pig2[10] = {'p', 'e', 'p', 'p', 'a' ,' ', 'p', 'i', 'g', 0};

    cout << "rabbit length: " << strlen(rabbit) << endl;
//    cout << "bad_pig length: " << strlen(bad_pig) << endl;
//    cout << "bad_pig2 length: " << strlen(bad_pig2) << endl;

    for(int i = 0; i < ::strlen(rabbit); i++) {
        cout << i << ":" << + rabbit[i] << "(" << rabbit[i] << ")" << endl;
    }

    cout << "rabbit is: " << rabbit  << endl;

    // string literals
    char name1[] = "Southern University of Science and Technology";
    char name2[] = "Southern University of "     " Science and Technology";
    char name3[] = "ABCD";

    // 其他字符类型
    const wchar_t s5[] = L"abce";
    const char16_t s9[] = u"abcd";
//    const char32_t s6[] = U"abce";

    // 字符串操作
    char str1[] = "Hello, \0Cpp";
    char str2[] = "World!";
    char res[128];

    strncpy(res, str1, 6);
    strcat(res, str2);

    cout << "res: " << res << endl;

    std::string str1_c = "Hello";
    std::string str2_c = "World";
    std::string res_c = str1_c + ", " + str2_c;
    cout << "res: " << res_c << endl;

    return 0;
}