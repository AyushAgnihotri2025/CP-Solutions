# Count divisors of product of array elements
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px">Given an array with N elements, the task is to find the count of factors of a number X which is product of all array elements. </span></span><br>
&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Example 1:</strong></span></span></p>

<pre><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Input:</strong>
N = 3
Arr[] = {2, 4, 6}
<strong>Output:</strong>
10
<strong>Explanation:</strong>
2 * 4 * 6 = 48, the factors of 48 are 
1, 2, 3, 4, 6, 8, 12, 16, 24, 48
whose count is 10.</span></span></pre>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Example 2:</strong></span></span></p>

<pre><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Input:</strong>
N = 3
Arr[] = {3, 5, 7}
<strong>Output:</strong>
8
<strong>Explanation:</strong>
3 * 5 * 7 = 105, the factors of 105 are 
1, 3, 5, 7, 15, 21, 35, 105 whose count is 8.</span></span></pre>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>countDivisorsMult()</strong>&nbsp;which takes the array <strong>A[]</strong> and its size <strong>N</strong><strong> </strong>as inputs and returns the count of factors of X.</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Expected Time Complexity:</strong> O(N. sqrt(N))<br>
<strong>Expected Auxiliary Space:</strong> O(N)</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Constraints:</strong><br>
2&lt;=N&lt;=10<sup>2</sup><br>
1&lt;=Arr[i]&lt;=10<sup>2</sup></span></span></p>
</div>