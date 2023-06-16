# Numbers with alternative 1's
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a number n, the task is to find all 1 to n bit numbers with no consecutive 1's in their binary representation. </span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>n = 3
<strong>Output: </strong>1 2 4 5
<strong>Explanation: </strong>All numbers upto 2 bit are:
1 - 1
2 - 10
3 - 11
4 - 100
5 - 101
6 - 110
7 - 111
Here 3, 6 and 7 have consecutive 1's in their 
binary representation. </span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>n = 2
<strong>Output: </strong>1 2 
<strong>Explanation: </strong>All numbers upto 2 bit are:
1 - 1
2 - 10
3 - 11
Here 3 has consecutive 1's in it's
binary representation.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anything.Your task is to complete the function&nbsp;<strong>numberWithNoConsecutiveOnes()&nbsp;</strong>which takes n as input parameter and returns a list of numbers in increasing order which do not contains 1's in their binary reperesentation.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(2<sup>n</sup>)<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(n)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n &lt;= 20</span></p>
</div>