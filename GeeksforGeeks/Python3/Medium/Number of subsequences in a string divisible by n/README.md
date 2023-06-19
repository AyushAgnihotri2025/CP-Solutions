# Number of subsequences in a string divisible by n
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given string <strong>s</strong> consisting of digits 0-9 and a number <strong>N</strong>, the task is to count the number of subsequences that are divisible by <strong>N</strong>.</span></p>

<p><span style="font-size:18px"><strong>Note:</strong> Answer can be large, output answer modulo 10<sup>9</sup> + 7</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: s = "1234", N = 4
<strong>Output:</strong> 4</span>
<span style="font-size:18px"><strong>Explanation</strong>: The subsequences 4, 12, 24 and 
124 are divisible by 4.</span></pre>

<div><span style="font-size:18px"><strong>Example 2:</strong></span></div>

<pre><span style="font-size:18px"><strong>Input</strong>: s = "330", N = 6
<strong>Output:</strong> 4</span>
<span style="font-size:18px"><strong>Explanation</strong>: The subsequences 30, 30, 330 
and 0 are divisible by 6.</span>
</pre>

<div><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Complete the function <strong><code>countDivisibleSubseq</code>()&nbsp;</strong>which takes <strong>s</strong> and <strong>N </strong>as input parameters and returns the integer value<br>
<br>
<strong>Expected Time Complexity:</strong> O(<strong>|s|*N</strong>)<br>
<strong>Expected Auxiliary Space:</strong> O(<strong>|s|*N</strong>)<br>
<br>
<strong>Constraints:</strong><br>
1 ≤ <strong>|s|*N</strong> ≤ 10<sup>6</sup></span></div>

<p>&nbsp;</p>
</div>