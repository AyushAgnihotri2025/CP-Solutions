# Print kth character
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string S consisting of lower alphabetic characters. Find K-th character in the&nbsp;string formed by concatenating all the unique substring of the given string in a sorted form. </span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>S = banana
K = 10
<strong>Output:
</strong>n
<strong>Explanation:
</strong>All substring in sorted form are, 
"a","an","ana","anan","anana","b","ba", 
"ban","bana","banan","banana","n","na", 
"nan", "nana".
Concatenated string = 
"aananaananananabbabanba-
nabananbananannanannana" 
We can see a 10th character in the above 
concatenated string is ‘n’ which is our 
final answer.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
S="abcdefg"
K=10
<strong>Output:</strong>
d
<strong>Explanation:</strong>
Concatenated string is 
"aababcabcdabcdeabcdefabcdefgbbcbcdbcdebc-
defbcdefgccdcdecdefcdefgddedefdefgeefe-
fgffgg".
We see that the 10th character is d.
so answer is d.</span>

</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>PrintKthCharacter()</strong> which takes the string S and the integer K&nbsp;as input parameters and returns the Kth character of the concatenated string formed of all sorted unique substrings.</span></p>

<p><span style="font-size:18px"><strong>Expected Time complexity:</strong>O(N<sup>2</sup>)<br>
<strong>Expected Auxillary Space:</strong>O(2*N)</span></p>

<p><strong><span style="font-size:18px">Constraints:</span></strong><br>
<span style="font-size:18px">1&lt;=|S|&lt;=1000<br>
1&lt;=K&lt;=Length of concatenated string</span></p>

<p>&nbsp;</p>
</div>