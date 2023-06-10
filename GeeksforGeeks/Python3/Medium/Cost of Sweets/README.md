# Cost of Sweets
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Jeny love Sweets&nbsp;so much. Now she is at famous restaurant and wants to eat <strong>M</strong>&nbsp;pieces of a particular&nbsp;sweet. Cost of <strong>nth</strong>&nbsp;sweet&nbsp;can only be determined by the determinant of matrix of order&nbsp;<strong>n</strong><strong>&nbsp;x n, </strong>where n&nbsp;=&nbsp;1 to M. The (i, j)th term of matrix is given as<strong>: A[i][j]= minimum(i, j) *(-1)<sup>((i-1)*n + (j-1))</sup>.</strong><br>
Matrix indexes starts with 1. The task is to&nbsp;find the cost of M sweets.</span><br>
<br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: M = 1
<strong>Output:</strong>&nbsp;1&nbsp;
<strong>Explanation</strong>: Matrix of 1*1 is: |1|.
Determinant of matrix 1x1 = 1.
Cost of 1 sweet&nbsp;= 1.</span><span style="font-size:18px">
</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>M = 2
<strong>Output:&nbsp;</strong>0
<strong>Explanation</strong>: Matrix of 2*2 is: &nbsp;|1 -1|
&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;     |1 -2|.
Determinant of matrix 2x2= -1.
Cost of 2 sweets&nbsp; = 
Cost of 1st sweet&nbsp;+ Cost of 2nd sweet&nbsp;= 1 + -1 = 0.</span>
</pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You dont need to read input or print anything. Complete the function <strong>costOfSweets()&nbsp;</strong>which takes M&nbsp;as input parameter and returns the cost of M sweets.<br>
<br>
<strong>Expected Time Complexity:</strong> O(1)<br>
<strong>Expected Auxiliary Space:</strong> O(1)<br>
<br>
<strong>Constraints:</strong><br>
1&lt;= M &lt;=10<sup>6</sup></span></p>
</div>