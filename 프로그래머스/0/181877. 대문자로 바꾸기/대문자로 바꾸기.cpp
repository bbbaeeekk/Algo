#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string myString) {
    string answer = "";
    for (char& c : myString) c = toupper(c);
    answer = myString;
    
    return answer;
}