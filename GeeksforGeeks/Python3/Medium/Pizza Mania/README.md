# Pizza Mania
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Small Pizza has an area of '<strong>S</strong>' units</span><span style="font-size:18px">. Medium Pizza has an area&nbsp;</span><span style="font-size:18px">of '<strong>M</strong></span><span style="font-size:18px">' units</span><span style="font-size:18px">. Large Pizza has an area of '<strong>L</strong>' units</span><span style="font-size:18px">.<br>
Cost of </span><span style="font-size:18px">Small,</span><span style="font-size:18px"> medium and Large Pizza is '</span><span style="font-size:18px"><strong>CS</strong>' ,</span><span style="font-size:18px"> '<strong>CM</strong>', and '<strong>CL</strong>' respectively.</span><span style="font-size:18px"> What is the minimum amount of money</span><span style="font-size:18px"> needed so that one can buy </span><span style="font-size:18px">atleast</span><span style="font-size:18px"> <strong>X</strong> units square of Pizza?</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<span style="font-size:18px"><strong>X = </strong>16, <strong>S = </strong>3, <strong>M = </strong>6, <strong>L = </strong>9, <strong>CS = </strong>50, <strong>CM = </strong>150, <strong>CL = </strong>300</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">300</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">We want </span><span style="font-size:18px">atleast</span><span style="font-size:18px"> 16 sq. units of Pizza.
1S 1M 1L area= 3+6+9 = 18 sq units, Cost=500
6S  area=18 sq units, Cost=300
2L area=18 sq units, Cost=600</span><span style="font-size:18px"> etc.
Of all the Arrangements, Minimum Cost is Rs. 300.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<span style="font-size:18px"><strong>X = </strong>10, <strong>S = </strong>1, <strong>M = </strong>3, <strong>L = </strong>10, <strong>CS = </strong>10, <strong>CM = </strong>20, <strong>CL = </strong>50</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">50</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">Of all the Arrangements possible,
Minimum Cost is Rs. 50.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>getPizza()</strong> which takes 7 Integers X, S, M, L, CS, CM, and CL as input and returns the minimum amount needed to buy atleast X sq. units of Pizza .</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(X)<br>
<strong>Expected Auxiliary Space:</strong> O(X)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong></span><br>
<span style="font-size:18px">1 &lt;= X &lt;= 500<br>
1 &lt;= S &lt;= M &lt;= L &lt;= 100<br>
1 &lt;= CS &lt;= CM &lt;= CL &lt;= 100</span></p>
</div>