//{ Driver Code Starts
//Initial Template for javascript
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for(;i<t;i++)
    {
        let n = parseInt(readLine());
        let arr = readLine().split(' ').map(x=>parseInt(x));
        let m = parseInt(readLine());
        let obj = new Solution();
        console.log(obj.findZeroes(arr, n, m));
    }
}

// } Driver Code Ends


//User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} n
 * @param {number} m
 * @return {integer}
 */
class Solution {
    findZeroes(a,n,m) {
        // code here
        let start = 0;
        let end = 0;
        let max_len = 0;
        let zeros = 0;
    
        while (end < n) {
            if (a[end] == 0 && zeros == m) {
                max_len = Math.max(max_len, end - start);
                while (a[start] != 0) {
                    start++;
                }
                start++;
            } else if (a[end] == 0) {
                zeros++;
            }
            end++;
        }
    
        max_len = Math.max(max_len, end - start);
        return max_len;
    }
}