# Series with largest GCD and sum equals to N
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an integer N, the task is to find out&nbsp;M increasing numbers such that the sum of M numbers is equal to N and the GCD of these M numbers is maximum among all possible combinations (or series) of M numbers.</span></p>

<p><span style="font-size:18px"><strong>Note: </strong>If two or more such series are possible then return&nbsp;the series which has smallest first term.<br>
<br>
<strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: N = 24, M = 3
<strong>Output:</strong>&nbsp;4 8 12
<strong>Explanation</strong>: (3, 6, 15) is also a series 
of M numbers which sums to N, but gcd = 3
(4, 8, 12) has gcd = 4 which is the maximum
possible.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 6, M = 4
<strong>Output:&nbsp;</strong>-1
<strong>Explanation</strong>: It is not possible as the 
least GCD sequence will be 1+2+3+4 which
is greater then n, hence print -1.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You dont need to read input or print anything. Complete the function <strong>M_sequence()&nbsp;</strong>which takes N&nbsp;and M&nbsp;as input parameter and returns th series of M&nbsp;numbers&nbsp;and if there are no series&nbsp;exist returns -1.<br>
<br>
<strong>Expected Time Complexity:</strong> O(sqrt(n))<br>
<strong>Expected Auxiliary Space:</strong> O(n)<br>
<br>
<strong>Constraints:</strong><br>
1 &lt;= N&nbsp;&lt;=10<sup>5</sup></span></p>
</div>