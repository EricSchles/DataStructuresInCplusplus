#include <iostream>
using namespace std;

//A generic swapping function
//This is the beauty of good code.

template<class genType>
void swap( const genType & e11, const genType & e12)
{
  genType tmp = e11; e11 = e12; e12 = tmp;
}

//As a general note, the author does not like using 'const'
//perhaps it was not part of the standard?
//if you receieve any errors, just put const infront of the variable and run again.
//it is likely this will solve any/all issues

int main()
{

  int x = 6;
  int y = 7;
  
  swap(x,y);

  cout << endl << x << ' ' << y << endl;
  //should be 7 6

  return 0;
}
