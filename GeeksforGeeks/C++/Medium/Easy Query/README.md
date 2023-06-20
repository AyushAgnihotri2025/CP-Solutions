# Easy Query
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are given an array nums&nbsp;of size n&nbsp;and q&nbsp;queries.&nbsp;Now for each query of the form l, r&nbsp;and k, output the kth smallest number in sub-array between l&nbsp;and r.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>nums = {4, 1, 2, 2, 3},
Query = {{1, 5, 2}, {3, 5, 3}}
<strong>Output: </strong>{2, 3}
<strong>Explanation: </strong>For the 1st query 2nd smallest in
[1, 5] is 2. For the 2nd query 3rd smallest in
[3, 5] is 3.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>nums = {1, 2, 3, 4, 5},
Query = {{2, 5, 1}}
<strong>Output: </strong>{2}
<strong>Explanation: </strong>The 1st smallest in [2, 5] is 2.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anyhting. Your Task is to complete the function&nbsp;<strong>FindQuery()&nbsp;</strong>which takes nums and Query as input parameter and returns a list containing kth smallest for every query.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(nlog(n))<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(n)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n &lt;= 15000<br>
1 &lt;= nums[i] &lt;= n<br>
1 &lt;= no. of queries &lt;= 10<sup>4</sup><br>
1 &lt;= l &lt;= r &lt;= n<br>
1 &lt;= k &lt;= r-l+1</span></p>
</div>