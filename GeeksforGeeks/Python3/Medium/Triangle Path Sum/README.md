# Triangle Path Sum
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a&nbsp;<strong>triangle</strong>&nbsp;array, return&nbsp;the <strong>minimum path sum</strong> to reach from<strong> top </strong>to <strong>bottom</strong>.</span></p>

<p><span style="font-size:18px">For each step, you may move to an adjacent number of the row below. More formally, if you are on index&nbsp;<strong><code>i</code></strong>&nbsp;on the <strong>current row</strong>, you may move to either index&nbsp;<strong><code>i</code>&nbsp;</strong>or index&nbsp;<strong><code>i + 1</code></strong>&nbsp;on the <strong>next row.</strong></span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n = 4
triangle = [[2],
&nbsp;          [3,4],
&nbsp;         [6,5,7],
&nbsp;        [4,1,8,3]]
<strong>Output:</strong>
11
<strong>Explanation:</strong></span>
     <span style="font-size:18px">2
   <u>3</u> 4
  6 <u>5</u> 7
 4 <u>1</u> 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n =  1</span>
<span style="font-size:18px">triangle = [[10]]
<strong>Output:</strong>
10</span></pre>

<p><strong><span style="font-size:18px">Your Task:</span></strong><br>
<span style="font-size:18px">You don't have to read input or print anything. Your task is to complete the function&nbsp;<strong>minimizeSum()&nbsp;</strong>which takes integer n and the triangle&nbsp;and returns the minimum sum to reach from top to bottom.</span></p>

<p><strong><span style="font-size:18px">Constraint:</span></strong><br>
<span style="font-size:18px">1 &lt;= triangle.length &lt;= 200</span><br>
<span style="font-size:18px">triangle[i].length =&nbsp; triangle[i-1].length + 1<br>
1 &lt;= triangle[i][j] &lt;= 1000</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(n * n)<br>
<strong>Expected Space Complexity:</strong> O(n* n)</span></p>
</div>