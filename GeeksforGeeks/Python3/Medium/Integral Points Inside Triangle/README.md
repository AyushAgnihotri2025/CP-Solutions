# Integral Points Inside Triangle
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given three non-collinear points whose co-ordinates are <strong>P(p1, p2), Q(q1, q2)&nbsp;</strong>and<strong> R(r1, r2) </strong>in the&nbsp;X-Y plane.&nbsp;Find the number of<strong> </strong>integral / lattice points strictly inside the&nbsp;triangle&nbsp;formed by these points.<br>
Note -&nbsp;A point in X-Y plane is said to be integral / lattice point if both its co-ordinates are integral.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
p = (0,0)
q = (0,5)
r = (5,0)
<strong>Output: </strong>6
<strong>Explanation:</strong>
There are 6 integral points in the 
triangle formed by p, q and r.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
p = (62,-3)
q = (5,-45)
r = (-19,-23)
<strong>Output: </strong>1129
<strong>Explanation:</strong>
There are 1129 integral points in the 
triangle formed by p, q and r.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>InternalCount()</strong> which takes the three points p, q&nbsp;and r as input parameters and returns the number of integral points contained within the triangle formed by p, q&nbsp;and r.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(Log<sub>2</sub>10<sup>9</sup>)<br>
<strong>Expected Auxillary Space:&nbsp;</strong>O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
-10<sup>9&nbsp;</sup>≤ x-coordinate, y-coordinate ≤&nbsp;10<sup>9</sup></span></p>
</div>