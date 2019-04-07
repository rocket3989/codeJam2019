#include <iostream>
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

    int tests = 0;
    cin >> tests;
    for(int test = 0; test < tests; test++){

        lli N;
        int len;

        cin >> N >> len;


        vector <lli> input;

        lli val;
        for(int i = 0; i < len; i++){
            cin >> val;
            input.push_back(val);
        }

        lli a = input[0], b = input[1];

        while(b > 0){
            lli temp = b;
            b = a % b;
            //b = fmod(a,b);
            a = temp;
        }
        
        vector <lli> primes;


        lli curr_prime = input[0] / a;

        primes.push_back(curr_prime);

        for(int i = 0; i < len; i++){
            curr_prime = input[i]/curr_prime;
            primes.push_back(curr_prime);
        }


        map <lli,char> primeMap;

        char charCount = 65;


        set<lli> Uprimes(primes.begin(),primes.end());
        for ( set<lli>::iterator it=Uprimes.begin(); it!=Uprimes.end(); ++it)
            primeMap[*it] = charCount++;
        
        string output;

        for(int i = 0; i < primes.size(); i++){
            output += primeMap[primes[i]];
        }

        cout << "Case #" << test + 1 << ": "<< output << endl;
    }
}


/*



103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053

CJQUIZKNOWBEVYOFDPFLUXALGORITHMS
CCJQUIZKNOWBEVYOFDPFLUXALGORITHMS

IPTHYJMNVBDUXNECOEKTWAKFNQHSGLR

10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543

SUBDERMATOGLYPHICFJKNQVWXZ
SUBDERMATOGLYPHICFJKNQVWXZ
 TBDERMASOGLXPHICFJKNQUVWY

*/



