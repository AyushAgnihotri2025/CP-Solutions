//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class BrowserHistory {
public:
    stack<string>st,rev;
     // constructor to initialize object with homepage
    BrowserHistory(string homepage) {
        st.push(homepage);
    }
    
    // visit current url
    void visit(string url) {
        st.push(url);
        while(!rev.empty()) rev.pop();
    }
    
    // 'steps' move backward in history and return current page
    string back(int steps) {
        if(steps>=st.size()) {
            while(st.size()!=1) {
                rev.push(st.top());
                st.pop();
            }
            
        } else {
            while (steps && !st.empty()) {
                rev.push(st.top());
                st.pop();
                steps--;
            }
        }
        return st.top();
    }
    
    // 'steps' move forward and return current page
    string forward(int steps) {
        if(steps>=rev.size()) {
            while(!rev.empty()) {
                st.push(rev.top());
                rev.pop();
            }
            
        } else {
            while (steps && !rev.empty()){
                st.push(rev.top());
                rev.pop();
                steps--;
            }
        }
        return st.top();
    }
};

//{ Driver Code Starts.

int main()
{
    string homepage;
    cin >> homepage;
    
    BrowserHistory obj(homepage);
    
    int total_queries;
    cin >> total_queries;
    while(total_queries--)
    {
        int query;
        cin >> query;
        
        // if query = 1, visit()
        // if query = 2, back()
        // if query = 3, forward()
        
        if(query == 1) {
            string url;
            cin >> url;
            obj.visit(url);
        }
        else if(query == 2) {
            int steps;
            cin >> steps;
            cout << obj.back(steps) << endl;
        }
        else {
            int steps;
            cin >> steps;
            cout << obj.forward(steps) << endl;
        }
    }
    return 0;
}
// } Driver Code Ends