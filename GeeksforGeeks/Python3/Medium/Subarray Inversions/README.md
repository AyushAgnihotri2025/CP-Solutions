# Subarray Inversions
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>arr[]</strong> of <strong>N</strong> integers, the task is to find the sum of the number of inversions in all subarrays of length <strong>K</strong>. To clarify, determine the number of inversions in each of the <strong>n k + 1</strong> subarrays of length k and add them together.</span></p>

<p><span style="font-size:18px">For example, if <strong>i </strong>and <strong>j </strong>are two different indices of an array <strong>arr[]</strong> such that <strong>i &lt; j</strong>&nbsp;and <strong>arr[i] &gt; arr[j]</strong>, it is an inversion.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 4, K = 3
arr[]= {1, 6, 7, 2}<strong>
Output:</strong> 2
<strong>Explanation</strong>: There are two subarrays 
of size 3, {1, 6, 7} and {6, 7, 2}. 
Count of inversions in first subarray 
is 0 and count of inversions in second 
subarray is 2. So sum is 0 + 2 = 2.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 8, K = 4<strong>
</strong>arr[]= {12, 3, 14, 8, 15, 1, 4, 22}
<strong>Output:</strong> 14 </span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong>inversion_count</strong>() that takes array <strong>a[],&nbsp;</strong>integer <strong>N, </strong>and integer<strong> K </strong>as parameters and returns the desired result.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N<sup>2</sup>).&nbsp;<br>
<strong>Expected Auxiliary Space:</strong> O(N).</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>3</sup></span></p>
</div>