#include <bits/stdc++.h>
#include <cstdlib>

#ifdef _WIN32
    #define EXECINWIN32 true
    #define EXECINPOSIX false
#elif defined(unix) || defined(__unix__) || defined(__unix) || (defined(__APPLE__) && defined(__MACH__))
    #define EXECINPOSIX true
    #define EXECINWIN32 false
#else
    #error "Error: Unknown OS platform to perform the execution!"
#endif

using std::cout, std::endl, std::string;
char *StringUppercase(char*);

struct MoildevStructure {
    const char *CPPCompiler = "g++", *IntoObject = "-o";
    const char *PackageConfigurations          = "`pkg-config";
    const char *PackageConfigurationFlagsWIN32 = "--libs=";
    const char *PackageConfigurationFlagsPOSIX = "--cflags --libs`";
    const char *RunBuilderWIN32                = "; .\\";
    const char *RunBuilderPOSIX                = "&& ./";
    char *Executable, *CPPSourceFile;
    char *LocalSourceDirectory, *ExternalPackages;
} MoildevBuilder;

char *StringUppercase(char* SourceString) {
    for (int i = 0; SourceString[i] != '\0'; i++) {
        if (SourceString[i] >= 'a' && SourceString[i] <= 'z') { SourceString[i] -= 32; }
    } return SourceString;
}

int main(int argc, char **argv) {
    char OutputSystemExecuting[1024], ExecutableFile[1024];

    // Executing commands for Ubuntu 18.04 (or above)
    // g++ -o <executable> <source> "moil_sdk/moildev.a" `pkg-config opencv4 --cflags --libs`

    // Executing commands for Raspberry Pi
    // g++ -o <executable> <source> "moil_sdk/moildev_rpi.a" `pkg-config opencv4 --cflags --libs`

    cout << "(MoildevBuilder) Usages [prompt]: " << endl;
    cout << "> Windows (WIN32): " << endl;
    cout << "    ./BuildMoildev [run || -r || --run] WIN32" << endl;
    cout << "        or" << endl;
    cout << "    .\\BuildMoildev [run || -r || --run] WIN32" << endl;
    cout << "> POSIX/MacOS (Unix): " << endl;
    cout << "    ./BuildMoildev [run || -r || --run] [UNIX || MACH || APPLE]" << endl;
    cout << endl;

    // Configure everything necessary for the compilation process.
    MoildevBuilder.Executable           = (char *)"MoildevFEMSA";
    MoildevBuilder.CPPSourceFile        = (char *)"MoildevFEMSA.cpp";
    MoildevBuilder.LocalSourceDirectory = (char *)"moil_sdk/moildev.a";
    MoildevBuilder.ExternalPackages     = (char *)"opencv4";

    if (EXECINWIN32) {
        if ((strcmp(StringUppercase(argv[1]), "RUN") == 0 || strcmp(StringUppercase(argv[1]), "-R") == 0 || strcmp(StringUppercase(argv[1]), "--RUN") == 0) && (strcmp(StringUppercase(argv[2]), "WIN32") == 0)) {
            snprintf(OutputSystemExecuting, 1024, 
            "%s %s %s %s \"%s\" %s%s", 
            MoildevBuilder.CPPCompiler, MoildevBuilder.IntoObject,
            MoildevBuilder.Executable, MoildevBuilder.CPPSourceFile,
            MoildevBuilder.LocalSourceDirectory, MoildevBuilder.PackageConfigurationFlagsWIN32,
            MoildevBuilder.ExternalPackages);
            snprintf(ExecutableFile, 1024, "%s%s", MoildevBuilder.RunBuilderWIN32, MoildevBuilder.Executable);

            system(OutputSystemExecuting);
        }
    } else if (EXECINPOSIX) {
        if ((strcmp(StringUppercase(argv[1]), "RUN") == 0 || strcmp(StringUppercase(argv[1]), "-R") == 0 || strcmp(StringUppercase(argv[1]), "--RUN") == 0) && (strcmp(StringUppercase(argv[2]), "UNIX") == 0 || strcmp(StringUppercase(argv[2]), "MACH") == 0 || strcmp(StringUppercase(argv[2]), "APPLE") == 0)) {
            snprintf(OutputSystemExecuting, 1024, 
            "%s %s %s %s \"%s\" %s%s", 
            MoildevBuilder.CPPCompiler, MoildevBuilder.IntoObject,
            MoildevBuilder.Executable, MoildevBuilder.CPPSourceFile,
            MoildevBuilder.LocalSourceDirectory, MoildevBuilder.PackageConfigurations,
            MoildevBuilder.ExternalPackages, MoildevBuilder.PackageConfigurationFlagsPOSIX);
            snprintf(ExecutableFile, 1024, "%s%s", MoildevBuilder.RunBuilderPOSIX, MoildevBuilder.Executable);

            system(OutputSystemExecuting);
        }
    }

    system(ExecutableFile);
    cout << endl;

    if (EXECINWIN32) cout << "[+] System: Windows (WIN32)"        << endl;
    else             cout << "[+] System: Unix/Apple/Mac (POSIX)" << endl;
    cout << "[+] Prompt: " << OutputSystemExecuting << endl;
    return 0;
}