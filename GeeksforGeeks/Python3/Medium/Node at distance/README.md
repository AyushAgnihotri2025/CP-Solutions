# Node at distance
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a Binary Tree and a positive integer <strong>k</strong>. The task is to count&nbsp;all distinct nodes that are distance k from a leaf node.&nbsp;A node is at k distance from a leaf if it is present k levels above the leaf and also, is a direct ancestor of this leaf node. If k is more than the height of Binary Tree, then nothing should be counted.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>        1
&nbsp;     /   \
&nbsp;    2     3
&nbsp;  /  \   /  \
&nbsp; 4   5  6    7
&nbsp;         \ 
&nbsp;         8
K = 2
<strong>Output: </strong>2<strong>
Explanation: </strong>There are only two unique
nodes that are at a distance of 2 units
from the leaf node.&nbsp;(node 3 for leaf
with value 8 and node 1 for leaves with
values 4, 5 and 7)
Note that node 2
isn't considered for leaf with value
8 because it isn't a direct ancestor
of node 8.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>          1
&nbsp;        /
&nbsp;       3
&nbsp;      /
&nbsp;     5
&nbsp;   /  \
&nbsp;  7    8
         \
&nbsp;         9
K = 4
<strong>Output: </strong>1<strong>
Explanation: </strong>Only one node is there
which is at a distance of 4 units
from the leaf node.(node 1 for leaf
with value 9)&nbsp;</span></pre>

<p><strong><span style="font-size:18px">Your Task:</span></strong><br>
<span style="font-size:18px">You don't have to read&nbsp;input or print anything. Complete the function <strong>printKDistantfromLeaf()&nbsp;</strong>that takes <strong>root node </strong>and<strong> k </strong>as inputs and <strong>returns </strong>the number of nodes that are at distance k from a leaf node. Any such node should be counted only once. For example, if a node is at a distance k from 2 or more leaf nodes, then it would add only 1 to our count.</span></p>

<p dir="ltr"><span style="font-size:18px"><strong>Expected Time Complexity: </strong>O(N).<br>
<strong>Expected Auxiliary Space: </strong>O(Height of the Tree).</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>5</sup></span></p>
</div>