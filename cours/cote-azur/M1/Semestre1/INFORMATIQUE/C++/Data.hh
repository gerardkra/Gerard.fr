#ifndef __DATA_HH__
#define __DATA_HH__

class Data 
{
    private:
        double* _x1;
        double* _x2;
        double* _y;
        int _n;

    public:
        /*
            Constructeur de la class Data
            l'entier n correspond au nombre de jeu de données
            contenues
        */
        Data(int n);
        
        ~Data();

        /*  renvoie un tableau de double correspondant au jeu de données
        indexé par i
        */
        double* getX(int i);

        /*
            renvoie la classe (1 ou -1) de la i-ème donnée
        */
        double getY(int i);   

        /*
            accesseur de la variable _n
        */
        int getN(); 

        /*
            mutateurs 
        */
        void setX1(double *x1);
        void setX2(double *x2);
        void setY(double *y);
        
};

#endif
