#include "Forme1.hh"

Forme::Forme(const Point2D &p): _centre(p) {}

string Forme::to_str() const{
  return "Forme géométrique de centre (" + to_string(_centre.x) + ", " + to_string(_centre.y) + ")";
}

void Forme::apply_rot(const Rot& r) {
  _centre = r(_centre);
}
