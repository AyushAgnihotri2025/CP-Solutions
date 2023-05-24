# Count in array
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two positive integer&nbsp;<strong>N</strong>&nbsp;and <strong>M.</strong>&nbsp;The task is to find the number of arrays of size N&nbsp;that can be formed such that:</span></p>

<p><span style="font-size:18px">1. Each element is in the range [1, M].</span></p>

<p><span style="font-size:18px">2. All adjacent element are such that one of them divide the another i.e element A<sub>i</sub>&nbsp;divides A<sub>i + 1&nbsp;</sub>or A<sub>i+1</sub>&nbsp;divides A<sub>i</sub>.</span></p>

<p><br>
<strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> 
N = 3
M = 3
<strong>Output :</strong> 
17
<strong>Explanation:</strong>
{1,1,1}, {1,1,2}, {1,1,3}, {1,2,1}, 
{1,2,2}, {1,3,1}, {1,3,3}, {2,1,1},
{2,1,2}, {2,1,3}, {2,2,1}, {2,2,2},
{3,1,1}, {3,1,2}, {3,1,3}, {3,3,1}, 
{3,3,3} are possible arrays.
</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>
N = 1
M = 10 
<strong>Output:</strong> 
10
<strong>Explanation:</strong> 
{1}, {2}, {3}, {4}, {5}, 
{6}, {7}, {8}, {9}, {10}
are possible arrays.</span>
</pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>count()</strong>&nbsp;which take&nbsp;integers&nbsp;<strong>N and M</strong>&nbsp;as input parameter&nbsp;and returns the total the number of arrays of size N&nbsp;that can be formed with given constraints. The return value may long so take modulo 10<sup>9</sup>+7.&nbsp;<br>
<br>
<strong>Expected Time Complexity:</strong>&nbsp;O(N*M*Log M)&nbsp;<br>
<strong>Expected Space Complexity:</strong>&nbsp;O(N*M)&nbsp;<br>
<br>
<strong>Constraints:</strong><br>
1&lt;=N,M&lt;=100</span></p>
</div>