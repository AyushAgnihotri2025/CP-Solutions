# Smallest Divisor
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are given an array of integers nums and an integer K, your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it, the sum of the division's result is less than or equal to the given integer K.<br>
Each result of the division is rounded to the nearest integer greater than or equal to that element. For Example: 7/3 = 3.</span></p>

<pre><span style="font-size:18px"><strong>Example:</strong>
<strong>Input: </strong>
A = [1 2 5 9]
6
<strong>Output:</strong>
5
<strong>Explanation:</strong>
If the divisor is 5 the sum will be 5 (1+1+1+2), which is less than 6.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
Complete the function int smallestDivisor(), which takes a vector nums and an integer K and returns the smallest integer as asked.<br>
<strong>Expected Time Complexity:</strong> O(nlogn).<br>
<strong>Expected Auxiliary Space:</strong> O(n).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= nums.length &lt;= 5 * 10<sup>5</sup><br>
1 &lt;= nums[i] &lt;= 10<sup>9</sup><br>
nums.length &lt;= K &lt;= 10<sup>6</sup></span></p>

<p><br>
&nbsp;</p>
</div>