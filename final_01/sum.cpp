#include <iostream>

int sumofsquares(int a, int b){
  int sum;
  while(a<b){
    sum = 0;
    for(a; a<b+1; a = a+1){
      int s = a*a;
      sum = sum + s;
    }
    return sum;
  }
}

int main(){
  std::cout << sumofsquares(5,10) << std::endl;
  return 0;
}
