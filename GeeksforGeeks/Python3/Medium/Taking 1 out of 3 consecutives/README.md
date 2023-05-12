# Taking 1 out of 3 consecutives
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>A</strong> consisting of <strong>N </strong><u>non-negative</u> integers your task is to&nbsp;find the minimum sum of the array such that out of 3 consecutive&nbsp; elements you need to add at-least one.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 6
A[] = {1, 2, 3, 6, 7, 1}
<strong>Output:</strong>
4
<strong>Explanation:</strong>
Moving from left to right 3+1. When 3
is added next 3 consecutive elements
be 6, 7 and 1, from which we take 1.
Which covers all subarray of lenght 3
(3+1=4).</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
2
3 2
<strong>Output:</strong>
0
<strong>Explanation:</strong>
We won't take any element as the
array length is less than 3.</span>
</pre>

<p><br>
<br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>minSum()</strong>&nbsp;which takes the array <strong>A[]</strong> and its size <strong>N</strong><strong> </strong>as inputs and returns the minimum sum that can be obtained.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space: </strong>O(N)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ a[i] ≤ 10<sup>5</sup></span></p>
</div>