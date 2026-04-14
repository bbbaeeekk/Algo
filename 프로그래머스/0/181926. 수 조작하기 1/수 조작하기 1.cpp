#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n, string control) {
    int answer = 0;
    
    
    for (char s : control) {
        if (s == 'w'){n +=1;}
        else if (s == 's'){n -=1;}
        else if (s == 'd'){n +=10;}
        else if (s == 'a'){n -=10;}
    }
    answer = n;
    
    return answer;
}