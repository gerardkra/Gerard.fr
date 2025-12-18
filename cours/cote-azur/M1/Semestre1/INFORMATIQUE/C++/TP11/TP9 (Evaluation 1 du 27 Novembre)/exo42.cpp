#include<iostream>
using namespace std;


int myMax(int* a, int n){  // n>=2
  int tmp ;
  tmp = a[0];
  for(int i=1;i<n;i++)
    tmp = (tmp<a[i]) ?  a[i]: tmp;
  return tmp;
}

double myMax(double* a, int n){  // n>=2
  double tmp ;
  tmp = a[0];
  for(int i=1;i<n;i++)
    tmp = (tmp<a[i]) ?  a[i]: tmp;
  return tmp;
}

void affiche(double* t, int n)
{
  for(int i=0;i<n-1;i++)
    cout << t[i] <<  " ";
  cout << t[n-1] << endl;
}

void affiche(int* t, int n)
{
  for(int i=0;i<n-1;i++)
    cout << t[i] <<  " ";
  cout << t[n-1] << endl;
}

int main() {
  double t0[4] = {-5.6, -6.6, 4.1, 1.3};
  int t1[6] = {6, -5, 5, 12, 1, 13};
  cout << "Affichage de t0" << endl;
  affiche(t0,4);
  cout << myMax(t0, 4) << endl;
  cout << "Affichage de t1" << endl;
  affiche(t1,6);
  cout << myMax(t1, 6) << endl;
}
