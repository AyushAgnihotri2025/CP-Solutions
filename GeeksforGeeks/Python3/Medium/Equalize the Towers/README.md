# Equalize the Towers
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given heights <strong>h[]</strong> of <strong>N</strong>&nbsp;towers, the task is to bring every tower to the same height by either adding or removing blocks in a tower. Every addition or removal&nbsp;operation costs <strong>cost[]</strong> a particular value for the respective tower. Find out the <strong>Minimum cost to&nbsp;Equalize the Towers</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 3, h[] = {1, 2, 3} 
cost[] = {10, 100, 1000}
<strong>Output:</strong> 120
<strong>Explanation</strong>: The heights can be equalized 
by either "Removing one block from 3 and 
adding one in 1" or "Adding two blocks in 
1 and adding one in 2". Since the cost 
of operation in tower 3 is 1000, the first 
process would yield 1010 while the second 
one yields 120. Since the second process 
yields the lowest cost of operation, it is 
the required output.</span></pre>

<p><span style="font-size:18px">&nbsp;<br>
<br>
<strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 5, h[] = {9, 12, 18, 3, 10} 
cost[] = {100, 110, 150, 25, 99}
<strong>Output:</strong> 1623 
</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong>Bsearch</strong>() that takes<strong>&nbsp;</strong>integer<strong> N, </strong>array<strong> H</strong>, and array<strong> Cost&nbsp;</strong>as parameters and returns the minimum cost required to equalize the towers.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(NlogN).&nbsp;<br>
<strong>Expected Auxiliary Space:</strong> O(1).</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>6</sup></span></p>
</div>