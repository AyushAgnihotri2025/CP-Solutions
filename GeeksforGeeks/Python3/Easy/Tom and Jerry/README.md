# Tom and Jerry
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Tom and Jerry being bored in this pandemic, decides to play a game. Given an&nbsp;<strong>integer N</strong>. On each player's turn, that player makes a move by&nbsp;<strong>subtracting a divisor of current N</strong>&nbsp;(which is less than N) from current N, thus&nbsp;<strong>forming a new N for the next turn</strong>.&nbsp;</span><span style="font-size:18px">The player who does not have any divisor left to subtract loses the game.</span></p>

<p><span style="font-size:18px">The game begins with Tom playing the first move. Both Tom and Jerry play optimally. The task is to determine who wins the game. Return&nbsp;<strong>1</strong>&nbsp;if Tom wins, else return&nbsp;<strong>0</strong>.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">N = 2</span>
<strong><span style="font-size:18px">Output:</span></strong>
<span style="font-size:18px">1</span>
<strong><span style="font-size:18px">Explanation:</span></strong>
<span style="font-size:18px">Tom subtracts 1 from N to make N = 1.
Now, Jerry isn't left with any possible
turn so Tom wins the game, and therefore
the Output is 1.</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">N = 4</span>
<strong><span style="font-size:18px">Output:</span></strong>
<span style="font-size:18px">1</span>
<strong><span style="font-size:18px">Explanation:
</span></strong><span style="font-size:18px">1st turn: Tom subtract 1 from N as 1 is 
a divisor of 4 and less than 4.

2nd turn: N=3, Jerry has to subtract 1 as 1 
is the only divisor of 3 which is less than 3.

3rd turn: N=2, Tom subtract 1 as 1 is the 
only divisor of 2 which is less than 2.

4th turn: N=1, Jerry can't subtract any value.
So, Tom wins.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function numsGame() which takes an Integer N as input and returns 1 if Tom wins else returns 0.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity: </strong>O(1)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p><strong><span style="font-size:18px">Constraints:</span></strong><br>
<span style="font-size:18px">1 &lt;&nbsp;N ≤ 10<sup>8</sup></span></p>
</div>