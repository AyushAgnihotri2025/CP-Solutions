# Two water Jug problem
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are at the side of a river. You are given a&nbsp;<strong>m</strong>&nbsp;litre jug and a&nbsp;<strong>n</strong>&nbsp;litre jug . Both the jugs are initially empty. The jugs dont have markings to allow measuring smaller quantities. You have to use the jugs to measure d litres of water . Determine the minimum no of operations to be performed to obtain d litres of water in one of the jugs.<br>
The operations you can perform are:</span></p>

<ol>
	<li><span style="font-size:18px">Empty a Jug</span></li>
	<li><span style="font-size:18px">Fill a Jug</span></li>
	<li><span style="font-size:18px">Pour water from one jug to the other until one of the jugs is either empty or full.</span></li>
</ol>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>m = 3, n = 5, d = 4
<strong>Output: </strong>6
<strong>Explanation:</strong>&nbsp;Operations are as follow-
</span><span style="font-size:18px">1. Fill up the 5 litre jug.
2. Then fill up the 3 litre jug using 5 litre
&nbsp;  jug. Now 5 litre jug contains 2 litre water.
3. Empty the 3 litre jug.
4. Now pour the 2 litre of water from 5 litre 
&nbsp;  jug to 3 litre jug.
5. Now 3 litre jug contains 2 litre of water 
&nbsp;  and </span><span style="font-size:18px">5 litre jug is empty. Now fill up the 
&nbsp;  5 litre jug.
6. Now fill one litre of water from 5 litre jug 
&nbsp;  to 3 litre jug. Now we have 4 litre water in 
&nbsp;  5 litre jug.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>m = 8, n = 56, d = 46
<strong>Output: </strong>-1
<strong>Explanation: </strong>Not possible to fill any one of 
the jug with 46 litre of water.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>minSteps()</strong>&nbsp;which takes m, n and d ans input parameter and returns the minimum number of operation to fill d litre of water in any of the two jug.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Comeplxity:&nbsp;</strong>O(d)<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(1)<br>
<br>
<strong>Constraints:</strong><br>
1 ≤ n,m ≤ 100<br>
1 ≤ d ≤ 100</span></p>
</div>