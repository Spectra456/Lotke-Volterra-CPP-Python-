#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

// первый вариант
#define X_init 300
#define Y_init 150

// второй вариант
//#define X_init 150
//#define Y_init 150

// третий вариант
//#define X_init 15
//#define Y_init 22

//четвертый вариант
//#define X_init 2
//#define Y_init 2

#define H 0.01

#define Alpha 2
#define Beta 0.01
#define Gamma 1
#define Delta 0.01

#define T_start 0.0

#define T_finish 10


double fx(double x, double y) { return (Alpha * x - Beta * x * y); }


double fy(double x, double y) { return (-Gamma * y + Delta * x * y); }


void runge_kutta(double *x, double *y, double h, double (*fx)(double, double),
                 double (*fy)(double, double)) {
    double dx1, dx2, dx3, dx4, dy1, dy2, dy3, dy4;

    dx1 = fx(*x, *y);
    dy1 = fy(*x, *y);
    dx2 = fx(*x + (h / 2.0) * dx1, *y + (h / 2.0) * dy1);
    dy2 = fy(*x + (h / 2.0) * dx1, *y + (h / 2.0) * dy1);
    dx3 = fx(*x + (h / 2.0) * dx2, *y + (h / 2.0) * dy2);
    dy3 = fy(*x + (h / 2.0) * dx2, *y + (h / 2.0) * dy2);
    dx4 = fx(*x + h * dx3, *y + h * dy3);
    dy4 = fy(*x + h * dx3, *y + h * dy3);

    *x += h * (dx1 + 2.0 * dx2 + 2.0 * dx3 + dx4) / 6.0;
    *y += h * (dy1 + 2.0 * dy2 + 2.0 * dy3 + dy4) / 6.0;
}

int main() {
    double xm[10000], ym[10000];
    double x, y;
    double i = T_start;

    x = X_init;
    y = Y_init;

    ofstream foutx("outx.txt");
    ofstream fouty("outy.txt");
    ofstream fouth("outh.txt");
    ofstream foutxs("outxs.txt");
    ofstream foutys("outys.txt");
    ofstream fouths("ouths.txt");
    int counter;

    while (i < T_finish){
        if(counter%50==0){
            foutxs <<x <<",\n";
            foutys <<y <<",\n";
            fouths <<i <<",\n";

        }


    //foutx << x<<", ";
    //fouty << y <<", ";
    foutx << x << ",\n";
    fouty << y << ",\n";
    fouth << i << "," << "\n";

        runge_kutta(&x, &y, H, fx, fy);
        i+=H;
        counter++;

    }



    foutx.close();
    fouty.close();
    return 0;
}