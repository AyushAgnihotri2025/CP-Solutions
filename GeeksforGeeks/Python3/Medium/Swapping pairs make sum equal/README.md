# Swapping pairs make sum equal
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two arrays of integers <strong>A[]</strong> and <strong>B[]</strong> of size <strong>N</strong> and <strong>M</strong>, the task is to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 6, M = 4
A[] = {4, 1, 2, 1, 1, 2}
B[] = (3, 6, 3, 3)
<strong>Output: </strong>1
<strong>Explanation</strong>: Sum of elements in A[] = 11
Sum of elements in B[] = 15, To get same 
sum from both arrays, we can swap following 
values: 1 from A[] and 3 from B[]</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 4, M = 4
A[] = {5, 7, 4, 6}
B[] = {1, 2, 3, 8}
<strong>Output:</strong> 1
<strong>Explanation</strong>: We can swap 6 from array 
A[] and 2 from array B[]</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong>findSwapValues</strong>() that takes array<strong> A, </strong>array<strong> B,&nbsp;</strong>integer<strong> N, </strong>and integer<strong> M&nbsp;</strong>as parameters and returns <strong>1</strong>&nbsp;if there exists any such pair otherwise returns&nbsp;<strong>-1</strong>.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(MlogM+NlogN).<br>
<strong>Expected Auxiliary Space:</strong> O(1).</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N, M ≤ 10<sup>6</sup></span></p>
</div>