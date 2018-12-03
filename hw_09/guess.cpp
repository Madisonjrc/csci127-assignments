#include <iostream>
#include <stdlib.h>

int main(){
  int x;
  int guess = 50;
  int high = 100;
  int low = 0;
  int max = 100;
  int result;
  int range;
  bool loop = 1;

  std::cout << "Enter a number between 0-99 then enter -1 if the number is lower than the guess or 1 if the number is higher and 0 if the number is correct: ";
  std::cin >> x;

  while(loop == 1){
    guess = rand() % max + low;
    std::cout << guess << " :Is this the value?: ";
    std::cin >> result;
    if(result == 0){
      loop = 0;
      }
    else if(result == 1){
      low = guess + 1;

      }
    else if(result == -1){
      high = guess;
      }
    max = high - low;
  }  
  std::cout << "Your number is " << guess << std::endl;
  return 0;
} 

