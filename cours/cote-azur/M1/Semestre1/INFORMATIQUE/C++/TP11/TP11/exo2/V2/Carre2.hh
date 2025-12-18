#ifndef __CARRE_HH__
#define __CARRE_HH__
#include "Forme2.hh"
#include "Point2D.hh"

class Carre: public Forme{
private:
  Point2D _centre;
  double _longueur;
  Point2D _pts[4];
public:
  Carre(Point2D, double);
  void apply_rot(const Rot& r);
  string to_str() const ;
  void set_sommets();
};
#endif
