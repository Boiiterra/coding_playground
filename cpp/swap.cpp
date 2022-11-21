// swap two middle digits in ints from 1000 to 9999 including last

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int a;
    cin >> a;
    cout << a / 1000 << (a % 100) / 10 << (a / 100) % 10 << a % 10 << endl;
    return 0;
}


