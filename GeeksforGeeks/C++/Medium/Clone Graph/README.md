# Clone Graph
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a reference of a node in a connected&nbsp;undirected graph. Return a clone&nbsp;of the graph.<br>
Each node in the graph contains a value (Integer) and a list (List[Node]) of its neighbors.<br>
<strong>For Example :&nbsp; &nbsp;&nbsp;</strong></span></p>

<pre><span style="font-size:18px">class Node {
    public int val;
    public List neighbors;
}</span></pre>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>adjList = [[2,4],[1,3],[2,4],[1,3]]
<strong>Output: </strong>1
<strong>Explanation: </strong>The graph is cloned successfully.
</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>adjList = [[2],[1]]
<strong>Output: </strong>1
<strong>Explanation: </strong>The graph is cloned successfully.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>cloneGraph( )&nbsp;</strong>which takes a&nbsp;node will always be the first node of the graph</span><span style="font-size:18px"> as input and returns the&nbsp;<strong>copy of the given node</strong>&nbsp;as a reference to the cloned graph.</span></p>

<p><span style="font-size:18px"><strong>Note:</strong>&nbsp;After the user will returns the node of the cloned graph the system will automatically check if&nbsp;the output graph is perfectly cloned or not.The output is 1 if the graph is cloned successfully. Otherwise output is 0. You can't return a reference to the original graph you have to make a deep copy of that.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N + M).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(N).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;=Number of nodes&lt;= 100<br>
1 &lt;=Node value&lt;= 100</span><br>
&nbsp;</p>
</div>