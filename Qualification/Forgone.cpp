#include <iostream>
#include <vector>
#include <cstdlib>
#include <utility>
#include <string>
using namespace std;


int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int tests = 0;
    cin >> tests;
    for(int test = 0; test < tests; test++){

        string input, a, b;

        cin >> input;

        bool found = false;

        for(int i = 0; i < input.size(); i++){
            if(input[i] == '4'){
                found = true;
                a += '2';
                b += '2';
            }
            else{
                a += input[i];
                if(found)
                    b += '0';
            }

        }
        
        cout << "Case #" << test + 1 << ": "<< a << ' ' << b << endl;
    }
}