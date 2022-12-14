// #include <bits/stdc++.h>
#include <iostream>
#include <vector>

#define ll long long
// #define fast std::ios_base::sync_with_stdio(0);std::cin.tie(0);`

using namespace std;

void welcome() {
    cout << "\x1B[32mWelcome to this cool cpp script." << endl;
    cout << "All this script does is:" << endl;
    cout << "  1. Get integer N -> how many numbers on one line separated by whitespace are going to be given." << endl;
    cout << "  2. Get N integers on single line." << endl;
    cout << "  2. Print out sum of given sequence.\n" << endl;
    cout << "Example:" << endl;
    cout << "Input:\n3\n1 2 3" << endl;
    cout << "Output:\n6\n\n\e[0m" << endl;
}

int main() {
    welcome();

    ll n, ans = 0;
    cin >> n;
    vector<ll> temp(n);
    for (ll i = n; i; i--) {
        cin >> temp[i];

        ans += temp[i];
    }
    cout << ans << endl;
    return 0;
}