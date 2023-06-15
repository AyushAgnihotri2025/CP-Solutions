# Maximum Sum Subsequence of length k
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array sequence [A1 , A2 ...An], the task is&nbsp;to find the maximum possible sum of increasing subsequence S of length K such that Si1&lt;=Si2&lt;=Si3.........&lt;=Sin.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 8 K = 3
A[] = {8 5 9 10 5 6 19 8}
<strong>Output: </strong>38
<strong>Explanation:</strong>
Possible increasing subsequence of
length 3 with maximum possible
sum is 9 10 19.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 2,K = 2
A[] = {10 5}
<strong>Output: </strong>-1
<strong>Explanation:
</strong>Can't make any increasing subsequence 
of length 2.
</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>max_sum()</strong>&nbsp;which takes sequence&nbsp;A as the first parameter&nbsp;and K as the second parameter and returns the maximum possible sum of K-length&nbsp;increasing subsequnece. If not possible return -1.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(max(Ai) * n * log(max(Ai)))<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(max(Ai))</span></p>

<p><span style="font-size:18px"><strong>Contraints:</strong><br>
1 &lt;= n &lt;= 100<br>
1 &lt;= A<sub>i</sub> &lt;= 100000</span></p>

<p>&nbsp;</p>

<p>&nbsp;</p>
</div>