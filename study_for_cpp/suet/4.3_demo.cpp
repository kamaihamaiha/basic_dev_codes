#include <iostream>

enum dataType {
    TYPE_INT8 = 1,
    TYPE_INT16 = 2,
    TYPE_INT32 = 4,
    TYPE_INT64 = 8
};

struct Point {
    enum dataType type;
    union {
        std::int8_t data8[3];
        std::int16_t data16[3];
        std::int32_t data32[3];
        std::int64_t data64[3];
    };
};

size_t dataWidth(struct Point pt){
    return size_t(pt.type) * 3;
}

int main(){


    return 0;
}