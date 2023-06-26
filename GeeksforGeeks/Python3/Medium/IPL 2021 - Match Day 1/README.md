# IPL 2021 - Match Day 1
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Due to the rise of covid-19 cases in India, this year BCCI decided to organize knock-out matches in IPL rather than a league. </span></p>

<p><span style="font-size:18px">Today is matchday 1 and it is between previous year winners Mumbai Indians and the city of Joy - Kolkata Knight Riders. Eoin Morgan the new captain of the team KKR, thinks that death overs are very important to win a match. He decided to end MI's innings with his most trusted bowler Pat Cummins to minimize the target. There must be at least 4 players inside the 30-yard circle in death overs. Positions of 3 players are already decided which are given as 2-D integer points <strong>A</strong>, <strong>B</strong>, and <strong>C</strong>,&nbsp; the task is to find the missing point <strong>D</strong> such that <strong>ABCD</strong> should be a parallelogram. If there are multiple such points, find the lexicographically smallest coordinate.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
A = (3, 2)
B = (3, 4)
c = (2, 2)
<strong>Output:
</strong>2.000000 0.000000
<strong>Explanation</strong>: There are two options for 
point D : (2, 4) and (2, 0) such that ABCD 
forms a parallelogram. Since (2, 0) is 
lexicographically smaller than (2, 4). Hence,
(2, 0) is the answer.</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>findPoint()&nbsp;</strong>which takes three lists of integers <strong>A[]</strong>, <strong>B[] </strong>and <strong>C[]</strong> and return <strong>D[]</strong> list of two numbers with a precision of 6 decimal places where first element of <strong>D[ ] </strong>denote x coordinate and second&nbsp;element of <strong>D[ ] </strong>denote y&nbsp;coordinate.</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ x, y ≤ 1000, where x and y denote coordinates of points A, B, and C.<br>
The order of points in the parallelogram doesnt matter.<br>
The given points are not collinear.</span></p>
</div>