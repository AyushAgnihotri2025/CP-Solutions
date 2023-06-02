# Find the element at given index
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>Arr[]</strong> of <strong>N</strong> elements. Perform <strong>K</strong> right circular rotations on given ranges [<strong>L...R</strong>]. After performing these rotations, we need to find element at a given index <strong>X</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 5, X = 1, K = 2
Arr[] = {1, 2, 3, 4, 5}
Ranges[][] = {{0, 2}, {0, 3}}
<strong>Output:</strong> 3
<strong>Explanation:</strong> Rotating the elements in range 
0-2 and 0-3, we have array as 4 3 1 2 5. 
Element at first position is 3.
</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 3, X = 2, K = 1
Arr[] = {1, 2, 3}
Ranges[][] = {{0, 1}}
<strong>Output:</strong> 3
</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>findElement()</strong>&nbsp;which takes the array of integers&nbsp;<strong>arr, n, x, ranges</strong>&nbsp;and&nbsp;<strong>k&nbsp;</strong>as parameters and returns an integer&nbsp;denoting the answer.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(K)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
2 &lt;= N&nbsp;&lt;= 10<sup>5</sup><br>
1 &lt;= Arr[i] &lt;= 10<sup>5</sup><br>
1 &lt;= K &lt;= 10<sup>5</sup><br>
X &lt; N<br>
0 &lt;= L &lt;= R</span></p>

<p>&nbsp;</p>
</div>