# Convert Level Order Traversal to BST
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array of size <strong>N</strong> containing level order traversal of a <strong>BST</strong>. The task is to complete the function <strong>constructBst()</strong>, that construct the BST (Binary Search Tree) from its given level order traversal.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 9
BST[] = {7,4,12,3,6,8,1,5,10}
<strong>Output: </strong>7 4 3 1 6 5 12 8 10<strong>
Explanation: </strong>After constructing BST, the
preorder traversal of BST is
7 4 3 1 6 5 12 8 10.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 6
BST[] = {1,3,4,6,7,8}
<strong>Output: </strong>1 3 4 6 7 8<strong>
Explanation: </strong>After constructing BST, the
preorder traversal of BST is 1 3 4 6 7 8.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Your task is to complete the function <strong>constructBst</strong>() which has two arguments, first as the array containing level order traversal of BST and next argument as the length of array which return the root of the newly constructed BST. The preorder traversal of the tree is printed by the driver's code.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N)<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(N).</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>3</sup></span></p>
</div>