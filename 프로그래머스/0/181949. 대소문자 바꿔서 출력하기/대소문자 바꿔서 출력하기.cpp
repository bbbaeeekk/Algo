#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    for (char x : str){

        if (isupper(x)){

            char a = tolower(x);
            cout << a;
        }
        else if (islower(x)){

            char b = toupper(x);
            cout << b;
        }
    }
    
    return 0;
}