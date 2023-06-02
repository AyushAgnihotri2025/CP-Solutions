# Not a subset sum
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a sorted&nbsp;array&nbsp;of N&nbsp;positive integers, find the smallest positive integer S such that S&nbsp;cannot be represented as sum of elements of any subset of the given array set.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 3
Arr[] = {1, 2, 3}
<strong>Output:</strong> 7
<strong>Explanation:</strong> 7 is the smallest positive number 
for which any subset is not present with sum 7.
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 6
Arr[] = {3, 6, 9, 10, 20, 28}
<strong>Output:</strong> 1
<strong>Explanation:</strong>&nbsp;1 is the smallest positive number
for which any subset is not present with sum 1.
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>findSmallest()</strong>&nbsp;which takes the array of integers&nbsp;<strong>arr</strong>&nbsp;and its size&nbsp;<strong>n&nbsp;</strong>as input parameters and returns an integer denoting the answer.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints</strong><br>
1 &lt;=&nbsp;N<strong> </strong>&lt;= 10<sup>6</sup><br>
0 &lt;= Arr[i] &lt;= 10<sup>15</sup></span><br>
&nbsp;</p>
</div>