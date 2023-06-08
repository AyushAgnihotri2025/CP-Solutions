# Minimum days to make M bouquets
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">To make one bouquet we need <strong>K </strong>adjacent flowers from the garden. Here the garden consists of <strong>N </strong>different flowers, the ith flower will bloom in the <strong>bloomDay[i]</strong>.&nbsp;Each flower can be used inside only one bouquets.&nbsp;We have to find the minimum number of days need to wait to make <strong>M </strong>bouquets from the garden. If we cannot make m bouquets, then return -1.</span></p>

<p><span style="font-size:18px">The first line of input contains two integers M and&nbsp;K.<br>
The second line contains N space-separated integers of bloomDay[i] array.</span></p>

<h4><span style="font-size:18px"><strong>Example 1</strong>:</span></h4>

<pre><span style="font-size:18px"><strong>Input</strong>:
M = 2, K = 3
bloomDay = [5, 5, 5, 5, 10, 5, 5]
<strong>Output</strong>:
10
<strong>Explanation</strong>:
As we need 2 (M = 2) bouquets and each should have 3 flowers,
After day 5: [x, x, x, x, _, x, x], we can make one bouquet of
the first three flowers that bloomed, but cannot make another bouquet.
After day 10: [x, x, x, x, x, x, x], Now we can make two bouquets,
taking 3 adjacent flowers in one bouquet.</span></pre>

<p><span style="font-size:18px"><strong>Example 2</strong>:</span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: </span>
<span style="font-size:18px">M = 3, K = 2</span>
<span style="font-size:18px">bloomDay = [1, 10, 3, 10, 2]</span>
<span style="font-size:18px"><strong>Output</strong>: 
-1</span>
<span style="font-size:18px"><strong>Explanation</strong>:
As 3 bouquets each having 2 flowers are needed, that means we need 6 flowers. 
But there are only 5 flowers so it is impossible to get the needed bouquets
therefore -1 will be returned.

</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Complete the function int solve(), which takes integer M, K, and a list of N integers as input and returns the </span><em>&nbsp;</em><span style="font-size:18px">minimum number of days needed to wait to be able to make&nbsp;<code>M</code>&nbsp;bouquets from the garden.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity</strong>: O(N.log(maxVal)), where&nbsp;maxVal = max(bloomDay<strong>)</strong><br>
<strong>Expected Auxiliary Space</strong>: O(1)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong></span></p>

<p><span style="font-size:18px">1 &lt;= N &lt;= 10<sup>5</sup><br>
1 &lt;= M &lt;= 10<sup>5</sup><br>
1 &lt;= K &lt;= N<br>
1 &lt;= <strong>bloomDay</strong>[i] &lt;= 10<sup>9</sup></span></p>
</div>