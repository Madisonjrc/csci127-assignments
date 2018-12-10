#include <iostream>
#include <math.h>

int discriminant(int a, int b, int c){
  int result;
  result = (b*b) - 4*(a*c);
  return result;
}

double quadsolve(int a, int b, int c){
  double d;
  d = discriminant(a,b,c);
  if(d>=0){
    return (-b+sqrt(d))/(2*a);
  }
  else{
    return 0;
  }
}

int main(){
  std::cout << "discriminant(1,2,3)" <<  discriminant(1,2,3) << std::endl;
  std::cout << "discriminant(6,5,-1)" << discriminant(6,5,-1) << std::endl;
  std::cout << "discriminant(1,3,-10" << discriminant(1,3,-10) << std::endl;
  std::cout << quadsolve(1,2,3) << std::endl;
  std::cout << quadsolve(6,5,-1) << std::endl;
  std::cout << quadsolve(1,3,-1) << std::endl;
  return 0;
}
