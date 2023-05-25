# Dyck Path
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Consider a <strong>N</strong> x <strong>N</strong> grid with indexes of top left corner as (0, 0). Dyck path is a staircase walk from bottom left, i.e., (N-1, 0) to top right, i.e., (0, N-1) that lies above the diagonal cells (or cells on line from bottom left to top right).</span></p>

<p><span style="font-size:18px">The task is to count the number of Dyck Paths from (N-1, 0) to (0, N-1).</span></p>

<p><span style="font-size:18px">Here are the some of the possible paths for different N.</span></p>

<p><span style="font-size:18px"><img alt="" src="https://contribute.geeksforgeeks.org/wp-content/uploads/Dyck.jpg"></span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<strong><span style="font-size:18px">N = </span></strong><span style="font-size:18px">4</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">14 </span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">Refer to the diagram above.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<strong><span style="font-size:18px">N = </span></strong><span style="font-size:18px">3</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">5</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">Refer to the diagram above.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>dyckPaths()</strong> which takes an Integer N as input and returns the answer.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong></span><br>
<span style="font-size:18px">1 &lt;= N &lt;= 30</span></p>
</div>