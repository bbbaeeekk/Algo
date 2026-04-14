#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;
    
    unordered_map<string,int> score_map;
    
    
    
    for (int i = 0; i < name.size(); i++)
    {
        score_map[name[i]] = yearning[i];
    }
    
    for (int j = 0; j < photo.size(); j++)
    {
        int score = 0;
        for ( int k = 0 ; k < photo[j].size(); k++)
            score += score_map[photo[j][k]];
        answer.push_back(score);
    }

    return answer;
}