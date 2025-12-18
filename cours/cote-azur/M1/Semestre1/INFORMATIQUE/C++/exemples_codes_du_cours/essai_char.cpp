#include<iostream>
using namespace::std;

int main(void)
{
  char w = 'a';      // w <-> 97 et 'a'
  cout << w << endl; // ça affiche 'a'!
  cout << w+2 << " "
       << 'a' + 1 << endl; // affiche 99 et 98!
  char z = 'a' + 1; 
  cout << z << endl; // ça affiche 'b'!
  return 0;
}
