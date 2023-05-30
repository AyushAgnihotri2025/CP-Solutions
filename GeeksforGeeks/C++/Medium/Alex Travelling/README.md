# Alex Travelling
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Alex is very fond of traveling. There are&nbsp;<strong>n </strong>cities, labeled from<strong> 1</strong> to<strong> n</strong>.&nbsp;&nbsp;You are also given flights, a list of travel flights as <strong>directed weighted</strong> edges<strong> flights[i] = (u<sub>i</sub>,v<sub>i</sub>,w<sub>i</sub>)</strong>&nbsp;where<strong> u<sub>i&nbsp;</sub></strong>is the source node,<strong> v<sub>i</sub>&nbsp;</strong>is the target node, and <strong>w<sub>i</sub></strong>&nbsp;is the price it takes for a person to travel from source to target.<br>Currently, Alex is in <strong>k</strong>'th city and wants to visit one city of his choice. Return&nbsp;the<strong>&nbsp;minimum&nbsp;</strong>money&nbsp;Alex should have so&nbsp;that he can visit any city of his choice from <strong>k</strong>'th&nbsp;city. If there is a city that has no path from&nbsp;<strong>k</strong>'th city, which means Alex can't visit that city,&nbsp;return <strong>-1</strong>.&nbsp;<br>Alex always takes the optimal path. He can any city via another city by taking multiple flights.</span><br>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
n: 4
k: 2
flights size: 3
flights: [[2,1,1],[2,3,1],[3,4,1]]
<strong>Output:</strong>
2
<strong>Explanation:</strong>
to visit 1 from 2 takes cost 1
to visit 2 from 2 takes cost 0
to visit 3 from 2 takes cost 1
to visit 4 from 2 takes cost 2,
2-&gt;3-&gt;4
So if Alex wants to visit city 4
from 2, he needs 2 units of money
</span><img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/711152/Web/Other/3d37201b-eda2-4fbf-97d7-cde7afa25d3c_1685087900.png">

</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
n: 4 
k: 3 
flights size: 3 
flights: [[2,1,1],[2,3,1],[3,4,1]] 
<strong>Output:</strong> -1
<strong>Explanation:</strong>
There is no direct or indirect path 
to visit city 2 and 1 from city 3
</span><img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/711152/Web/Other/81ceaa5b-7e97-4937-9431-ff299dacb76e_1685087901.png">

</pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong></span></p>
<p><span style="font-size: 18px;">You don't need to print or input anything. Complete the function <strong>minimumCost()&nbsp;</strong>which takes a&nbsp; flights array, an integer n and an integer k<strong>&nbsp;</strong>as the input parameters and returns an integer, denoting&nbsp;the<strong> minimum&nbsp;</strong>money Alex should have so&nbsp;that he can visit any city of his choice from k'th city.<br><br><strong>Expected Time Complexity:</strong> O((V+E) log V), here V is number of cities and E is number of flights.&nbsp;<br><strong>Expected Auxiliary Space</strong>: O(V+E), here V is number of cities and E is number of flights.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span></p>
<ul>
<li><span style="font-size: 18px;">2 &lt;= n &lt;= 500</span></li>
<li><span style="font-size: 18px;">1 &lt;= flights.length&nbsp;&lt;= 100000</span></li>
<li><span style="font-size: 18px;">flights[i].length == 3</span></li>
<li><span style="font-size: 18px;">1 &lt;= u<sub>i</sub>, v<sub>i</sub>, k&lt;= n</span></li>
<li><span style="font-size: 18px;">u<sub>i</sub>&nbsp;!= v<sub>i</sub></span></li>
<li><span style="font-size: 18px;">1 &lt;= w<sub>i</sub>&nbsp;&lt;= 100</span></li>
<li><span style="font-size: 18px;">All the pairs&nbsp;(u<sub>i</sub>, v<sub>i</sub>)&nbsp;are&nbsp;<strong>unique</strong>. (i.e., no multiple edges)</span></li>
</ul></div>