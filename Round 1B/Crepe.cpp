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

typedef long double ld;

typedef unsigned long long lli;


int maxOf(int a, int b){
    return (a > b ? a : b);
}

int minOf(int a, int b){
    return (a < b ? a : b);
}



int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    for(int test = 0; test < T; test++){
        int P, Q, x, y;
        char D;
        cin >> P >> Q;

        vector <int> xUpper, xLower, yUpper, yLower;
        
        xUpper.assign(Q,0);
        xLower.assign(Q,0);
        yUpper.assign(Q,0);
        yLower.assign(Q,0);
        
        for(int i = 0; i < P; i++){
            cin >> x >> y >> D;

            switch(D){
                case 'N':
                    yLower[y]++;
                    break;
                case 'S':
                    yUpper[y]++;
                    break;
                case 'E':
                    xLower[x]++;
                    break;
                case 'W':
                    xUpper[x]++;
                    break;
            }
        }

        int xBest = xLower[0] - xUpper[0], yBest = yLower[0] - yUpper[0];
        x = 0, y = 0;

        int sum = 0;

        for(int i = 1; i < Q; i++){
            sum += xLower[i-1] - xUpper[i];
            if(sum > xBest){
                x = i; 
                xBest = sum;
            }
        }
        sum = 0;
        for(int i = 1; i < Q; i++){
            sum = sum + (yLower[i-1] - yUpper[i]);
            if(sum > yBest){
                y = i; 
                yBest = sum;
            }
            
        }

        cout << "Case #" << test + 1 << ": " << x << ' ' << y << endl;
    }

}




/*



3
1 10
5 5 N
4 10
2 4 N
2 6 S
1 5 E
3 5 W
8 10
0 2 S
0 3 N
0 3 N
0 4 N
0 5 S
0 5 S
0 8 S
1 5 W

*/