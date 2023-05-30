# Detect Cycle using DSU
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an undirected&nbsp;graph with <strong>V</strong> nodes and <strong>E</strong>&nbsp;edges. The task is to check if there is any cycle in undirected graph.<br><strong>Note:&nbsp;</strong>Solve the problem using disjoint set union(dsu).</span><br>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: 
</strong></span><img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/701410/Web/Other/f496602b-dcfb-4de5-bdf6-0c51462af952_1685087018.png" alt="">
<span style="font-size: 18px;"><strong>Output:</strong><strong>&nbsp;</strong>1
<strong>Explanation: </strong>There is a cycle between 0-&gt;2-&gt;4-&gt;0</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: 
</strong></span><img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/701410/Web/Other/ca19a9ca-7f9f-4c36-98cc-e678c1076ffd_1685087019.png" alt="">
<span style="font-size: 18px;"><strong>Output: </strong>0
<strong>Explanation: </strong>The graph doesn't contain any cycle</span>
</pre>
<p>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read or print anyhting. Your task is to complete the function&nbsp;<strong>detectCycle()&nbsp;</strong>which takes number of vertices in the graph denoting as V and adjacency list denoting as adj and returns 1 if&nbsp;graph contains any cycle otherwise returns 0.<br><br><strong>Expected Time Complexity:</strong>&nbsp;O(V + E)<br><strong>Expected Space Complexity:&nbsp;</strong>O(V)</span><br>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ V, E ≤ 10<sup>4</sup></span></p></div>