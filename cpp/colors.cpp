#include <iostream>
#include <string>

using namespace std;

// ANSI escape color codes

void ansi() {
    printf("\n");
    printf("\x1B[31mTexting\033[0m\t\t");
    printf("\x1B[32mTexting\033[0m\t\t");
    printf("\x1B[33mTexting\033[0m\t\t");
    printf("\x1B[34mTexting\033[0m\t\t");
    printf("\x1B[35mTexting\033[0m\n");
    printf("\x1B[36mTexting\033[0m\t\t");
    printf("\x1B[36mTexting\033[0m\t\t");
    printf("\x1B[36mTexting\033[0m\t\t");
    printf("\x1B[37mTexting\033[0m\t\t");
    printf("\x1B[93mTexting\033[0m\n");
    printf("\033[3;42;30mTexting\033[0m\t\t");
    printf("\033[3;43;30mTexting\033[0m\t\t");
    printf("\033[3;44;30mTexting\033[0m\t\t");
    printf("\033[3;104;30mTexting\033[0m\t\t");
    printf("\033[3;100;30mTexting\033[0m\n");
    printf("\033[3;47;35mTexting\033[0m\t\t");
    printf("\033[2;47;35mTexting\033[0m\t\t");
    printf("\033[1;47;35mTexting\033[0m\t\t");
    printf("\t\t\e[0m");
    printf("\n");
}

// void more_colors() {
//     HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
//     #include <windows.h>
//     // you can loop k higher to see more color choices
//     for(int k = 1; k < 255; k++)
//     {
//         // pick the colorattribute k you want
//         SetConsoleTextAttribute(hConsole, k);
//         cout << k << " I want to be nice today!" << endl;
//     }
// }

int main(int argc, char ** argv){
    // more_colors(); // Works on windows
    ansi();
    return 0;
}
