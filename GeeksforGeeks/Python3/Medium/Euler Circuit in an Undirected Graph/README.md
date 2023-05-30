# Euler Circuit in an Undirected Graph
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Eulerian Path&nbsp;is a path in a graph that visits every edge exactly once. Eulerian Circuit is an Eulerian Path that starts and ends on the same vertex. Given the number of vertices V and adjacency list adj denoting the graph.&nbsp;Your task is to find that there exists the Euler circuit or not</span></p>
<p><span style="font-size: 18px;"><strong>Note that:&nbsp;</strong>Given graph is connected.</span><br><br><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: 
</strong></span><img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700536/Web/Other/b21c49fc-2edf-4662-b105-85f7bb2f7f30_1685086713.png" alt="">
<span style="font-size: 18px;"><strong>Output: </strong>1
<strong>Explanation: </strong>One of the Eularian circuit 
starting from vertex 0 is as follows:
0-&gt;1-&gt;3-&gt;2-&gt;0</span>
</pre>
<p>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>isEularCircuitExist()</strong>&nbsp;which takes V and adjacency list adj as input parameter and returns boolean value 1 if Eular circuit exists otherwise returns 0.</span><br>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O(V + E)<br><strong>Expected Space Complexity:&nbsp;</strong>O(V)</span><br>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= V &lt;= 10<sup>5</sup><br>1 &lt;= E &lt;= 2*10<sup>5</sup></span></p></div>