#include <iostream>

using namespace std;

int main()
{
 int a = 1;
 double b = 3.14;

 cout << sizeof(a) << ": " << a << endl;
 cout << sizeof(b) << ": " << b << endl;
 cout << sizeof(a+b) << ": " << a+b << endl;
 return 0;
}
