# Recurrence Matrix
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Let's define a series whose recurrence formula is as follows :<br>
C(i)= 3*C(i-1) + 4*C(i-2) + 5*C(i-3) + 6*C(i-4)&nbsp;<br>
C(0)= 2<br>
C(1)= 0<br>
C(2)= 1<br>
C(3)= 7<br>
Now based on this Series a matrix&nbsp;of size n*n is to be formed.The top left cell is(1,1) and the bottom right corner is (n,n).&nbsp;<br>
Each cell (i,j) of the matrix contains either 1 or 0.&nbsp;<br>
If C( (i * j)<sup>3</sup>)is odd, matrix(i,j) is 1, otherwise, it's 0.<br>
You will be given a list of queries containing n. Your task is to count number of ones in matrix for&nbsp;each&nbsp;query.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>Queries = {2}
<strong>Output: </strong>0
<strong>Explanation: </strong>C(1,1) = C(1<sup>3</sup>*1<sup>3</sup>) = C(1) = 0
C(1,2) = C(1<sup>3</sup>*2<sup>3</sup>) = 11424
C(2,1) = C(2<sup>3</sup>*1<sup>3</sup>) = 11424
C(2,2) = C(2<sup>3</sup>*2<sup>3</sup>) = 17408414112797894176
So the matrix formed will be 
0 0 
0 0 
i,e total no. of ones = 0.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Youd don't need to read or print anyhting. Your task is to complete the function&nbsp;<strong>CountOnes()&nbsp;</strong>which takes Queries as input parameter and returns a list containing count of ones for each queries.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(n<sup>2</sup>)<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(n<sup>2</sup>)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= No. of queries &lt;= 1000<br>
1 &lt;= n &lt;= 1000</span></p>
</div>