# Smallest Subarray GCD
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an integer <strong>G</strong> and an array <strong>arr[]</strong>&nbsp;of size <strong>N</strong>, find the length of the minimum subarray whose Greatest Common Divisor equals to <strong>G</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 8
arr[] = {6, 9, 7, 10, 12, 24, 36, 27}
G = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> GCD of subarray {6,9} is 3.
GCD of subarray {24, 36, 27} is also 3,
but {6, 9} is the smallest.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 6
Arr[] = {9, 12, 15, 24, 36, 27}
G = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong>&nbsp;GCD 2 is not possible from 
any subarray from the given array.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>findSmallestSubArr()</strong>&nbsp;which takes&nbsp;<strong>arr[]</strong>,&nbsp;<strong>n</strong> and <strong>g</strong>&nbsp;as input parameters and returns length of minimum subarray. Return&nbsp;<strong>-1</strong> if no such subarray is possible.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N * (logN)<sup>2</sup>)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N * logN)&nbsp;</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;=&nbsp;N &lt;= 10<sup>4</sup><br>
1 &lt;= arr[i] &lt;= 10<sup>5</sup><br>
1 &lt;=&nbsp;G&nbsp;&lt;= 100</span></p>

<p>&nbsp;</p>
</div>