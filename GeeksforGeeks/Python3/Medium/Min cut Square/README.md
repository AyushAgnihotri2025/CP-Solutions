# Min cut Square
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two numbers <strong>M and N</strong>, which represents the length and breadth of a paper, the task is to cut the paper into squares of any size and find the minimum number of squares that can be cut from the paper.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: M = 36, N = 30
<strong>Output:</strong> 5
<strong>Explanation</strong>: </span>
<span style="font-size:18px">3 (squares of size 12x12) + 
2 (squares of size 18x18)</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>M = 4, N = 5
<strong>Output: </strong>5
<strong>Explanation</strong>: 
</span></pre>

<pre><span style="font-size:18px">1 (squares of size 4x4) + 
4 (squares of size 1x1)</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Complete the function <strong><code>minCut</code>()&nbsp;</strong>which takes <strong>M</strong> and <strong>N</strong> as input parameters and returns the integer value<br>
<br>
<strong>Expected Time Complexity:</strong>&nbsp;O(<strong>M*N*(N +M)</strong>)</span><br>
<span style="font-size:18px"><strong>Expected Auxiliary Space:</strong> O(<strong>M*N</strong>)<br>
<br>
<strong>Constraints:</strong><br>
1 ≤ M, N ≤ 10<sup>2</sup></span></p>
</div>