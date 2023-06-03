# Print the Sequence
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Construct the sequence arr[1], arr[2], ... by the following rules. For i=1 we put arr[1]=1. Now let i &gt;= 2. Then arr[i] is the least positive integer such that the following two conditions hold<br>
(i) arr[i] &gt; arr[i - 1];<br>
(ii) for all k, j &lt; i we have arr[i] is not equal to n1 * arr[k] - n2 * arr[j].<br>
Find the first <strong>n</strong> terms of this sequence.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>:</span>
<span style="font-size:18px"><strong>n1 = </strong>2, <strong>n2</strong> <strong>= </strong>1, <strong>n = </strong>10</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">1 2 4 5 10 11 13 14 28 29</span> 
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">The first 10 terms of the sequence is printed.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>:</span>
<span style="font-size:18px"><strong>n1 = </strong>1, <strong>n2</strong> <strong>= </strong>1, <strong>n = </strong>5</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">1 2 3 4 5</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">The first 5 terms of the sequence is printed.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>findSeq()</strong> which takes 3 Integers n1, n2, and n as input and returns a vector denoting the first n terms of the sequence.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(n<sup>2</sup>)<br>
<strong>Expected Auxiliary Space:</strong> O(n<sup>2</sup>)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt;= n1,n2 &lt;= 50</span><br>
<span style="font-size:18px">1 &lt;= n &lt;= 10<sup>3</sup></span></p>
</div>