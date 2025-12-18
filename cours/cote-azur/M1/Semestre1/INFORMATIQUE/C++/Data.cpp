#include <cstdlib>
#include "Data.hh"

using namespace std;


Data::Data(int n)
{
    _n = n;
    _x1 = new double[n];
    _x2 = new double[n];
    _y = new double[n];
}

Data::~Data()
{
    delete[] _x1;
    delete[] _x2;
    delete[] _y;
}

double *Data::getX(int i)
{
    double *res = new double[3];
    res[0] = 1;
    res[1]= _x1[i];
    res[2] = _x2[i];
    return res;
}

double Data::getY(int i)
{
    return _y[i];
}

int Data::getN()
{
    return _n;
}

void Data::setX1(double *x1)
{
    for (int i = 0; i < _n; i++)
        _x1[i] = x1[i];
}


void Data::setX2(double *x2)
{
    for (int i = 0; i < _n; i++)
        _x2[i] = x2[i];
}

void Data::setY(double *y)
{
    for (int i = 0; i < _n; i++)
        _y[i] = y[i];
}
