/*
Notice the use of a declaration in the template
It's pretty nuts that you can pass in variables to templates.

 */

#include <iostream>
using namespace std;

template<class genType, int size = 50>
class genClass {
public:
  genType storage[size];
};

int main()
{

  genClass<int> intObject1;

  return 0;
}
