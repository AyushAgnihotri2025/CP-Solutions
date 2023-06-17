# Modify array to maximize sum of adjacent differences
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>arr</strong> of size <strong>N</strong>, the task is to modify values of this array in such a way that the sum of absolute differences between two consecutive elements is maximized. If the value of an array element is X, then we can change it to either 1 or X. Find the maximum possible value of the sum of absolute differences between two consecutive elements</span>.</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: N = 4, arr[] = [3, 2, 1, 4, 5]
<strong>Output:</strong> 8</span>
<span style="font-size:18px"><strong>Explanation</strong>: We can modify above array as
arr[] = [3, 1, 1, 4, 1]
Sum of differences = 
|1-3| + |1-1| + |4-1| + |1-4| = 8
Which is the maximum obtainable value 
among all choices of modification.</span></pre>

<div><span style="font-size:18px"><strong>Example 2:</strong></span></div>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 2, arr[] = {1, 5}
<strong>Output: </strong>4
<strong>Explanation</strong>: No modification required</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Complete the function <strong><code>maximumDifferenceSum</code>()&nbsp;</strong>which takes <strong>N</strong> and array <strong>arr </strong>as input parameters and returns the integer value<br>
<br>
<strong>Expected Time Complexity:</strong> O(<strong>N</strong>)<br>
<strong>Expected Auxiliary Space:</strong> O(<strong>N</strong>)<br>
<br>
<strong>Constraints:</strong><br>
1 ≤&nbsp;<strong>N</strong> ≤ 10<sup>5</sup></span></p>
</div>