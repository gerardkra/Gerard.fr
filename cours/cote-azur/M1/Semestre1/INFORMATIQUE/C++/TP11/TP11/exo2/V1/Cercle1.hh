#ifndef __CERCLE_HH__
#define __CERCLE_HH__
#include "Forme1.hh"
#include "Point2D.hh"

class Cercle: public Forme{
private:
  double _rayon;
public:
  Cercle(const Point2D&, double);
   string to_str() const;
};
#endif
