# Restricted Pacman
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">In the game of Restricted Pacman, an infinite linear path is given. Pacman has to start at position 0 and eat as many candies as possible. In one move he can only jump a distance of either <strong>M</strong> or <strong>N</strong>. &nbsp;If <strong>M</strong> and <strong>N</strong> are coprime numbers, find how many candies will be left on the board after the game is over.<br>
<strong>Note:</strong> The result is always finite as after a point <strong>X</strong> every index in the infinite path can be visited.&nbsp;</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>M = 2, N = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> From index 0, the indices that 
can be visited are
0 + 2 = 2
0 + 2 + 2 = 4
0 + 5 = 5
0 + 2 + 2 + 2 = 6
0 + 2 + 5 = 7
0 + 2 + 2 + 2 + 2 = 8
0 + 2 + 2 + 5 = 9
0 + 5 + 5 = 10
and so on.
1 and 3 are the only indices that cannot be 
visited. Therefore the candies at these two 
positions will be left on the board.&nbsp;</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: M</strong> = 2, N = 7
<strong>Output:</strong> 3 </span>
</pre>

<p><span style="font-size:18px"><strong>Example 3:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: M</strong> = 25, N = 7
<strong>Output:</strong> 72</span></pre>

<p><span style="font-size:18px"><strong>Your Task: </strong>&nbsp;<br>
You don't need to read input or print anything. Complete the function <strong>candies()</strong> which take M&nbsp;and N&nbsp;as input parameters and return the answer.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space:</strong> O(N)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;&nbsp;M, N&nbsp;≤ 500</span></p>
</div>