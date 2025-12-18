#ifndef __CERCLE_HH__
#define __CERCLE_HH__
#include "Forme2.hh"
#include "Point2D.hh"

class Cercle: public Forme{
private:
  double _rayon;
public:
  Cercle(const Point2D&, double);
  void apply_rot(const Rot& r);
  string to_str() const;
};
#endif
