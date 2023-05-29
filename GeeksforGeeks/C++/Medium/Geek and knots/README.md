# Geek and knots
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two walls A, B with M, N hooks respectively. You are given K ropes. By using one rope you can connect one hook on wall A with another hook on wall B. One hook can connect with only one rope.&nbsp;Find the number of <strong>different ways</strong> you can use all the K ropes.<br>
Two ways that use the&nbsp;<strong>exact same set</strong> of hooks from wall A <strong>and</strong> wall B are considered to be same.&nbsp;</span></p>

<blockquote>
<p><span style="font-size:18px">For Example,&nbsp;<br>
A1 &nbsp; &nbsp;A2 &nbsp; &nbsp;A3 &nbsp; &nbsp; </span><span style="font-size:18px">&nbsp;is same as</span><span style="font-size:18px">&nbsp;&nbsp; &nbsp; A1&nbsp;&nbsp; A2&nbsp;&nbsp; A3 &nbsp; &nbsp;&nbsp;</span><span style="font-size:18px">and can be ignored.</span><br>
<span style="font-size:18px">&nbsp;| &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
B1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; B2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;B2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; B1</span></p>
</blockquote>

<p><span style="font-size:18px">Because both knots are using same set of wall A hooks (A1, A3) and same set of wall B hooks (B1,B2)<br>
<strong>Note:</strong>&nbsp;Answer can be large, return the answer modulo 10<sup>9</sup>+7.&nbsp;</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
M = 3, N = 2, K = 2
<strong>Output:</strong> 3
<strong>Explanation: </strong>
hooks on Wall A are A1, A2, A3.
hooks on wall B are B1, B2. </span>
<span style="font-size:18px">Different Possible Knots are
K1 = (A1-B1, A2-B2), K2 = (A1-B1, A3-B2), 
K3 = (A2-B1, A3-B2)  
Each of these use different set of hooks from wall A. </span>

</pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
M = 2, N = 2, K = 2
<strong>Output:</strong> 1
<strong>Explanation: 
</strong>A1   A2 
|    | 
B1   B2
There is only one way to select 2 hooks 
from wall A and 2 from wall B. </span>
</pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function <strong>knots()</strong> which takes M, N and K as input parameters and returns the number of possible knots. Return the answer modulo 10<sup>9</sup>+7.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(max(N2, M2))<br>
<strong>Expected Auxiliary Space: </strong>O(max(N2, M2))</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N, M, K ≤ 1000<br>
1 ≤ K ≤ min(N, M)&nbsp;</span></p>
</div>