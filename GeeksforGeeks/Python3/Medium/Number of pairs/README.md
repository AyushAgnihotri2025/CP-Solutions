# Number of pairs
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two arrays <strong>X[]</strong> and <strong>Y[]</strong>&nbsp;of size M and N respectively.&nbsp;Find number of pairs such that&nbsp;<strong>x<sup>y</sup> &gt; y<sup>x</sup></strong>&nbsp;where <strong>x</strong> is an element from <strong>X[]</strong> and <strong>y</strong> is an element from <strong>Y[]</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>M = 3, N = 2
X[] = {2, 1, 6}, Y = {1, 5}
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are total 3 pairs 
where pow(x, y) is greater than pow(y, x) 
Pairs are (2, 1), (2, 5) and (6, 1).</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>M = 3, N = 3
X[] = {10, 19, 18}, Y[] = {11, 15, 9}
<strong>Output:</strong> 2
<strong>Explanation:</strong>&nbsp;There are total 2 pairs 
where pow(x, y) is greater than pow(y, x) 
Pairs are (10, 11) and (10, 15).</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>countPairs()</strong>&nbsp;which takes array&nbsp;<strong>X[]</strong>, array&nbsp;<strong>Y[]</strong>, <strong>m</strong>&nbsp;and&nbsp;<strong>n&nbsp;</strong>as input parameters and returns an integer denoting the number of pairs that are true to the given condition.&nbsp;</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N*logN + M*logM)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ M, N ≤ 10<sup>5</sup><br>
1 ≤ X[i], Y[i]&nbsp;≤ 10<sup>3</sup></span><br>
&nbsp;</p>
</div>