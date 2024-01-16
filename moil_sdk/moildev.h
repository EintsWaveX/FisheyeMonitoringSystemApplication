#ifndef MOILDEV_H
#define MOILDEV_H

#include <cstdio>
#include <string>
#include <iostream>
#include <cmath>
#include <vector>

#include "configdata.h"

#define PI                    3.1415926
#define PI_2                  1.5707963
#define PCT_UNIT_WIDTH        1.27
#define PCT_UNIT_HEIGHT       1.27
#define FOCAL_LENGTH_FOR_ZOOM 250
#define APPROX_FACT           8

using namespace std;

class Moildev {
    public:
        class ConfigData* cfg;

/*
Purpose:
Each fisheye camera can be calibrated and derives a set of parameters by MOIL laboratory, before the successive functions can work correctly, configuration is necessary in the beginning of program.

Parameters:
`cameraName`         - A string to describe this camera
`cameraSensorWidth`  - Camera sensor width  `(in cm)`
`cameraSensorHeight` - Camera Sensor Height `(in cm)`
`iCx` - Image center at `X` coordinate      `(in pixel)`
`iCy` - Image center at `Y` coordinate      `(in pixel)`
`i_ratio`:          Sensor pixel aspect ratio
`imageWidth`:       Input image width
`imageHeight`:      Input image height  
`calibrationRatio`: Input imageWidth / calibrationImageWidth
`para0 ... para5`:  Calibration parameters

Example:
`#include "moildev.h"`
`Moildev *md = new Moildev();`

`// Raspberry Pi 220 degree fisheye camera`
`md->Config(`
    `"car", 1.4, 1.4,`
    `1320.0, 1017.0, 1.048,`
    `2592, 1944, 4.05,`
    `0, 0, 0, 0, -47.96, 222.86`
`);`
*/
        Moildev();
        bool fastMode = false; 
        
        /* Each fisheye camera can be calibrated and derives a set of parameters by MOIL laboratory, before the successive functions can work correctly, configuration is necessary in the beginning of program. */
        bool Config(string cameraName, 
                    double cameraSensorWidth, double cameraSensorHeight,
                    double iCx, double iCy,
                    double i_ratio,
                    double imageWidth, double imageHeight,
                    double calibrationRatio,
                    double para0, double para1, double para2, double para3, double para4, double para5
        );

        double getImageHeight();
        double getImageWidth();
        double getiCx();
        double getiCy();

