# Euler circuit and Path
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Eulerian Path is a path in graph that visits every edge exactly once. Eulerian Circuit is an Eulerian Path which starts and ends on the same vertex.&nbsp;The task is to find that there exists the Euler Path or circuit or none in given undirected graph with <strong>V </strong>vertices and adjacency list <strong>adj.</strong><br><br><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: 
</strong></span><img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700537/Web/Other/c191d733-5295-4e4a-81b7-7a1de77ec269_1685086734.png" alt="">
<strong><span style="font-size: 18px;">Output: </span></strong><span style="font-size: 18px;">2
<strong>Explanation: </strong>The graph contains Eulerian circuit</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>
</span><img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700537/Web/Other/c5419f69-5051-4865-aabe-4898ff1c92f3_1685086735.png" alt="">
<strong><span style="font-size: 18px;">Output: </span></strong><span style="font-size: 18px;">1
<strong>Explanation: </strong>The graph contains Eulerian path.</span>
</pre>
<p>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read or print anything. Your task is to complete the function <strong>isEulerCircuilt()&nbsp;</strong>which takes number of vertices in the graph denoting as V and adjacency list of graph denoting as adj and returns 1 if graph contains Eulerian Path, 2 if graph contains Eulerian Circuit 0 otherwise.</span><br>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O(V+E) where E is the number of edges in graph.<br><strong>Expected Space Complexity:&nbsp;</strong>O(V)</span><br>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ V, E ≤ 10<sup>4</sup></span></p></div>