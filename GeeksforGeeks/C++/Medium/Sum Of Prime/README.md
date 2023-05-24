# Sum Of Prime
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a number <strong>N</strong>,&nbsp; find if&nbsp;<strong>N&nbsp;</strong>can be expressed as&nbsp;<strong>a + b&nbsp;</strong>&nbsp;such that <strong>a</strong> and <strong>b</strong> are prime.<br>
<strong>Note: </strong>If [a, b] is one solution with a &lt;= b, and [c, d] is another solution with c &lt;= d, and a &lt; c then&nbsp; [a, b] is considered as our answer.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<span style="font-size:18px"><strong>N = </strong>8</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">3 5</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">3 and 5 are both prime and they
add up to 8.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<span style="font-size:18px"><strong>N = </strong>3</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">-1 -1</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">There are no solutions to the number 3.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>getPrimes()</strong> which takes an integer <strong>n</strong> as input and <strong>returns</strong> (a,b) as an array of size 2.&nbsp;<br>
<strong>Note: </strong>If no value of (a,b) satisfy the condition return (-1,-1) as an array of size 2.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N*loglog(N))<br>
<strong>Expected Auxiliary Space:</strong> O(N)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong></span><br>
<span style="font-size:18px">2 &lt;= N &lt;= 10<sup>6</sup></span></p>
</div>