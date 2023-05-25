# Pyramid form
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">We have an array <strong>a[] </strong>of <strong>N</strong> stones of various heights laid out in a row. By taking some consecutive section of the stones, we wish to form a pyramid, where the height of the stones start from 1, increase by 1, until it reaches some value x, then decreases by 1 until it reaches 1 again i.e. the stones should be 1, 2, 3, 4…x – 1, x, x – 1, x – 2 … 1. All other stones not part of the pyramid should have a height 0. We cannot move any of the stones from their current position, however, by paying a fee of 1, we can reduce the heights of the stones. We wish to minimize the cost of building a pyramid. Output the minimum cost to build this pyramid. Assume that always a pyramid would be made of the input elements.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span><span style="font-size:18px"> </span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<span style="font-size:18px"><strong>N = </strong>6</span>
<span style="font-size:18px"><strong>a[] = </strong>{1, 2, 3, 4, 2, 1}</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">4</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">We </span><span style="font-size:18px">can obtain the array {1, 2, 3, 2, 1, 0}
by substracting 2 out of 4, 1 out of 2,
and 1 out of 1. In total, we will substract 4.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span><span style="font-size:18px"> </span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<span style="font-size:18px"><strong>N = </strong>3</span>
<span style="font-size:18px"><strong>a[] = </strong>{1, 2, 1}</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">0</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">The array is already in Pyramid form.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>pyramidForm()</strong> which takes an Integer N and an array a[] as input and returns the minimum cost.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(1)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong></span><br>
<span style="font-size:18px">1 &lt;= N &lt;= 10<sup>5</sup></span><br>
<span style="font-size:18px">1 &lt;= a[i] &lt;= 10<sup>5</sup></span></p>
</div>