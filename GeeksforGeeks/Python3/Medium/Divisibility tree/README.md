# Divisibility tree
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a tree with n nodes and edge connection between them . The tree is rooted at node 1.&nbsp;Your task is to remove minimum number of edges from the given tree such that the tree converts into disjoint union tree&nbsp;so that nodes of connected component left is divisible by 2.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>n = 10, edges = {{2,1},{3,1},{4,3},{5,2}
,{6,1},{7,2},{8,6},{9,8},{10,8}}
<strong>Output: </strong>2
<strong>Explanation: </strong>Take two integers at a time i.e. 2 
is connected with 1, 3 is connected with 1,4 is 
connected with 3, 5 is connected with 2 and so 
on. Fig will understand you better.
Original tree:
</span><img src="https://contribute.geeksforgeeks.org/wp-content/uploads/1466090203-2e0cf4f1be-even.png"><span style="font-size:18px">&nbsp;&nbsp;&nbsp;
After removing edge 1-3 and 1-6. So ans is 2
because all nodes are even
</span><img src="https://contribute.geeksforgeeks.org/wp-content/uploads/image1-1.png">
</pre>

<p>&nbsp;</p>

<p><strong><span style="font-size:18px">Your Task:</span></strong><br>
<span style="font-size:18px">You don't need to read or print anyhting. Your task is to complete the function&nbsp;<strong>minimumEdgeRemove()&nbsp;</strong>which takes n and edges as input parameter and returns the minimum number of edges which is removed to make the tree disjoint union tree&nbsp;such that the tree converts into disjoint union tree&nbsp;so that nodes of connected component left is divisible by 2.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Compelxity:&nbsp;</strong>O(n)<br>
<strong>Expected Space Comeplxity:&nbsp;</strong>O(1)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n &lt;= 10<sup>4</sup></span></p>
</div>