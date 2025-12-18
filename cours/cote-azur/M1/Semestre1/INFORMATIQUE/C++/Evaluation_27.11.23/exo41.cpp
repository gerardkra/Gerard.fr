#include<iostream>
using namespace std;

double theSum(double* t, int n, bool even)
{
  double s = 0;
  if(even)
    {
      for(int i=0;i<n;i+=2)
	s += t[i];
    }
  else
    {
      for(int i=1;i<n;i+=2)
	s += t[i];
    }
  return s;
}

int main()
{
  double t[7] = {-1.1, -1.2, 2.4, 0.2, 5.6, 4.1, 1.3};
  // python -c "import numpy as np;t=[-1.1, -1.2, 2.4, 0.2, 5.6, 4.1, 1.3];print(np.sum(np.array(t)[range(0,len(t),2)]))"
  cout << theSum(t, 7, true) << " (indices pairs - on doit trouver 8.2)" << endl;
  cout << theSum(t, 7, false) << " (indices impairs - on doit trouver 3.1)" << endl;
}


