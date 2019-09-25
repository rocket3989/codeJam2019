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


class Class{

public:
    Class(int _attr = 0){
        attr = _attr;
    }
    int getAttr(){
        return attr;
    }
    void setAttr(int _attr){
        attr = _attr;
    }
private:
    int attr;
};


int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    const int size = 10;
    Class arr [size];

    for(int test = 0; test < T; test++){
        int P, Q, x, y;
        char D;
        cin >> P >> Q;

        cout << "Case #" << test + 1 << ": " << x << ' ' << y << endl;
    }
}
