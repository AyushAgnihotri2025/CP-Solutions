# Find all distinct subset (or subsequence) sums
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a set of integers, find all distinct sums that can be generated from the subsets of the given sets.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>nums = {1,2}
<strong>Output: </strong>{0,1,2,3}
<strong>Explanation: </strong>Four distinct sums can be
calculated which are 0, 1, 2 and 3.
0 if we do not choose any number.
1 if we choose only 1.
2 if we choose only 2.
3 if we choose 1 and 2.</span>

</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>nums = {1,2,3}
<strong>Output: </strong>{0,1,2,3,4,5,6}
<strong>Explanation: </strong>Seven distinct sum can be calculated
which are 0, 1, 2, 3, 4, 5 and 6.
0 if we do not choose any number.
1 if we choose only 1.
2 if we choose only 2.
3 if we choose only 3.
4 if we choose 1 and 3.
5 if we choose 2 and 3.
6 if we choose 1, 2 and 3.</span>

</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>DistinictSum()&nbsp;</strong>which takes nums as input parameter and returns a list containing the distinict sum in increasing order,</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(n * sum) where sum = sum of all elements of nums.<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(n * sum)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= length of nums &lt;= 10<sup>2</sup></span><br>
<span style="font-size:18px">1 &lt;= nums[i] &lt;= 10</span><sup>2</sup></p>
</div>