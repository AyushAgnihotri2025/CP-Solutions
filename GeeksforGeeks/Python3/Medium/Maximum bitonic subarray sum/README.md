# Maximum bitonic subarray sum
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px">Given an array containing n numbers. The task is to find the maximum sum bitonic subarray. A bitonic subarray is a subarray in which elements are first increasing and then decreasing. A strictly increasing or strictly decreasing subarray is also considered as bitonic subarray.</span></span><br>
&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Example 1:</strong></span></span></p>

<pre><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Input:</strong>
n = 7
a[] = {5, 3, 9, 2, 7, 6, 4}
<strong>Output:</strong>
19
<strong>Explanation:</strong>
All Bitonic Subarrays are as follows:
{5}, {3}, {9}, {2}, {7}, {6}, {4},
{5,3}, {3,9}, {9,2}, {2,7}, {7,6}, 
{6,4}, {3,9,2}, {2,7,6}, {7,6,4}, {2,7,6,4}.
Out of these, the one with the maximum
sum is {2,7,6,4} whose sum is 19.</span></span></pre>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Example 2:</strong></span></span></p>

<pre><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Input:</strong>
n = 7
a[] = {5, 4, 3, 2, 1, 10, 6}
<strong>Output:</strong>
17</span></span>
</pre>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>maxSumBitonicSubArr()</strong>&nbsp;which takes the array <strong>a[]</strong> and its size <strong>n</strong><strong> </strong>as inputs and returns the maximum bitonic subarray sum.</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Expected Time Complexity:</strong> O(n)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Constraints:</strong><br>
1&lt;=n&lt;=10<sup>5</sup><br>
1&lt;=a[i]&lt;=10<sup>5</sup></span></span></p>
</div>