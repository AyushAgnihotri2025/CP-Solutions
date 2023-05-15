# Count ways to increase LCS length of two strings by one
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two strings <strong>S1</strong> and <strong>S2</strong>&nbsp;of lower alphabet characters of length <strong>N1 </strong>and <strong>N2</strong>, we need to find the number of ways to insert a character in the first string S1&nbsp;such that length of LCS&nbsp;of both strings increases by one.</span><br>
<br>
<strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N1 = 4
S1 = abab
N2 = 3
S2 = abc
<strong>Output:</strong>
3
<strong>Explanation:</strong>
LCS length of given two 
strings is 2. There are 3 
ways of insertion in str1,to 
increase the LCS length by 
one which are enumerated below, 
str1 = “abcab” str2 = “abc” LCS length = 3 
str1 = “abacb” str2 = “abc” LCS length = 3 
str1 = “ababc” str2 = “abc” LCS length = 3</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N1 = 6
S1 = abcabc
N2 = 4
S2 = abcd<strong>
Output:
</strong>4<strong>
Explanation:
</strong>LCS length of given two
strings is 3. There are 4
ways of insertion in str1,to
increase the LCS length by
one which are enumerated below,
str1 = “abcdabc” str2 = “abcd” LCS length = 4
str1 = “abcadcb” str2 = “abcd” LCS length = 4
str1 = “abcabdc” str2 = “abcd” LCS length = 4
str1 = “abcabcd” str2 = “abcd” LCS length = 4</span>
</pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>waysToIncreaseLCSBy1</strong><strong>()</strong>&nbsp;which take&nbsp;string S1 and string S2 of length N1 and N2 respectively&nbsp;as input parameters and returns the number of ways to insert a character in the first string S1&nbsp;such that length of LCS&nbsp;of both strings increases by one.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N1 * N2)&nbsp;<br>
<strong>Expected Space Complexity:</strong>&nbsp;O(N1 * N2)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong></span><br>
<span style="font-size:18px">1&lt;= N1, N2&nbsp;&lt;=100<br>
S1 and S2 contains lower case English character</span></p>
</div>