# Tic Tac Toe
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">A Tic-Tac-Toe board is given after some moves are played. Find out if the given board is valid, i.e., is it possible to reach this board position after some moves or not.</span></p>

<p><span style="font-size:18px">Note that every arbitrary filled grid of 9 spaces isn’t valid e.g. a grid filled with 3 X and 6 O isn’t valid situation because each player needs to take alternate turns.</span></p>

<p><span style="font-size:18px"><strong>Note : &nbsp;</strong>The game starts with X</span></p>

<p><span style="font-size:18px"><img alt="" src="http://d1hyf4ir1gqw6c.cloudfront.net/wp-content/uploads/tictactoe.png" style="height:223px; width:350px"></span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
board[] = {'X', 'X', 'O', 
           'O', 'O', 'X',
           'X', 'O', 'X'};
<strong>Output:</strong> Valid
<strong>Explanation:</strong> This is a valid board.
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>board[] = {'O', 'X', 'X', 
           'O', 'X', 'X',
           'O', 'O', 'X'};
<strong>Output:</strong> Invalid
<strong>Explanation:</strong>&nbsp;Both X and O cannot win.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>isValid()</strong>&nbsp;which takes a character array of size 9 representing the board as input&nbsp;parameter&nbsp;and returns a boolean value&nbsp;denoting if it is valid or not.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(1)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
Every character on the&nbsp;board can either&nbsp;be 'X' or 'O'.</span></p>

<p>&nbsp;</p>
</div>