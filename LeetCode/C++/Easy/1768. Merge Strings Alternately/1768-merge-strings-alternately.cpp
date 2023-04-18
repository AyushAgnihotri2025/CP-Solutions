class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string merged;
        int i = 0;
        for (char c : word1 + word2) {
            if (i < word1.length()) {
                merged += word1[i];
            }
            if (i < word2.length()) {
                merged += word2[i];
            }
            i++;
        }
        return merged;
    }
};