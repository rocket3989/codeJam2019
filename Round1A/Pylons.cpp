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

#define x first
#define y second

typedef unsigned long long lli;

int maxOf(int a, int b){
    return (a > b ? a : b);
}

int minOf(int a, int b){
    return (a < b ? a : b);
}

vector<pair <int,int>> centers;
vector<pair <int,int>> points;

int net [250][250] = {0};

int R, C;