//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++

class Solution{   
public:
    string convertToWords(long n) {
        // code here
        string out;
        out += numToWords((n / 10000000), "crore ");
        out += numToWords(((n / 100000) % 100), "lakh ");
        out += numToWords(((n / 1000) % 100), "thousand ");
        out += numToWords(((n / 100) % 10), "hundred ");
        if (n > 100 && n % 100){
            out += "and ";
        }
        out += numToWords((n % 100), "");
        return out;
    }
    string numToWords(int n, string s){
        string one[] = { "", "one ", "two ", "three ", "four ",
                 "five ", "six ", "seven ", "eight ",
                 "nine ", "ten ", "eleven ", "twelve ",
                 "thirteen ", "fourteen ", "fifteen ",
                 "sixteen ", "seventeen ", "eighteen ",
                 "nineteen " };
        string ten[] = { "", "", "twenty ", "thirty ", "forty ",
                 "fifty ", "sixty ", "seventy ", "eighty ",
                 "ninety " };
        string str = "";
        if(n>19){
            str += ten[n / 10] + one[n % 10];
        }
        else{
            str += one[n];
        }
        if(n){
            str += s;
        }
        return str;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        long n;
        cin >> n;
        Solution ob;
        auto ans = ob.convertToWords(n);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends