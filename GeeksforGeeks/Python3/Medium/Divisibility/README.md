# Divisibility
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>nums[]</strong>&nbsp;of <strong>n</strong>&nbsp;elements and a number <strong>k.</strong>&nbsp;Your task is to count the number of integers from 1 to k&nbsp;which are divisible by atleast one of the elements of nums[].</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>nums = {2, 3}, k = 10
<strong>Output: </strong>7
<strong>Explanation: </strong>The numbers from 1 to 10
which are divisible by either 2 or 3
are - 2, 3, 4, 6, 8, 9, 10</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>nums = {2}, k = 5
<strong>Output: </strong>2
<strong>Explanation: </strong>The numbers which are divisble 
by 2 from 1 to 5 are 2 and 4.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't have to read or print anyhting. Your task is to complete the function&nbsp;<strong>Count()</strong>&nbsp;which takes nums and k as input parameter and returns count of integers from 1 to k which are divisible by atleast one of the element of nums[].</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Compelxity:&nbsp;</strong>O(n&nbsp;* 2<sup>n</sup></span><span style="font-size:18px">&nbsp;* log(k))<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(1)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n &lt;= 12<br>
1 &lt;= k &lt;= 10<sup>18</sup><br>
1 &lt;= nums[i] &lt;= 20</span></p>
</div>