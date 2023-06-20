# Arrange Balls
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">There are p&nbsp;balls of type P, q&nbsp;balls of type Q and r&nbsp;balls of type R. Using the balls we want to create a straight line such that no two balls of same type are adjacent.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>p = 2, q = 2, r = 2
<strong>Output: </strong>30
<strong>Explanation: </strong>There are 30 possible arrangements
of balls. Some of them are PQR, PRQ, PRP, PRQ,
PQR,...</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>p = 1, q = 1, r = 1
<strong>Output: </strong>6
<strong>Explanation: </strong>There are 6 possible arrangements
and these are PQR, PRQ, QPR, QRP, RPQ, RQP.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>CountWays()</strong>&nbsp;which takes count of P type balls, Q type balls and R type balls and returns total number of possible arrangements such that no two balls of same type are adjacent modulo 10<sup>9</sup>&nbsp;+ 7.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N<sup>3</sup>) where N = max(p, q, r)<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(N<sup>3</sup>)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constranits:&nbsp;</strong><br>
1 &lt;= p, q, r &lt;= 100&nbsp;</span></p>
</div>