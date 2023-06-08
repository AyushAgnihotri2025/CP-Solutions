# Buy Stock with Transaction Fee
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are given an array&nbsp;<code>prices</code>&nbsp;where&nbsp;<code>prices[i]</code>&nbsp;is the price of a given stock on the&nbsp;<code>i<sup>th</sup></code>&nbsp;day, and an integer&nbsp;<code>fee</code>&nbsp;representing a transaction fee.</span></p>

<p><span style="font-size:18px">Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.</span></p>

<p><span style="font-size:18px"><strong>Note:</strong>&nbsp;You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</span></p>

<pre><strong><span style="font-size:18px">Example:
Input:
</span></strong><span style="font-size:18px">n = 6
prices = [1,3,2,8,4,9]
fee = 2
<strong>Output:
</strong>8
<strong>Explanation:</strong></span>
<span style="font-size:18px">The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.</span>
</pre>

<p><strong><span style="font-size:18px">Your Task:</span></strong><br>
<span style="font-size:18px">You don't have to read input or print anything. Your task is to complete the function&nbsp;<strong>maximumProfit()&nbsp;</strong>which takes the integer&nbsp;<strong>n</strong>&nbsp;and array prices and transaction <strong>fee&nbsp;</strong>and returns the maximum profit that can earn.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity: </strong>O(n)<br>
<strong>Expected Space Complexity: </strong>O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraint:</strong><br>
1 &lt;= n &lt;= 5*10<sup>4</sup></span><br>
<span style="font-size:18px">1 &lt;= prices[i] &lt;&nbsp;5 * 10<sup>4&nbsp;</sup><br>
0 &lt;= fee &lt; 5 * 10<sup>4</sup></span></p>

<p>&nbsp;</p>
</div>