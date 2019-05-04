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

#define MX 1000000



int maxOf(int a, int b){
    return (a > b ? a : b);
}

int minOf(int a, int b){
    return (a < b ? a : b);
}

int abs(int a){
    return ( a > 0 ? a : -a);
}

int C[MX];
int D[MX];


int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    for(int test = 1; test <= T; test++){

        int N, K;
        cin >> N >> K;

        for(int i = 0; i < N; i++)
            cin >> C[i];
        for(int i = 0; i < N; i++)
            cin >> D[i];

        int count  = 0;

        for(int L = 0; L < N; L++){
            for(int R = L; R < N; R++){
                int maxC = 0, maxD = 0;
                for(int i = L; i <= R; i++){
                    maxC = maxOf(C[i],maxC);
                    maxD = maxOf(D[i],maxD);
                }
                if(abs(maxC - maxD) <= K)
                    count++;
            }
        }

        cout << "Case #" << test << ": " << count << endl;

    }
}
/*
N K
C0 C1 C2 C3 C4
D0 D1 D2 D3 D$







*/