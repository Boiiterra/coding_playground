#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main() {
    srand(time(NULL));
    cout << "Guess the number game is started." << endl;
    while (true) {
        cout << "New number is generated from 1 to 100." << endl;
        cout << "Your goal is to guess it." << endl;
        cout << "If you want to exit enter 0." << endl;
        int randNum = rand() % 100 + 1;
        while (true) {
            int number;
            cout << "Number -> ";
            cin >> number;
            if (number == 0) {
                cout << "Are you sure that you want to exit? (y/n) ";
                char yn;
                scanf(" %c",&yn);
                if (tolower(yn) == 'y') {
                    cout << "Exiting..." << endl;
                    return 0;
                }
                else if (tolower(yn) == 'n') {
                    cout << "\nRestarted\n" << endl;
                    break;
                }
                else {
                    cout << "\nExiting with code 1" << endl;
                    return 1;
                }
            }
            else if (number == randNum) {
                cout << "\n\nYou guessed the number. It was '" << randNum << "'.\n\n" << endl;
                cout << "Do you want to restart? (y/n) ";
                char yn;
                scanf(" %c",&yn);
                if (tolower(yn) == 'n') {
                    cout << "Exiting..." << endl;
                    return 0;
                }
                else if (tolower(yn) == 'y') {
                    cout << "\nRestarted\n" << endl;
                    break;
                }
                else {
                    cout << "\nExiting with code 1" << endl;
                    return 1;
                }
                break;
            }
            else if (number > randNum) {
                cout << "Number '" << number << "' is to big." << endl;
            }
            else if (number < randNum) {
                cout << "Number '" << number << "' is to small." << endl;
            }
        }
    }
    cout << "Guess the number game is finished." << endl;
}