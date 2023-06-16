# Number of palindromic strings
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two integers <strong>N</strong> and <strong>K</strong>, the task is to find the count of palindromic strings of length lesser than or equal to <strong>N</strong>, with first K characters of lowercase English language, such that each character in a string doesn’t appear more than twice.</span></p>

<p><span style="font-size:18px"><strong>Note:</strong> Anwer can be very large, so, output answer modulo 10<sup>9</sup>+7</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> N = 3, K = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> </span><span style="font-size:20px">The possible strings are:
"a", "b", "aa", "bb", "aba", "bab".</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> N = 4, K = 3
<strong>Output:</strong> 18
<strong>Explanation:</strong> </span><span style="font-size:20px">The possible strings are: 
"a", "b", "c", "aa", "bb", "cc", "aba",
"aca", "bab", "bcb", "cac", "cbc", 
"abba", "acca", "baab", "bccb", "caac", 
"cbbc".&nbsp;</span></pre>

<p><span style="font-size:18px"><strong>Your task:</strong><br>
You do not need to read any input or print anything. The task is to complete the function <strong>palindromicStrings()</strong>, which takes two integers as input and returns the count. </span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(K<sup>2</sup>)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(K<sup>2</sup>)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong></span><br>
<span style="font-size:18px">1 ≤ K ≤ 26<br>
1 ≤ N ≤ 52<br>
N ≤ 2*K</span></p>
</div>