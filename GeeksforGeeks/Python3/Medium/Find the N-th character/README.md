# Find the N-th character
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a binary string <strong>S</strong> . Perform <strong>R</strong> iterations on string S, where in each iteration <strong>0 becomes 01</strong> and <strong>1 becomes 10</strong>. Find the <strong>N</strong>th character (considering <strong>0 based indexing</strong>) of the string after performing these R iterations. (See Examples for better understanding)</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>:
S = 101
R = 2 
N = 3
<strong>Output</strong>:
1
<strong>Explanation </strong>: 
After 1st iteration S becomes 100110.
After 2nd iteration, S = 100<strong>1</strong>01101001
Now, we can clearly see that the character
at 3rd index is 1, and so the output.</span>
</pre>

<p><span style="font-size:18px"><strong>Example</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>:
S = 11
R = 1 
N = 3
<strong>Output</strong>:
0
<strong>Explanation</strong>: 
After 1st iteration S becomes 101<strong>0</strong>.
Now, we can clearly see that the character
at 3rd index is 0, and so the output.</span></pre>

<div><br>
<span style="font-size:18px"><strong>Your task:</strong></span></div>

<div><span style="font-size:18px">You don't need to read input or print anything. Your task is to complete the function <strong>nthCharacter()</strong> which takes the string <strong>S</strong> and integers <strong>R</strong> and <strong>N</strong> as input parameters and returns the N-th character of the string after performing R operations on S.</span></div>

<div>&nbsp;</div>

<div><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(r*len(s))</span></div>

<div><span style="font-size:18px"><strong>Expected Auxilary Space:</strong> O(len(s))</span></div>

<div><br>
<span style="font-size:18px"><strong>Constraints</strong>: </span><br>
<span style="font-size:18px">1 ≤ String length ≤ 10<sup>3</sup></span><br>
<span style="font-size:18px">1 ≤ R ≤ 20</span><br>
<span style="font-size:18px">0 ≤ N &lt; Length of final string</span></div>
</div>