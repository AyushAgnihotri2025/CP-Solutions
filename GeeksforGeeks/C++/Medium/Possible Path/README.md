# Possible Path
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an undirected graph with n vertices and connections between them. Your task is to find whether you can come to same vertex X if you start from X by traversing all the vertices atleast once and use all the paths exactly once.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>paths = {{0,1,1,1,1},{1,0,-1,1,-1},
{1,-1,0,1,-1},{1,1,1,0,1},{1,-1,-1,1,0}}
<strong>Output: </strong>1
<strong>Exaplanation: </strong>One can visit the vertices in
the following way:
1-&gt;3-&gt;4-&gt;5-&gt;1-&gt;4-&gt;2-&gt;1
Here all the vertices has been visited and all
paths are used exactly once.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>isPossible()&nbsp;</strong>which takes paths as input parameter and returns 1 if it is possible to visit all the vertices atleast once by using all the paths exactly once otherwise 0.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(n<sup>2</sup>)<br>
<strong>Expected Space Compelxity:&nbsp;</strong>O(1)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n &lt;= 100<br>
-1 &lt;= paths[i][j] &lt;= 1<br>
<strong>Note:</strong>&nbsp;If i == j then paths[i][j] = 0.&nbsp;If paths[i][j] = 1 it means there is a path between i to j. If paths[i][j] = -1 it means there is no path between i to j.</span></p>

<p>&nbsp;</p>
</div>