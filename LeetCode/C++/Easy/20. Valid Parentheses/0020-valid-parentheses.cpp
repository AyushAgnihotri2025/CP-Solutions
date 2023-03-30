class Solution {
public:
    bool isValid(string s) {
        map<char, char> paren;
        paren['('] = ')';
        paren['{'] = '}';
        paren['['] = ']';
        set<char> keys = {'(', '{', '['};
        stack<char> stk;
        for(char c : s){
            if(keys.find(c) != keys.end()){
                stk.push(c);
            }else if(!stk.empty() && paren[stk.top()] == c){
                stk.pop();
            }else{
                return false;
            }
        }
        return stk.empty();
    }
};