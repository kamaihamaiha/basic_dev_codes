#include <iostream>

using namespace std;

#define PRINT_ARRAY(array, n) \
for(int index = 0; index < (n); index++) { \
      cout << "array[" << index << "] = " << (array)[index] << endl; \
}


int main(){

    int nums[4] = {0, 1, 2, 3};
    int *p = nums + 1; // point to the element with value 1

    PRINT_ARRAY(nums, 4)

    *p = 10; // change 1-index element value to 10
    cout << endl;
    PRINT_ARRAY(nums, 4)
    p++; // point to the element with value 2

    // p 应该相比于 nums 地址偏移了 8bit( 2 个 int)
    cout << "nums: " << nums << endl;
    cout << "p: " << p << endl;

    *p = 20; // change 2-index element value to 20
    *(p - 1) = 1000; // change 1-index element to 1000
    p[1] = 300; // change 3-index element to 300

    PRINT_ARRAY(nums, 4)

    return 0;
}