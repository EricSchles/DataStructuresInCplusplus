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
