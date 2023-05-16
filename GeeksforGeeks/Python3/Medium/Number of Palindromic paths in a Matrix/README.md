# Number of Palindromic paths in a Matrix
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a <strong>matrix</strong>&nbsp;containing lower alphabetical characters only of size <strong>n*m</strong>.&nbsp;We need to count the number of palindromic paths in the given matrix.<br>
A path is defined as a sequence of cells starting from top-left cell and ending at bottom-right cell. We are allowed to move to <strong>right</strong> and <strong>down</strong> only from current cell.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>matrix = {{a,a,a,b},{b,a,a,a},{a,b,b,a}}
<strong>Output: </strong>3
<strong>Explanation: </strong>Number of palindromic paths are 3 
from top-left to bottom-right.
aaaaaa (0, 0) -&gt; (0, 1) -&gt; (1, 1) -&gt; (1, 2) -&gt; 
(1, 3) -&gt; (2, 3)    
aaaaaa (0, 0) -&gt; (0, 1) -&gt; (0, 2) -&gt; (1, 2) -&gt; 
(1, 3) -&gt; (2, 3)    
abaaba (0, 0) -&gt; (1, 0) -&gt; (1, 1) -&gt; (1, 2) -&gt; 
(2, 2) -&gt; (2, 3)</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>matrix = {{a,b},{c,d}}
<strong>Output: </strong>0
<strong>Explanation: </strong>There is no palindromic paths.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anyhting. Your task is to complete the function&nbsp;<strong>countPalindromicPaths()&nbsp;</strong>which takes the matrix as input parameter and returns the total nuumber of palindromic paths modulo 10<sup>9</sup>&nbsp;+ 7.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(n<sup>2</sup>*m<sup>2</sup>)<br>
<strong>Space Complexity:&nbsp;</strong>O(n*m)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n, m ≤ 100</span></p>
</div>