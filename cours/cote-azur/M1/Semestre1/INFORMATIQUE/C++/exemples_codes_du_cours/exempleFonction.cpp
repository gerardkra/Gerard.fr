#include <iostream>
using namespace std;

double my_pow(double a, unsigned int expo)
{
  double res = 1;

  for(unsigned int i=0; i<expo; i++)
    res *= a;
  return res;
}

int main()
{
  cout << "2^5 = " << my_pow(2.0,5) << endl;
  return 0;
}
