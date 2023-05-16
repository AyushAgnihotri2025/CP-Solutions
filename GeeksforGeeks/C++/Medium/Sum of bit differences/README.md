# Sum of bit differences
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an integer array of <strong>N</strong>&nbsp;integers, find sum of bit differences in all pairs that can be formed from array elements. Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y.<br>
For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7 is 111 (first and last bits differ in two numbers).</span></p>

<p><span style="font-size:18px"><strong>Note</strong>: (x, y) and (y, x) are considered two separate pairs.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> 
N = 2
arr[] = {1, 2}
<strong>Output:</strong> 4
<strong>Explanation</strong>: All pairs in array are (1, 1)
(1, 2), 2, 1), (2, 2)
Sum of bit differences = 0 + 2 + 2 + 0
                       = 4</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 3 
arr[] = {1, 3, 5}
<strong>Output:</strong> 8
<strong>Explanation</strong>: 
All pairs in array are (1, 1), (1, 3),
(1, 5), (3, 1), (3, 3) (3, 5),(5, 1),
(5, 3), (5, 5)
Sum of bit differences =  0 + 1 + 1 +
                          1 + 0 + 2 +
                          1 + 2 + 0 
                       = 8</span></pre>

<p><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>sumBitDifferences</strong><strong>()</strong>&nbsp;which takes the array&nbsp;<strong>arr[]</strong>&nbsp;and&nbsp;<strong>n</strong><strong>&nbsp;</strong>as inputs and returns an integer denoting&nbsp;the answer.<br>
<br>
<strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)<br>
<br>
<strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>5</sup><br>
1 &lt;= arr[i] &lt;= 10<sup>5</sup></span></p>

<p>&nbsp;</p>
</div>