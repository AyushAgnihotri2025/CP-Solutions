# Money Distributions
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Find the number of ways in which <strong>N</strong> coins can be distributed among <strong>K</strong> pupils such that each pupil receives at least one coin each.&nbsp;Two distributions are said to be different only if they have at least one pupil who got a different number of coins.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 7, K = 3
<strong>Output: </strong>15
<strong>Explanation: 
</strong>Coin distribution can be any of the following 15 ways. 
{1,1,5}, {1,5,1}, {5,1,1}, {2,1,4}, {1,2,4}, {1,4,2}
{2,4,1}, {4,1,2}, {4,2,1}, {3,1,3}, {1,3,3}, {3,3,1}
{2,2,3}, {2,3,2}, {3,2,2}
</span>

</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 5, K = 5
<strong>Output: </strong>1
<strong>Explanation: </strong>{1, 1, 1, 1, 1} is the only way.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong></span><br>
<span style="font-size:18px">You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>totalWays()</strong>&nbsp;which takes N&nbsp;and K&nbsp;as input parameters and returns the number of possible distributions&nbsp;modulo 10^9+7<strong>.</strong></span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N)<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(N)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N, K&nbsp;&lt;= 100000</span></p>
</div>