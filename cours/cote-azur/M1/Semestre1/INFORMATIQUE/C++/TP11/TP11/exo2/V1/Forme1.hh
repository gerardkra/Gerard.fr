#ifndef __FORME_HH__
#define __FORME_HH__
#include<string>
using namespace std;
#include "Rot.hh"

class Forme{
protected:
  Point2D _centre;
public:
  Forme(const Point2D&);
  void apply_rot(const Rot &) ;
  virtual string to_str() const;
};
#endif
