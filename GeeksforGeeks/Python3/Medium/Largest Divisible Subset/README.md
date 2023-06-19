# Largest Divisible Subset
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a set of&nbsp;<strong>distinct</strong>&nbsp;positive integers&nbsp;<code>nums</code>, return the largest subset&nbsp;<code>answer</code>&nbsp;such that every pair&nbsp;<code>(answer[i], answer[j])</code>&nbsp;of elements in this subset satisfies:</span></p>

<ul>
	<li><span style="font-size:18px"><code>answer[i] % answer[j] == 0</code>, or</span></li>
	<li><span style="font-size:18px"><code>answer[j] % answer[i] == 0</code></span></li>
</ul>

<p><span style="font-size:18px">If there are multiple sequences with the largest size, return any of them.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:
</span></strong><span style="font-size:18px">n = 3<strong><span style="font-size:18px">
</span></strong>arr = [1,2,3]
<strong>Output:</strong>
[1,2]</span><span style="font-size:18px">
<strong>Explanation:
</strong>Largest Divisble Subset is [1,2].</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input</span></strong>:
<span style="font-size:18px">n = 4<strong><span style="font-size:18px">
</span></strong>arr = [1,2,4,8]
<strong>Output:
</strong>[1,2,4,8]</span></pre>

<p><strong><span style="font-size:18px">Your Task:</span></strong><br>
<span style="font-size:18px">You don't have to read input or print anything. Your task is to complete the function&nbsp;<strong>LargestSubset()&nbsp;</strong>which takes the integer&nbsp;<strong>n</strong>&nbsp;and array <strong>arr</strong> and returns the Largest Divisible Subset.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity: </strong>O(n<sup>2</sup>)<br>
<strong>Expected Space Complexity: </strong>O(n<sup>2</sup>)</span></p>

<p><strong><span style="font-size:18px">Constraint:</span></strong><br>
<span style="font-size:18px">1 &lt;= n &lt;= 1000<br>
1&nbsp; &lt;= arr[i] &lt;= 2 * 10<sup>9</sup></span></p>
</div>