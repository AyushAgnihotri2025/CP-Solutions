# Sum of subarray minimum
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>a</strong><strong>rr&nbsp;</strong>of size <strong>N</strong>&nbsp;containing&nbsp;positive integers, find the sum of <strong>min(b),</strong> where <strong>b</strong> ranges over every (contiguous) subarray of arr. Since answer may be very large, return the answer <strong>modulo 10<sup>9</sup>&nbsp;+7</strong>.&nbsp;</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<div style="--darkreader-inline-bgcolor:#222426; --darkreader-inline-bgimage:initial; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-top:#3e4446; background:#eeeeee; border:1px solid #cccccc; padding:5px 10px"><span style="font-size:18px"><strong>Input:</strong><br>
N = 4<br>
arr[ ] = {3, 1, 2, 4}<br>
<strong>Output: </strong>17<br>
<strong>Explanation:</strong> subarrays are {3}, {1}, {2}, {4}, {3, 1}, {1, 2}, {2, 4}, {3, 1, 2}, {1, 2, 4}, {3, 1, 2, 4}.<br>
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1. Sum is 17.</span><br>
&nbsp;</div>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<div style="--darkreader-inline-bgcolor:#222426; --darkreader-inline-bgimage:initial; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-top:#3e4446; background:#eeeeee; border:1px solid #cccccc; padding:5px 10px"><span style="font-size:18px"><strong>Input:</strong><br>
N = 4<br>
arr[ ] = {71, 55, 82, 55}<br>
<strong>Output: </strong>593</span></div>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>sumSubarrayMins()</strong>&nbsp;which takes the&nbsp;array of&nbsp;integers&nbsp;<strong>arr </strong>and <strong>N&nbsp;</strong>as parameters and returns a sum of <strong>min(b)</strong> over all possible non-empty subarrays of arr.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5</sup><br>
0 ≤ arr<sub>i&nbsp; </sub>≤ 10<sup>6</sup></span></p>
</div>