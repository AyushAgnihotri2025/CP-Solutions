# Longest Span in two Binary Arrays
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two<strong> binary arrays</strong> arr1[] and arr2[] of same size N. Find length of the longest common span [i, j]&nbsp;where j&gt;=i such that arr1[i] + arr1[i+1] + …. + arr1[j] = arr2[i] + arr2[i+1] + …. + arr2[j].&nbsp;</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 6
Arr1[] = {0,&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;0,&nbsp;0}
Arr2[] = {1,&nbsp;0,&nbsp;1,&nbsp;0,&nbsp;0,&nbsp;1}
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest span with same
sum is from index 1 to 4 following zero 
based indexing.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything.&nbsp;Complete the function <strong>longestCommonSum()</strong>&nbsp;which takes two arrays&nbsp;<strong>arr1, arr2&nbsp;</strong>and integer&nbsp;<strong>n</strong>&nbsp;as input parameters&nbsp;and returns the length of the longest common span.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>5</sup><br>
0 &lt;= Arr1[i], Arr2[i] &lt;= 1</span></p>
</div>