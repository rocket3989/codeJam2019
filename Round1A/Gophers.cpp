#include <iostream>
#include <unordered_map> 
#include <vector>
#include <cstdlib>
#include <utility>
#include <string>
#include <math.h>
#include <set>
#include <map>

using namespace std;

int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int T, N, M;
    cin >> T >> N >> M;

    for(int test = 0; test < T; test++){
        int mods[7] = {};

        int guesses [7] = {17,16,13,11,9,7,5};

        for(int guess = 0; guess < 7; guess++){
            for(int i = 0; i < 18; i++)
                cout << guesses[guess] << ' ';
            cout << endl;

            int count = 0;
            for(int i = 0; i < 18; i++){
                int temp;
                cin >> temp;
                count += temp;
            }

            count %= guesses[guess];

            mods[guess] = count;
        }
        
        for(int i = 0; i < M; i++){
            bool found = true;
            for(int mod = 0; mod < 7; mod++){
                if(i % guesses[mod] != mods[mod])
                    found  = false;
            }
            if(found){
                cout << i << endl;
                break;
            }
        }
        int output;
        cin >> output;
        if(output == -1)
            break;
    }
}