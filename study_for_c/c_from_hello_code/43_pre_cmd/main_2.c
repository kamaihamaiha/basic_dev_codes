#include <stdio.h>

#define FMT(state, city) "The value of " #state #city " is %d\n"
#define VARNAME(state, city) state ## city
int main(){

  int ChinaBeijing = 1;
  int ChinaShanghai = 2;
  int BritishLondon = 100;
  int BritishBeijing = 100;

  printf(FMT(China, Beijing), VARNAME(China, Beijing));
  printf(FMT(British, London), VARNAME(British, London));
  return 0;
}