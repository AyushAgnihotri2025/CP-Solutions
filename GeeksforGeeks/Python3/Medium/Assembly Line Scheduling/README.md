# Assembly Line Scheduling
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">A car factory has two assembly lines, and also given an&nbsp; 2D array <strong>a[2][]</strong> of size <strong>N </strong>which represent the time taken by each station. Each station is dedicated to some sort of work like engine fitting, body fitting, painting, and so on. So, a car chassis must pass through each of the n stations in order before exiting the factory. The two parallel assemble line perform same task.<br>
From any line one can switch another line diagonally. A 2D array <strong>T[2][]</strong> of size <strong>N</strong> is also given, which represent&nbsp; exit time to switch line 1 to line 2 diagonally.<br>
Also each assembly line takes an entry time e<sub>i</sub>&nbsp;and exit time x<sub>i</sub>&nbsp;which may be different for the two lines.</span></p>

<p><span style="font-size:18px">For more clarity, refer the following diagram<br>
<img alt="" src="https://media.geeksforgeeks.org/img-practice/AssembleScheduling1-1646927884.png"></span></p>

<p><span style="font-size:18px">The task is to&nbsp;computing the minimum time it will take to build a car chassis.<br>
One can minimize the total time taken by performing following steps:</span></p>

<ol>
	<li><span style="font-size:18px">&nbsp;A car chassis must pass through all stations from 1 to N&nbsp;in order(in any of the two assembly lines). i.e. it cannot jump from station i to station j if they are not at one move distance.</span></li>
	<li><span style="font-size:18px">The car chassis can move one station forward in the same line, or one station diagonally in the other line. It incurs an extra cost T<sub>i,j</sub> to move to station j from line i. No cost is incurred for movement in same line.</span></li>
	<li><span style="font-size:18px">The time taken in station j on line i is a<sub>i, j</sub>.</span></li>
</ol>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> N = 4
a[2][] = <code>{{4, 5, 3, 2}, 
      {2, 10, 1, 4}</code>}
T[2][] = {{0,7, 4, 5},
           {0,9, 2, 8}}
e[2] = {10,12}, x[2] = {18,7}</span>

<span style="font-size:18px"><strong>Output:</strong> 35
<strong>Explanation: </strong>
According to the TC, this would 
be the following diagram
<img alt="" src="https://media.geeksforgeeks.org/img-practice/AssembleScheduling-1646930583.png" style="height:200px; width:536px">
The bold line shows the path covered by the 
car chassis for given input values. So the minimum 
time taken by the car is 35.
</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>carAssembly</strong><strong>()</strong>&nbsp;which takes two array of&nbsp;integers&nbsp;<strong>a,T </strong>of size&nbsp;<strong>n&nbsp;</strong>and<strong>&nbsp;</strong>array of<strong> e&nbsp;</strong>and <strong>x </strong>of size 2<strong>&nbsp;</strong>as parameters and returns an integer&nbsp;denoting the answer.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤&nbsp;N ≤ 10<sup>5</sup><br>
1 ≤ a[2][], T[2][], e[], x[]&nbsp;≤ 10<sup>6</sup></span></p>

<p>&nbsp;</p>

<p><br>
<span style="font-size:18px">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></p>
</div>