        ConfigData *getcd();

/*
Purpose: 
Anypoint Mode 1, the purpose is to generate a pair of `X-Y` Maps for the specified `alpha`, `beta` and `zoom` parameters. The result `X-Y` Maps can be used later to remap the original fisheye image to the target angle `image`. The result rotation is `betaOffset` degree rotation around the `Z-axis(roll)` after `alphaOffset` degree rotation around the `X-axis(pitch)`.

Parameters:
`mapX`: Memory pointer of result `X`-Map   
`mapY`: Memory pointer of result `Y`-Map
`w`: Width of the Map (both `mapX` and `mapY`)
`h`: Height of the Map (both `mapX` and `mapY`)
`alphaOffset`:  Alpha offset 
`betaOffset`:   Beta offset
`zoom`:         Decimal zoom factor, normally `1...12`
`manification`: Input `imageWidth / calibrationWidth`, where `calibrationWidth` can get by calling `getImageWidth()`, manification is normally equal to `1`

Example:
`#include <opencv2/opencv.hpp>`
`#include "moildev.h"`
`Moildev *md = new Moildev();`

`// md->Config	`
`int m_ratio = 2592/ md->getImageWidth();`
`Mat mapX = Mat(1944, 2592, CV_32F);`
`Mat mapY = Mat(1944, 2592, CV_32F);`
`Mat image_input = imread( "image.jpg", IMREAD_COLOR);`
`Mat image_result;`
`md->AnyPointM((float *)mapX.data, (float *)mapY.data, mapX.cols, mapX.rows, 0, 0, 4, m_ratio);     `
`cv::remap(image_input, image_result, mapX, mapY, INTER_CUBIC, BORDER_CONSTANT, Scalar(0, 0, 0));`
*/
        double AnyPointM(float *mapX, float *mapY, int w, int h, double alphaOffset, double betaOffset, double zoom, double magnification);

/*
Purpose:
Anypoint mode 2, the purpose is to generate a pair of `X-Y` Maps for the specified `thetaX`, `thetaY` and `zoom` parameters. The result `X-Y` Maps can be used later to remap the original fisheye image to the target `angle` image. The result rotation is `thetaY` degree rotation around the `Y-axis(yaw)` after `thetaX` degree rotation around the `X-axis(pitch)`.

Parameters:
`mapX`: Memory pointer of result `X`-Map
`mapY`: Memory pointer of result `Y`-Map
`w`: Width of the Map (both `mapX` and `mapY`)
`h`: Height of the Map (both `mapX` and `mapY`)
`thetaX_degree`: `thetaX`
`thetaY_degree`: `thetaY`
`zoom`: decimal zoom factor, normally `1...12`
`manification`: input `imageWidth / calibrationWidth`, where `calibrationWidth` can get by calling `getImageWidth()`, manification is normally equal to `1`

Example:
`#include <opencv2/opencv.hpp>`
`#include "moildev.h"`
`Moildev *md = new Moildev();`

`// md->Config`
`int m_ratio = 2592/ md->getImageWidth();`
`Mat mapX = Mat(1944, 2592, CV_32F);`
`Mat mapY = Mat(1944, 2592, CV_32F);`
`Mat image_input = imread( "image.jpg", IMREAD_COLOR);`
`Mat image_result;`

`md->AnyPointM2((float *)mapX.data, (float *)mapY.data, mapX.cols, mapX.rows, 30, 30, 4, m_ratio);     `
`cv::remap(image_input, image_result, mapX, mapY, INTER_CUBIC, BORDER_CONSTANT, Scalar(0, 0, 0));`
*/
        double AnyPointM2(float *mapX, float *mapY, int w, int h, double thetaX_degree, double thetaY_degree, double zoom, double magnification);

/*
Purpose:
To generate a pair of `X-Y` Maps for the specified `alpha`, `beta` and `zoom` parameters. The result `X-Y` Maps can be used later to remap the original fisheye image to the target `angle` image. This function use fast algorithm to achieve similar result. However, some sampling artifacts appear with larger `alphaOffset` value. This function save about `50%` computing time on Raspberry Pi.

Parameters:
Same as the function of `AnyPointM2`'s parameters above.

Example:
Same as the function of `AnyPointM2`'s example above.
*/
        double fastAnyPointM(float *mapX, float *mapY, int w, int h, double alphaOffset, double betaOffset, double zoom, double magnification);
        
/*
Purpose:
To generate a pair of X-Y Maps for alpha within 0..alpha_max degree, the result X-Y Maps can be used later to generate a panorama image from the original fisheye image.

Parameters:
`mapX`: Memory pointer of result `X`-Map   
`mapY`: Memory pointer of result `Y`-Map
`w`: Width of the Map (both `mapX` and `mapY`)
`h`: Height of the Map (both `mapX` and `mapY`)
`manification`: Input `imageWidth / calibrationWidth`, where `calibrationWidth` can get by calling `getImageWidth()`, manification is normally equal to `1`
`alpha_max`: Max of Alpha. The recommended vaule is half of camera FOV. For example, use `90` for a `180` degree fisheye images and use `110` for a `220` degree fisheye images

Example:
`#include <opencv2/opencv.hpp>`
`#include "moildev.h"`
`Moildev *md = new Moildev();`

`// md->Config	`
`int m_ratio = 2592/ md->getImageWidth();`
`Mat mapX = Mat(1944, 2592, CV_32F);`
`Mat mapY = Mat(1944, 2592, CV_32F);`
`Mat image_input = imread( "image.jpg", IMREAD_COLOR);`
`Mat image_result;`

`md->PanoramaM((float *)mapX.data, (float *)mapY.data, mapX.cols, mapX.rows, m_ratio, 110);`
`cv::remap(image_input, image_result, mapX, mapY, INTER_CUBIC, BORDER_CONSTANT, Scalar(0, 0, 0));`
*/
        double PanoramaM(float *mapX, float *mapY, int w, int h, double magnification, double alpha_max);
        
/*
Purpose:
To generate a pair of `X-Y` Maps for `alpha` within `0...alpha_max` degree. The result `X-Y` Maps can be used later to generate a panorama image from the original fisheye image. The panorama image centered at the `3D` direction with `alpha = iC_alpha_degree` and `beta = iC_beta_degree`.

Parameters:
`mapX`: Memory pointer of result `X`-Map   
`mapY`: Memory pointer of result `Y`-Map
`w`: Width of the Map (both `mapX` and `mapY`)
`h`: Height of the Map (both `mapX` and `mapY`)
`manification`: Input `imageWidth / calibrationWidth`, where `calibrationWidth` can get by calling `getImageWidth()`, manification is normally equal to `1`.  
`alpha_max`: Max of `alpha`. The recommended vaule is half of camera FOV. For example, use `90` for a `180` degree fisheye images and use `110` for a `220` degree fisheye images.
`iC_alpha_degree`: Alpha angle of panorana center
`iC_beta_degree`: Beta angle of panorama center

Example:
`#include <opencv2/opencv.hpp>`
`#include "moildev.h"`
`Moildev *md = new Moildev();`

`// md->Config	`
`int m_ratio = 2592/ md->getImageWidth();`
`Mat mapX = Mat(1944, 2592, CV_32F);`
`Mat mapY = Mat(1944, 2592, CV_32F);`
`Mat image_input = imread( "image.jpg", IMREAD_COLOR);`
`Mat image_result;`

`md->PanoramaM_Rt((float *)mapX.data, (float *)mapY.data, mapX.cols, mapX.rows, m_ratio, 110, 30, 30);`
`cv::remap(image_input, image_result, mapX, mapY, INTER_CUBIC, BORDER_CONSTANT, Scalar(0, 0, 0));`
*/
        double PanoramaM_Rt(float *mapX, float *mapY, int w, int h, double magnification, double alpha_max, double iC_alpha_degree, double iC_beta_degree);
        
