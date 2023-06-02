# Maximum length Bitonic Subarray
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>Arr[0 … N-1]</strong> containing <strong>N</strong>&nbsp;positive integers, a subarray <strong>Arr[i … j]</strong> is bitonic if there is a <strong>k</strong> with <strong>i &lt;= k &lt;= j</strong> such that <strong>A[i] &lt;= Arr[i+1] &lt;= ... &lt;= Arr[k] &gt;= Arr[k+1]&nbsp;&gt;= ... A[j – 1] &gt;= A[j]</strong>.&nbsp;Write a function that takes an array and array length&nbsp;as arguments and returns the length of the maximum length bitonic subarray.</span></p>

<p><span style="font-size:18px">For Example: In array {20, 4, 1, 2, 3, 4, 2, 10}&nbsp;the maximum length bitonic subarray is {1, 2, 3, 4, 2} which is of length 5.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 6
Arr[] = {12, 4, 78, 90, 45, 23}
<strong>Output:</strong> 5
<strong>Explanation:</strong> In the given array, 
bitonic subarray is 4 &lt;= 78 &lt;= 90
&gt;= 45 &gt;= 23.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 4
Arr[] = {10, 20, 30, 40}
<strong>Output:</strong> 4
<strong>Explanation:</strong>&nbsp;In the given array, 
bitonic subarray is 10 &lt;= 20 &lt;=
30 &lt;= 40.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>bitonic()</strong>&nbsp;which takes the&nbsp;array of&nbsp;integers&nbsp;<strong>arr </strong>and&nbsp;<strong>n</strong><strong>&nbsp;</strong>as parameters and returns an integer denoting the answer.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ Arr[i] ≤ 10<sup>6</sup></span><br>
&nbsp;</p>
</div>