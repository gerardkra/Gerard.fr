// g++ main2.cpp Rot.cpp Mat22.cpp Point2D.cpp Carre2.cpp Cercle2.cpp -o main2
#include "Carre2.hh"
#include "Cercle2.hh"
#include "Rot.hh"
#include<cmath>

int main()
{
  Rot r(M_PI/4);
  Carre c(Point2D(0,0), 2);
  cout << c.to_str() << endl;
  c.apply_rot(r);
  cout << c.to_str() << endl;
  Cercle cl(Point2D(-1,2), 3);
  cout << cl.to_str() << endl;
  cl.apply_rot(r);
  cout << cl.to_str() << endl;
  Forme* v[2];
  v[0] = &c;
  v[1] = &cl;
  for(int i=0;i<2;i++)
    cout << v[i]->to_str() << endl;
  return 0;
}
