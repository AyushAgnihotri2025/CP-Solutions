# Minimum steps to get desired array
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Consider an array with N&nbsp;elements and value of all the elements is zero. We can perform following operations on the array.<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1. Incremental operations: Choose 1 element from the array and increment its value by 1.<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2. Doubling operation: Double the values of all the elements of array.<br>
Given an array <strong>arr[]</strong> of integers&nbsp;of size <strong>N</strong>. Print the&nbsp;smallest possible number of operations needed to change the original array containing only zeroes to arr[].</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 3
arr[] = {16, 16, 16}
<strong>Output:</strong> 7
<strong>Explanation:</strong> First apply an incremental 
operation to each element. Then apply the 
doubling operation four times. 
Total number of operations is 3+4 = 7.
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 2
arr[] = {2, 3}
<strong>Output:</strong> 4
<strong>Explanation:</strong>&nbsp;To get the target array 
from {0, 0}, we first increment both 
elements by 1 (2 operations), then double 
the array (1 operation). Finally increment 
second element (1 more operation).&nbsp;
Total number of operations is&nbsp;2+1+1 = 4.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>countMinOperations()</strong>&nbsp;which takes <strong>arr[]&nbsp;</strong>and&nbsp;<strong>n&nbsp;</strong>as input parameters and returns an integer&nbsp;denoting the answer.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N*log(max(Arr[i])))<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>4</sup><br>
1 ≤ arr[i] ≤ 5*10<sup>4</sup></span></p>

<p>&nbsp;</p>
</div>