        int getRhoFromAlpha(double alpha);
        double getAlphaFromRho(int rho);

/*
Purpose:
To get `alpha` and `beta` value for point on original fisheye image.

Parameters:
`Mode`: `0` for Pitch/Roll mode (Mode 1), `1` for Pitch/Yaw mode (Mode 2) 
`Pos`: `X` and `Y` of point

Example (C++):
`#include <opencv2/opencv.hpp>`
`#include "moildev.h"`
`Moildev *md = new Moildev();`

`// md->Config	`
`int m_ratio = 2592/ md->getImageWidth();`
`Mat mapX = Mat(1944, 2592, CV_32F);`
`Mat mapY = Mat(1944, 2592, CV_32F);`
`Mat image_input = imread( "image.jpg", IMREAD_COLOR);`

`vector<int>Pos;`
`Pos.push_back(1000);`
`Pos.push_back(600);`
`vector<int>ab = md->getAlphaBetaFromPos(0, Pos);`

Example (Qt):
`Moildev md;`
`QPoint Pos = QPoint(1000, 600);`
`QPointF ab = md.getAlphaBetaFromPos(0, Pos);`
`currAlpha = (int)ab.x();`
`currBeta = (int)ab.y();`
*/
        vector<int> getAlphaBetaFromPos(int Mode, vector<int> Pos);
        
    private:
        double sinArray[90 * APPROX_FACT + 1]; 
        void initSin();
        double ApproxSin(double angle);
        double ApproxCos(double angle);

        float ApproxAtan(float z);
        float ApproxAtan2(float y, float x);
};

#endif // MOILDEV_H
