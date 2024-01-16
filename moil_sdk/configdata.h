#ifndef CONFIGDATA_H
#define CONFIGDATA_H

#include <string>
#include <iostream>
#include <cmath>

#define PI 3.1415926
using namespace std;

class ConfigData {
    public:
        double cameraSensorWidth, cameraSensorHeight;
        double iCx, iCy;
        double dCx, dCy;
        double ratio;

        double imageWidth, imageHeight;
        double para0, para1, para2, para3, para4, para5;
        double calibrationRatio;

        string cameraName;
        int alphaToRho_Table[1800];  // degree /10
        int rhoToAlpha_Table[3600];  // pixel

        ConfigData();
        void setCameraSensorWidth(double cameraSensorWidth);
        void setCameraSensorHeight(double cameraSensorHieght);
        void setIcx(double iCx);
        void setIcy(double iCy);
        void setDcx(double dCx);
        void setDcy(double dCy);
        void setRatio(double ratio);
        void setImageWidth(double imageWidth);
        void setImageHeight(double imageHeight);
        void setParameter0(double parameter0);
        void setParameter1(double parameter1);
        void setParameter2(double parameter2);
        void setParameter3(double parameter3);
        void setParameter4(double parameter4);
        void setParameter5(double parameter5);
        void setCalibrationRatio(double calibrationRatio);
        void setCameraName(string cameraName);
        double getCameraSensorWidth();
        double getCameraSensorHeight();
        double getIcx();
        double getIcy();

        ConfigData *getcd();
        double getDcx();
        double getDcy();
        double getRatio();
        double getImageWidth();
        double getImageHeight();
        double getParameter0();
        double getParameter1();
        double getParameter2();
        double getParameter3();
        double getParameter4();
        double getParameter5();
        double getCalibrationRatio();

        string getCameraName();
        void initAlphaRho_Table();
        int getRhoFromAlpha(double alpha);
        double getAlphaFromRho(int rho);
};

#endif // CONFIGDATA_H
