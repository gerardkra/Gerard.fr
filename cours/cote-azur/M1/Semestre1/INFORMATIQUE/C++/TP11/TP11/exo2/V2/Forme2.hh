#ifndef __FORME_HH__
#define __FORME_HH__
#include<string>
using namespace std;
#include "Rot.hh"

class Forme{
protected:
  Point2D _centre;
public:
  virtual void apply_rot(const Rot &)  = 0;
  virtual string to_str() const = 0;
};
#endif
