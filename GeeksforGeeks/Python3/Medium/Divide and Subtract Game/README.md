# Divide and Subtract Game
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Jon and Arya are playing a game. Rules of game as follows:<br>
<strong></strong>&nbsp;&nbsp;They have a single number <strong>N</strong> initially.</span><br>
<span style="font-size:18px"><strong></strong>&nbsp;&nbsp;&nbsp;Both will play an alternate move. Jon starts first.</span><br>
<span style="font-size:18px"><strong></strong>&nbsp; &nbsp;Both will play each move optimally.</span><br>
<span style="font-size:18px"><strong></strong>&nbsp;&nbsp;&nbsp;In each move, they can perform <strong>only one of these operation</strong></span><br>
<span style="font-size:18px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.&nbsp;Divide that number by 2, 3, 4 or 5 and take floor of result.</span><br>
<span style="font-size:18px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.&nbsp;Subtract that number by 2, 3, 4 or 5.<br>
<strong>&nbsp;&nbsp; </strong>If after making a move the number becomes 1, the player who made the move automatically loses the game.<br>
<strong></strong>&nbsp;&nbsp;&nbsp;When number becomes zero, the game will stop and the player who can't make a move loses the game.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<span style="font-size:18px"><strong>N = </strong>3</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">Jon</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">Jon will just subtract 3 from initial
number and win the game.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<span style="font-size:18px"><strong>N = </strong>6</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">Arya</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">Jon will divide by 3 and then in next step
Arya will subtract by 2 and win the game.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>divAndSub()</strong> which takes an Integer N as input and returns a string denoting who won the game.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space:</strong> O(N)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong></span><br>
<span style="font-size:18px">1 &lt;= N &lt;= 10<sup>5</sup></span></p>
</div>