# Leftmost Divisor
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">For any two given positive integers p&nbsp;and q, find (if present) the leftmost digit in the number obtained by computing the exponent p<sup>q</sup>&nbsp; i.e. p&nbsp;raised to the power q, such that it is a divisor of p<sup>q</sup>.<br>
<strong>Note: </strong>p<sup>q</sup><sup>&nbsp;</sup>may be a very huge number, so if the number of digits in p<sup>q</sup> is greater than 18, you need to extract the first 10 digits of the result and&nbsp; check if any digit of that number divides the number.</span><br>
<br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: p = 1, q = 1
<strong>Output:</strong>&nbsp;1&nbsp;
<strong>Explanation</strong>: 1 raised to the power 1 gives 1, 
which is a divisor of itself i.e. 1.</span><span style="font-size:18px">  
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>p = 5, q = 2
<strong>Output:&nbsp;</strong>5
<strong>Explanation</strong>: The exponent 5 raised to the power 2 
gives 25, wherein leftmost digit 2, does not 
divide 25 but 5 does. Hence output is 5. 
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You dont need to read input or print anything. Complete the function <strong>leftMostDiv()&nbsp;</strong>which takes p&nbsp;and q&nbsp;as input parameter and returns&nbsp;the left-most digit in the number p<sup>q</sup>&nbsp;which is a divisor of p<sup>q</sup>. If no such digit exists, returns&nbsp;-1.<br>
<br>
<strong>Expected Time Complexity:</strong> O(n)<br>
<strong>Expected Auxiliary Space:</strong> O(1)<br>
<br>
<strong>Constraints:</strong><br>
1 &lt;= p&nbsp;, q&nbsp;&lt;=50</span></p>
</div>