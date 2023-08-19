#include <iostream>
 
using namespace std;
 
 
int a = 0, b = 0;
 
 
int main() {
    cin >> a >> b;
    if (a > b) {
        cout << ">" << endl ;
    }
    else if (a < b) {
        cout << "<" << endl;
    }
    else {
        cout << "==" << endl;
    }
 
}