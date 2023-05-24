# Possible paths
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a directed graph and two vertices <strong>‘u’</strong> and <strong>‘v’</strong> in it. Find the number of possible walks from <strong>‘u’</strong> to <strong>‘v’</strong> with exactly <strong>k</strong> edges on the walk modulo 10<sup>9</sup>+7.</span></p>

<p><span style="font-size:18px"><strong>Note :&nbsp;</strong>There can be a cycle in the graph and an edge can be travelled multiple times.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input 1: </strong>graph = {{0,1,1,1},{0,0,0,1}, 
{0,0,0,1}, {0,0,0,0}}, u = 0, v = 3, k = 2
<strong>Output: </strong>2
<strong>Explanation: </strong>Let source ‘u’ be vertex 0, 
destination ‘v’ be 3 and k be 2. The output 
should be 2 as there are two walk from 0 to 
3 with exactly 2 edges. The walks are {0, 2, 3}
and {0, 1, 3}.</span>
<img alt="" src="http://d1hyf4ir1gqw6c.cloudfront.net/wp-content/uploads/graph1.png">
</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>MinimumWalk()&nbsp;</strong>which takes graph, u, v and k as input parameter and returns total possible paths from u to v using exactly k edges modulo 10<sup>9</sup>+7.</span><br>
<span style="font-size:18px"><strong>Note:&nbsp;</strong>In graph, if graph[i][j] = 1, it means there is an directed edge from vertex i to j.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(n<sup>3</sup>)<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(n<sup>3</sup>)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n ≤ 50<br>
1 ≤ k ≤ n<br>
0 ≤ u, v ≤ n-1</span></p>
</div>