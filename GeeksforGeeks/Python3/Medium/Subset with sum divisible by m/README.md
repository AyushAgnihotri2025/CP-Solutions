# Subset with sum divisible by m
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a set of <strong>n</strong> non-negative&nbsp;integers, and a value <strong>m</strong>, determine if there is a subset of the given <strong>set with sum divisible by m</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: 
</strong>n = 4 m = 6 
nums[] = {3 1 7 5}
<strong>Output:
</strong>1
<strong>Explanation:
</strong>If we take the subset {7, 5} then sum
will be 12 which is divisible by 6.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n = 3, m = 5
nums[] = {1 2 6}
<strong>Output:
</strong>0
<strong>Explanation: </strong>
All possible subsets of the given set are 
{1}, {2}, {6}, {1, 2}, {2, 6}, {1, 6}
and {1, 2, 6}. There is no subset whose
sum is divisible by 5.</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>DivisibleByM()</strong>&nbsp;which takes the given set and m as input parameter and returns 1 if any of the subset(non-empty) sum is divisible by m otherwise returns 0.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(n*m)<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(n)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= elements in set &lt;= 1000<br>
1 &lt;= n, m &lt;= 1000</span></p>
</div>