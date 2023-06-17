# Palindromic Strings
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given string <strong>s</strong> and an integer, you have to transform <strong>s</strong> into a <strong>palindrome</strong>. In order to achieve that you have to perform exactly <strong>k</strong> insertion of characters(you cannot perform anymore or less number of insertions). The task is to check if the string can be converted to a palindrome by making exactly <strong>k</strong> insertions.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: s = "abac", K = 2
<strong>Output:</strong> 1</span>
<span style="font-size:18px"><strong>Explanation</strong>: "abac" can be transformed to 
"cabbac" (which is palindrome) adding 
two characters c and b.</span></pre>

<div><span style="font-size:18px"><strong>Example 2:</strong></span></div>

<pre><span style="font-size:18px"><strong>Input</strong>: s = "abcde", K = 3
<strong>Output:</strong> 0</span>
<span style="font-size:18px"><strong>Explanation</strong>: "abcde" cannot be transformed
to palindrome using 3 insertions.</span></pre>

<div><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Complete the function <strong><code>isPossiblePalindrome</code>()&nbsp;</strong>which takes <strong>s</strong> and <strong>K </strong>as input parameters and returns a boolean value<br>
<br>
<strong>Expected Time Complexity:</strong> O(<strong>|s|<sup>2</sup></strong>)<br>
<strong>Expected Auxiliary Space:</strong> O(<strong>|s|<sup>2</sup></strong>)<br>
<br>
<strong>Constraints:</strong><br>
1 ≤ <strong>|s|</strong> ≤ 10<sup>3<br>
<strong>s</strong> contains lower case English alphabets</sup></span></div>
</div>