#include <iostream>
using namespace std;
int main()
{
  int a = 0;

  while (a < 10)
    {
      cout << a << endl;
      a = a + 1;
    }

  do
    {
      cout << a << endl;
      a = a - 1;
    }
  while (a > 0);

  return 0;
}
