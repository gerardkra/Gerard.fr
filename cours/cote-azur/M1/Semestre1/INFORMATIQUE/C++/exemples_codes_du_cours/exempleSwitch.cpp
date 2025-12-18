#include <iostream>
using namespace std;

int main()
{
  unsigned int a;
  cout << "Valeur de a ?" << endl;
  cin >> a;
  switch (a)
    {
    case 0 :
      cout << "a est nul" << endl;
      break;
    case 1 :
      cout << "a vaut 1" << endl;
      break;
    default:
      cout << "a est > 1" << endl;
      break;
    }
  return 0;
}
