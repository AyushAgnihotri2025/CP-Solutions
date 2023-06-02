# Smallest Non-Zero Number
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>arr[]</strong> of the size <strong>N</strong>, the task is to find a number such that when the number is processed against each array element starting from the 0th index till the (n-1)-th index under the conditions given below, it never becomes negative.</span></p>

<ol>
	<li><span style="font-size:18px">If the number is greater than an array element, then it is increased by difference of the number and the array element.</span></li>
	<li><span style="font-size:18px">If the number is smaller than an array element, then it is decreased by difference of the number and the array element.</span></li>
</ol>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 5, arr[] = {3, 4, 3, 2, 4}
<strong>Output:</strong>  4
<strong>Explanation</strong>: If we process 4 from left 
to right in given array, we get following :
When processed with 3, it becomes 5.
When processed with 5, it becomes 6
When processed with 3, it becomes 9
When processed with 2, it becomes 16
When processed with 4, it becomes 28
We always get a positive number. For all 
values lower than 4, it would become 
negative for some value of the array.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 2, arr[] = {4, 4}
<strong>Output:</strong> 3
<strong>Explanation:</strong> When processed with 4, 
it becomes 2 When processed with 
next 4, it becomes 1</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong>find</strong>() that takes array<strong> A </strong>and integer<strong> N</strong> as parameters and returns the smallest possible number.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N).&nbsp;<br>
<strong>Expected Auxiliary Space:</strong> O(1).</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>6</sup></span></p>
</div>