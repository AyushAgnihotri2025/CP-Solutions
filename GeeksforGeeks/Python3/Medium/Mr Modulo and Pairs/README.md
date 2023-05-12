# Mr Modulo and Pairs
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Mr. Modulo comes up with another problem related to modulo and this time he is interested in finding all the possible pairs a&nbsp;and b in&nbsp;the array arr[] such that a&nbsp;% b = k where k is a given integer. The array given&nbsp;will have distinct elements.<br>
You are required to print how many such pairs exist.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N=5, K=3
arr[] = {2, 3, 5, 4, 7}
<strong>Output:</strong> 4
<strong>Explanation</strong>:
The pairs are -: 
7 % 4 = 3
3 % 4 = 3
3 % 5 = 3
3 % 7 = 3</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N=2, K=3
arr[] = {1, 2} 
<strong>Output:</strong> 0
</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong>printPairs</strong>() that takes <strong>array arr, integer n and integer k</strong>&nbsp;as parameters and return the&nbsp;total number of such pairs in the array.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> &nbsp;O(N* sqrt(max)) where max is the maximum element in the array.<br>
<strong>Expected Auxiliary Space: </strong>O(N).</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>4</sup></span></p>

<p>&nbsp;</p>
</div>