# Buying Vegetables
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Geek wants to inspect the quality of vegetables at each shop in the vegetable market. There are N different vegetable sellers in a line. A single kilogram each of brinjal, carrot and tomato are available with every seller but at different prices.&nbsp;Geek wants to buy exactly one vegetable from one shop and avoid buying the same vegetables from adjacent shops.&nbsp;<br>
Given the cost of each vegetable in each shop in a Nx3 matrix, calculate the minimum amount of money that Geek must spend in the inspection.&nbsp;</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>
N = 3
cost = {{1, 50, 50}, 
        {50, 50, 50}, 
        {1, 50, 50}}
<strong>Output:</strong> 52
<strong>Explaination:</strong> 
Shop 1: Buy Brinjals for Rs 1.
Shop 2: Buy Carrot or Tomatoes for Rs 50.
Shop 3: Buy Brinjals for Rs 1.
Total = 1+50+1 = 52</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function <strong>minCost()</strong> which takes N and Nx3 matrix cost[][] as input parameters and returns he minimum amount of money that Geek must spend in the inspection.&nbsp;</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity: </strong>O(N)<br>
<strong>Expected Auxiliary Space: </strong>O(N)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5&nbsp;</sup><br>
1 ≤ cost[i][j] ≤ 100&nbsp;</span></p>
</div>