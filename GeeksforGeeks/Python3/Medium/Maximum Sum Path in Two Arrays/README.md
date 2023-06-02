# Maximum Sum Path in Two Arrays
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two sorted arrays such the arrays may have some common elements. Find the sum of the maximum sum path to reach from beginning of any array to end of any of the two arrays. You&nbsp;can start from any array and&nbsp;switch from one array to another array&nbsp;only at common elements.&nbsp;</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>M = 5, N = 4
Arr1[] = {2, 3, 7, 10, 12}
Arr2[] = {1, 5, 7, 8}
<strong>Output: </strong>35
<strong>Explanation:</strong> 35 is sum of 1 + 5 + <strong>7</strong> + 10 +
12. We start from the first element of
Arr2 which is 1, then we move to 5, then 7
From 7, we switch to Arr1 (as 7 is common)
and traverse 10 and 12.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>M = 2, N = 3
Arr1[] = {10, 12}
Arr2[] = {5, 7, 9}
<strong>Output:</strong> 22
<strong>Explanation:</strong>&nbsp;22 is the sum of 10 and 12.
Since there is no common element, we need
to take all elements from the array with
more sum.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>maxPathSum()</strong>&nbsp;which takes two&nbsp;arrays of&nbsp;integers&nbsp;<strong>arr1, arr2,&nbsp;m</strong> and <strong>n&nbsp;</strong>as parameters and returns an integer&nbsp;denoting the answer.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(M+N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= M, N&nbsp;&lt;= 10<sup>5</sup><br>
0 &lt;= Arr1[i], Arr2[i] &lt;= 10<sup>6</sup></span></p>

<p>&nbsp;</p>
</div>