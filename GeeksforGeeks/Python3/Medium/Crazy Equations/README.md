# Crazy Equations
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Jon wants to go in birthday party of Arya. But he is busy in finding solution of crazy equations, so he wants your help to solve this problem.&nbsp;Jon has four integers <strong>a, b, c, d </strong>now he wants to calculate how many distinct set of&nbsp;<strong>x, y, z, w </strong>are present such that&nbsp;&nbsp;<strong>a + b - x &nbsp;== a + c - y == c + d - z == b + d - w<br>
NOTE :&nbsp;</strong>&nbsp;1&lt;= x, y, z, w&lt;=n&nbsp; &nbsp;where n is a given&nbsp;integer.<br>
Two set of x, y, z, w will be different if atleast one value will be different.</span><br>
<br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: n = 5, a = 1, b = 2, c = 2, d = 2
<strong>Output:</strong>&nbsp;4
<strong>Explanation</strong>: Sets of x, y, z, w can be
             (1, 1, 2, 2)
             (2, 2, 3, 3)
             (3, 3, 4, 4)
             (4, 4, 5, 5).</span><span style="font-size:18px">
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>n = 5, a = 1, b = 2, c = 2, d = 1
<strong>Output:&nbsp;</strong>5
<strong>Explanation</strong>: same explanation as previous one.
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You dont need to read input or print anything. Complete the function <strong>distinctValues()&nbsp;</strong>which takes n, a, b, c&nbsp;and d&nbsp;as input parameter and returns the total number of&nbsp;distinct set of&nbsp;<strong>x, y, z, w&nbsp;</strong>are present.&nbsp;</span><br>
<br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(n)<br>
<strong>Expected Auxiliary Space:</strong> O(1)<br>
<br>
<strong>Constraints:</strong><br>
1 &lt;= n&nbsp;&lt;= 10<sup>6</sup><br>
1 &lt;= a, b, c, d&nbsp;&lt;= n</span></p>
</div>