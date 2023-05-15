# Find the string in grid
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a 2D grid&nbsp;of n*m of characters and a word, find all occurrences of given word in grid. A word can be matched in all 8 directions at any point. Word is said to be found in a direction if all characters match in this direction (not in zig-zag form). The 8 directions are, horizontally left, horizontally right, vertically up, vertically down, and 4 diagonal directions.<br>
<br>
<strong>Note:</strong> The returning list should be lexicographically smallest. If the word can be found in multiple directions starting from the same coordinates, the list should contain the coordinates only once.&nbsp;</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>grid = {{a,b,c},{d,r,f},{g,h,i}},
word = "abc"
<strong>Output: </strong>{{0,0}}
<strong>Explanation: </strong>From (0,0) one can find "abc"
in horizontally right direction.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>grid = {{a,b,a,b},{a,b,e,b},{e,b,e,b}}
,word = "abe"
<strong>Output: </strong>{{0,0},{0,2},{1,0}}
<strong>Explanation: </strong>From (0,0) one can find "abe" in 
right-down diagonal. From (0,2) one can
find "abe" in left-down diagonal. From
(1,0) one can find "abe" in Horizontally right 
direction.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anything, Your task is to complete the function&nbsp;<strong>searchWord()&nbsp;</strong>which takes grid and word as input parameters and returns a list containing the positions from where the word originates&nbsp;in any direction. If there is no such position then returns an&nbsp;empty&nbsp;list.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(n*m*k) where k is constant<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(1)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n &lt;= m &lt;= 100<br>
1 &lt;= |word| &lt;= 10</span></p>
</div>