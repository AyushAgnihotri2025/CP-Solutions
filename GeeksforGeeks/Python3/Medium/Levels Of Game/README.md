# Levels Of Game
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are playing a game. At each level of the game, you have to choose one of the roads to go to the next level. Initially, you have h amount of health and m&nbsp;amount of money.<br>
If you take the first road then health decreases by 20 and money increase by 5.&nbsp;If you take the second road then your health decreases by 5 and money decrease by 10. If you take the third&nbsp;road then your health increases by 3&nbsp;and money increase by 2.<br>
You have to tell what is the maximum level you can reach up to under the constraints that in no two consecutive levels you can select the same road twice and once your health or money becomes &lt;= 0 game ends(that level is not counted).</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
H=2
M=10
<strong>Output:</strong>
1
<strong>Explanation:</strong>
For the first level, we can only choose the third road.
Now we cannot move ahead anymore.</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
H=20
M=8
<strong>Output:</strong>
5
<strong>Explanation:</strong>
Go like this:- R3(23,10)-&gt;R1(3,15)-&gt;R3(6,17)-&gt;
R2(1,7)-&gt;R3(4,9)-&gt; game ends as we cannot choose
any more roads.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>maxLevel()</strong>&nbsp;which takes in the health and the money as input and returns the maximum level that can be reached by you.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N*N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N*N)</span><br>
<br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= H,M&lt;=800.&nbsp;</span></p>
</div>