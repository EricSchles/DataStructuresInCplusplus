/*

This example comes from chapter 1, section 2 page 3.
This class is intended to show you a way to write and instantiate
a class.
Notice the design choices: no initialization vectors,
the use of protected data, the use of char *s instead of 
the string class.
The author intends to only show you classes and nothing else new.
That is what makes this book superior to Mark Allen-Weiss' book.
 
Sadly, this code uses the old standard and therefore is not recognized by 
the current g++ compiler.
*/

#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

class C {
public:
  C(const char *s="", int i = 0, double d = 1){
    strcpy(dataMember1,s);
    dataMember2 = i;
    dataMember3 = d;
  }
  void memberFunction1(){
    cout << dataMember1 << ' ' << dataMember2 << ' '
	 << dataMember3 << endl;
  }
  void memberFunction2(int i, const char *s = "unknown"){
    dataMember2 = i;
    cout << i << " received from " << s << endl;
  }
protected:
  char dataMember1[20];
  int dataMember2;
  double dataMember3;
};

int main()
{
  C object1("object1",100,2000), object2("object2"),object3;

  return 0;
}
