# Sum-string
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string of digits, the task is to check if it is a ‘sum-string’. A string S is called a sum-string if a rightmost substring can be written as a sum of two substrings before it and the same is recursively true for substrings before it. </span></p>

<p>&nbsp;</p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">12243660
<strong>Output:</strong></span>
<span style="font-size:18px">1</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">"12243660" is a sum string. As we </span>
<span style="font-size:18px">can get, 24 + 36 = 60 &amp; 12 + 24 = 36.</span></pre>

<p>&nbsp;</p>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">1111112223</span>
<strong><span style="font-size:18px">Output:</span></strong>
<span style="font-size:18px">1</span>
<strong><span style="font-size:18px">Explanation:</span></strong>
<span style="font-size:18px">"1111112223" is a sum string. As we </span>
<span style="font-size:18px">can get, 111+112 = 223 &amp; 1+111 = 112.</span></pre>

<p>&nbsp;</p>

<p><strong><span style="font-size:18px">Your Task:</span></strong></p>

<p><span style="font-size:18px">You don't need to read input or print anything. Your task is to complete the function isSumString() which takes the string S and returns 1 is S is a sum-string otherwise returns 0.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity: </strong>O(|S|<sup>2</sup>)<br>
<strong>Expected Auxiliary Space:</strong> O(|S|)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt;=|S|&lt;=10<sup>3</sup></span></p>

<p>&nbsp;</p>
</div>