# Fisheye Monitoring System Application

## FTDC - Team 3

### Sources: Moildev SDKs, Qt Creator, and OpenCV

## A. Introduction

Fisheye Monitoring System Application is a project that we from FTDC Laboratory in Telkom University work on, as we try to understand more of the depth about how fisheye cameras work in particular purposes, and how it can benefit more in OpenCV's technologies nowadays.

This project includes the following libraries to work with, especially with the Moildev and OpenCV SDKs and such.

For more information, please refer to the original documentation
about moildev's header and configurations by given the link below:

> Moildev SDK: <https://github.com/cjchng/moil_sdk>

For C++ libraries purposes, I as the creator of this repository depends on MSYS2 libraries (because I'm working in Windows, but it does also work on Unix/POSIX systems, including Apple/MacOS). Please refer to the link(s) below for more information:

> OpenCV: <https://github.com/opencv/opencv>

As for Python libraries, I use Qt(s) for development purposes, i.e. designing the UI app, and coding the app for simple add-ons, such as tooltips for each buttons, layers, etc. For more information please refer to the official Qt website, featuring Qt Creator, and originally as the development tools from pip (PYPI):

### 1. Application Creation and Designing Purposes

Qt Creator 12.0.1 (Community)
> Qt Creator 12.0.1 (Community): <https://www.qt.io/offline-installers>

### 2. Development Tools with (PyQt5 and PyQt6)

PyQt5:
> PyQt5: <https://pypi.org/project/pyqt5>

PyQt6:
> PyQt6: <https://pypi.org/project/pyqt6>

or

### (Optional) Development Tools with PySide6

> PySide6: <https://pypi.org/project/pyside6/>

### Note: This project also uses PySide6 for development, but it's an optional one since I made two versions of the app, and it can use either the PyQt6 or the PySide6 one

As for the development tools, just consider to add `-tools` when installing using PIP command, as shown below:

    pip install pyqt5-tools

or

    pip install pyqt6-tools

## B. Program Usage (Python)

In order to use the program, you can run the Pythons file that consisting the word `-Application` right away without importing any other external libraries, by just doing this so:

    [py || python3] -u "(directory)//PyQt6-Application.py"

or

    [py || python3] -u "(directory)//PySide6-Application.py"

If you want to run the app separately by importing the `WidgetUI` module, then you may refer to the both file namely as:

> Run the main application file ONLY without changing or interfering with the applications design and code stuffs:

    > File name: MainApplication.py
    Then, do:
        [py || python3] -u "(directory)//MainApplication.py"

> If you want to work with the application programs ONLY without running the app everytime you execute the code, you may go with the file namely as:

    > File name: FishEyeMonitoring.py
    Then, do:
        [py || python3] -u "(directory)//MainApplication.py"

### Note: For file names `form.ui`, `ui_form.py`, and `widget.py`, PLEASE DO NOT ATTEMPT TO EDIT THOSE FILES, unless you're working with the Qt Creator/Designer mentioned above, since it's a case sensitive file for any changes been made OUTSIDE of the Qt Creator/Designer app

## C. Program Usage (C++)

There're few restrictions on how to use the C++ file, hence this may need Ubuntu and/or Raspberry PI for development safely, and not much libraries that most Windows GCC/G++'s compiler do have, but since I use MSYS2 for development here using Windows, I make some rule that it can only be compiled in Windows and on Unix/POSIX systems separately.

In order to do that, please make sure that you got the OpenCV library for C++ first above, then you may proceed to do the following:

    (MoildevBuilder) Usages [prompt]: 
    > Windows (WIN32): 
        ./BuildMoildev [run || -r || --run] WIN32
            or
        .\BuildMoildev [run || -r || --run] WIN32
    > POSIX/MacOS (Unix): 
        ./BuildMoildev [run || -r || --run] [UNIX || MACH || APPLE]

That is the result of calling a G++ compiler command to compile and execute the specific file name, targeted as: `BuildMoildev.cpp`.

In order to obtain the program usage prompt like that, please run the following command firstly:

    g++ -Wall -Wextra -pedantic -ggdb BuildMoildev.cpp -o BuildMoildev

Then, in order to run it, you can just run the program by the following command:

    ./BuildMoildev

or

    .\BuildMoildev

_(depends on some operating systems)..._

Next, try to run the following additional variabel arguments, namely as `char **argv` in C++ driver program `int main()` declarations, such as:

    ./BuildMoildev run WIN32

for Windows operating systems, and:

    ./BuildMoildev run UNIX

for Unix/POSIC operating systems.

### Note: If you tried to run one of the commands above in a different required operating system to work, you may get an unexpected result though in the end

And for the commands, __REMEMBER THAT__ the subcommand `run` or `-r` or `--run` shall be provided before the type of the operating system to be executing at, and here's the list of `OK` subcommands for the type of operating systems:

    > Windows:
    win32, WIN32

    > Unix/POSIX:
    unix, mach, apple (all lowercase)
    UNIX, MACH, APPLE (all uppercase)

_(it also works on Raspberry PI operating systems, since its dependecies also come mostly from Linux operating system)..._

## Future updates may coming soon
