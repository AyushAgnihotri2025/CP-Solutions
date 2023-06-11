# Largest subsquare surrounded by X
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a matrix A of dimensions NxN where every element is either O or X.&nbsp;Find the largest subsquare surrounded by X.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N=2
A=[[X,X][X,X]]
<strong>Output:</strong>
2
<strong>Explanation:</strong>
The largest square submatrix 
surrounded by X is the whole 
input matrix.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N=4
A=[[X,X,X,O],[X,O,X,X],
[X,X,X,O],[X,O,X,X]]
<strong>Output:</strong>
3
<strong>Explanation:</strong>
Here,the input represents following 
matrix of size 4 x 4
X X X O
X O X X
X X X O
X O X X
The square submatrix starting at 
(0,0) and ending at (2,2) is the 
largest submatrix surrounded by X.
Therefore, size of that matrix would be 3.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>largestSubsquare()</strong> which takes the integer N and the matrix A as input parameters and returns the size of the largest subsquare surrounded by 'X'.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>O(N<sup>2</sup>)<br>
<strong>Expected Auxillary Space:</strong>O(N<sup>2</sup>)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt;=N&lt;=1000<br>
A[i][j]={'X','O'}&nbsp;</span></p>
</div>