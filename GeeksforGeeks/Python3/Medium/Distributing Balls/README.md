# Distributing Balls
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Geek wants to distribute M balls among N children. His nemesis Keeg wants to disrupt his plan and removes P balls from Geek's bag. The minimum number of balls required to make each child happy are given in an array arr[]. Find the number of ways Geek can distribute the remaining balls so that each is happy.&nbsp;</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>
m = 13, n = 4, p = 5
arr = {2, 3, 1, 3}
<strong>Output:</strong> -1
<strong>Explaination:</strong> Number of balls left is 
m-p = 8. Minimum 9 balls are required to 
make everyone happy. So the task is not 
possible and the answer is -1.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>
m = 30, n = 10, p = 14
arr = {2, 2, 1, 1, 1, 2, 2, 3, 1, 1}
<strong>Output:</strong> 1
<strong>Explaination:</strong> At least 16 balls are required 
to make the children happy. 16 balls are left. 
So there is only one way to make them happy.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function <strong>countWays()</strong> which takes m, n, p and arr as input parameters and returns the &nbsp;number of possible ways to distribute the balls. Return the answer modulo 10<sup>9</sup> + 7.&nbsp;If there is no way of making everyone happy, return -1.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(m*n)<br>
<strong>Expected Auxiliary Space:</strong> O(n)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ m, p ≤ 1000<br>
1 ≤ n ≤ 100<br>
1 &lt; arr[i] &lt; 10&nbsp;</span></p>
</div>