#include <iostream>
using namespace std;

unsigned int mySum(unsigned int N)
{
  unsigned int resu = 0;

  for(unsigned int i=0; i<N+1; i++)
    resu += i;
  return resu;
}

int main()
{
  cout << "Somme jusqu'à 5 inclus = "
       << mySum(5) << endl;
  return 0;
}
