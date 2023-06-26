# Partition Array for Maximum Sum
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an integer array&nbsp;<strong><code>arr</code></strong>, partition the array into (contiguous) subarrays of length&nbsp;<strong>at most</strong>&nbsp;<strong><code>k</code></strong>. After partitioning, each subarray has their values changed to become the maximum value of that subarray.&nbsp;Return&nbsp;the largest sum of the given array after partitioning.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n = 7
k = 3
arr = [1,15,7,9,2,5,10]
<strong>Output:</strong>
84
<strong>Explanation:</strong>
arr becomes [15,15,15,9,10,10,10]</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n = 1
k = 1
arr = [1]
<strong>Output:</strong>
1</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong></span><br>
<span style="font-size:18px">You don't have to read input or print anything. Your task is to complete the function&nbsp;<strong>Solve()&nbsp;</strong>which takes the integer&nbsp;<strong>n</strong>&nbsp;and array&nbsp;<strong>arr and </strong>integer<strong> k</strong>&nbsp;and returns the Largest Sum of the Array after Partitioning.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity</strong>: O(n<sup>2</sup>)<br>
<strong>Expected Space Complexity:</strong> O(n)</span></p>

<p><span style="font-size:18px"><strong>Constraint:</strong><br>
1 &lt;= n &lt;= 500<br>
0 &lt;= arr[i] &lt;= 10<sup>9</sup><br>
1 &lt;= k &lt;= n</span></p>
</div>