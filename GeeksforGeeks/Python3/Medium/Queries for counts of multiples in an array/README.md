# Queries for counts of multiples in an array
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px">Given an array of positive integers and many queries for divisibility. In every query Q[i], we are given an integer K , we need to count all elements in the array which are perfectly divisible by K.</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Example 1:</strong></span></span></p>

<pre><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Input:
</strong>N = 6
A[] = { 2, 4, 9, 15, 21, 20}
M =  3
Q[] = { 2, 3, 5}
<strong>Output:</strong>
3 3 2
<strong>Explanation:</strong>
Multiples of '2' in array are:- {2, 4, 20}
Multiples of '3' in array are:- {9, 15, 21}
Multiples of '5' in array are:- {15, 20}</span>
</span></pre>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Example 2:</strong></span></span></p>

<pre><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Input:</strong>
N = 3
A[] = {3, 4, 6}
M = 2
Q[] = {2, 3}
<strong>Output:</strong>
2 2</span></span>
</pre>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>leftElement()</strong>&nbsp;which takes the array <strong>A[]</strong> and its size <strong>N</strong>, array<strong> Q[] </strong>and its size<strong> M </strong>as inputs and returns the array&nbsp;containing the required count&nbsp;for each query Q[i].</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Expected Time Complexity:</strong> O(Mx*log(Mx))<br>
<strong>Expected Auxiliary Space:</strong> O(Mx)</span><br>
<span style="font-size:16px">where Mx is the maximum value in array elements.</span></span></p>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Constraints:</strong><br>
1&lt;=N,M&lt;=10<sup>5</sup><br>
1&lt;=A[i],Q[i]&lt;=10<sup>5</sup></span></span></p>
</div>