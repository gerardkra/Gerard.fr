// g++ main1.cpp Rot.cpp Mat22.cpp Point2D.cpp Forme1.cpp Cercle1.cpp -o main1
#include "Forme1.hh"
#include "Cercle1.hh"
#include "Rot.hh"
#include<cmath>

int main()
{
  Rot r(M_PI/4);
  Forme f(Point2D(4,3));
  cout << f.to_str() << endl;
  f.apply_rot(r);
  cout << f.to_str() << endl;
  Cercle cl(Point2D(-1,2), 3);
  cout << cl.to_str() << endl;
  cl.apply_rot(r);
  cout << cl.to_str() << endl;  
  Forme* v[2];
  v[0] = &f;
  v[1] = &cl;
  for(int i=0;i<2;i++)
    cout << v[i]->to_str() << endl;
  return 0;
}
