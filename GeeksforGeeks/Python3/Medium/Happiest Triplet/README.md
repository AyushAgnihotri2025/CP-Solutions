# Happiest Triplet
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Three arrays of the same size are given. Find a triplet such that (maximum – minimum) in that triplet is the minimum of all the triplets. A triplet should be selected in a way such that it should have one number from each of the three given arrays. This triplet is the happiest among all the possible triplets. Print the triplet in decreasing order. If there are 2 or more smallest difference triplets, then the one with the smallest sum of its elements should be displayed.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N=3
a[] = { 5, 2, 8 }
b[] = { 10, 7, 12 }
c[] = { 9, 14, 6 }&nbsp; 
<strong>Output:</strong> 7 6 5
<strong>Explanation</strong>:
The triplet { 5,7,6&nbsp;}&nbsp; has difference
(maximum - minimum)= (7-5) =2 which is
minimum of all triplets.  </span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N=4
a[] = { 15, 12, 18, 9 }
b[] = { 10, 17, 13, 8 }
c[] = { 14, 16, 11, 5 }</span>
<span style="font-size:18px"><strong>Output:</strong> 11 10 9</span>
</pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong>smallestDifferenceTriplet</strong>() that takes <strong>array arr1 , array arr2 ,array arr3 and integer n </strong>as parameters and returns the happiest triplet in an array.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(NLogN).<br>
<strong>Expected Auxiliary Space:</strong> O(1).</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5</sup></span></p>

<p>&nbsp;</p>
</div>