# Find shortest safe route in a matrix
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a path in the form of a rectangular matrix having few landmines arbitrarily placed (marked as 0), calculate length of the shortest safe route possible from any cell in the first column to any cell in the last column of the matrix. We have to avoid landmines and their four adjacent cells (left, right, above and below) as they are also unsafe. We are allowed to move to only adjacent cells which are not landmines. i.e. the route cannot contains any diagonal moves.</span></p>

<p>&nbsp;</p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">[1 0 1 1 1]
[1 1 1 1 1]
[1 1 1 1 1]
[1 1 1 0 1]
[1 1 1 1 0]</span>
<strong><span style="font-size:18px">Output: 6</span></strong>
<strong><span style="font-size:18px">Explanation: </span></strong>
<span style="font-size:18px">We can see that length of shortest</span>
<span style="font-size:18px">safe route is 13 (Highlighted in <strong>Bold</strong>).</span>
<span style="font-size:18px">[1 0 1 1 1]
[1 1 <strong><em>1 1 1</em></strong>] 
[<em><strong>1 1 1</strong></em> 1 1]
[1 1 1 0 1] 
[1 1 1 1 0]</span>
</pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong><span style="font-size:18px">
[1 1 1 1 1]
[1 1 0 1 1]
[1 1 1 1 1]</span><strong><span style="font-size:18px">
Output: </span></strong><span style="font-size:18px">-1</span><strong><span style="font-size:18px">
Explanation: </span></strong><span style="font-size:18px">There is no possible path from
first column to last column.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>findShortestPath()&nbsp;</strong>which takes matrix as input parameter and return an integer denoting the shortest path. If there&nbsp;is no possible path, return -1.&nbsp;<br>
<br>
<strong>Expected Time Complexity:</strong>&nbsp;O(R&nbsp;* C)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)<br>
<br>
<strong>Constraints:</strong><br>
1 &lt;= R,C&nbsp;&lt;= 10</span><sup><span style="font-size:15px">3</span></sup></p>
</div>