# Minimum cost to fill given weight in a bag
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>cost[]</strong> of positive integers of size <strong>N</strong> and an integer <strong>W</strong>, cost[i] represents the cost of <strong>i</strong> kg packet of oranges, the task is to find the minimum cost to buy <strong>W</strong> kgs of oranges.</span> <span style="font-size:18px">If it is not possible to buy exactly <strong>W</strong> kg oranges then the output will be -1</span></p>

<p><span style="font-size:18px"><strong>Note:</strong><br>
1. cost[i] = -1 means that i kg packet of orange is unavailable<br>
2. </span> <span style="font-size:18px">It may be assumed that there is infinite supply of all available packet types.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: N = 5, arr[] = {20, 10, 4, 50, 100}
W = 5
<strong>Output:</strong> 14
<strong>Explanation</strong>: choose two oranges to minimize 
cost. First orange of 2Kg and cost 10. 
Second orange of 3Kg and cost 4. </span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: N = 5, arr[] = {-1, -1, 4, 3, -1}
W = 5
<strong>Output:</strong> -1
<strong>Explanation</strong>: It is not possible to buy 5 
kgs of oranges</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Complete the function <strong><code>minimumCost</code>()&nbsp;</strong>which takes <strong>N, W, </strong>and array <strong>cost </strong>as input parameters and returns the minimum value.<br>
<br>
<strong>Expected Time Complexity:</strong> O(<strong>N*W</strong>)<br>
<strong>Expected Auxiliary Space:</strong> O(<strong>N*W</strong>)<br>
<br>
<strong>Constraints:</strong><br>
1 ≤ N, W ≤ 2*10<sup>2</sup></span><br>
<span style="font-size:18px">-1 ≤ cost[i] ≤ 10<sup>5</sup></span><br>
<span style="font-size:18px">cost[i] ≠ 0</span></p>
</div>