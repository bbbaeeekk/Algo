#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    
    for (int x : arr){
        answer.resize(answer.size() + x, x);
    }
    
    return answer;
}