# Number of pairs
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two arrays <strong>X</strong> and <strong>Y</strong> of positive integers, find the number of pairs such that&nbsp;<strong>x<sup>y</sup> &gt; y<sup>x</sup></strong>&nbsp;<strong>(raised to power of)</strong> where x is an element from X and y is an element from Y.</span><br>
<br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: 
M = 3, X[] = [2 1 6] 
N = 2, Y[] = [1 5]
<strong>Output</strong>: 3
<strong>Explanation</strong>: 
The pairs which follow x<sup>y</sup> &gt; y<sup>x</sup> are 
as such: 2<sup>1</sup> &gt; 1<sup>2</sup>,&nbsp; 2<sup>5</sup> &gt; 5<sup>2</sup> and 6<sup>1</sup> &gt; 1<sup>6 .</sup></span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: 
M = 4, X[] = [2 3 4 5]
N = 3, Y[] = [1 2 3]
<strong>Output</strong>: 5
<strong>Explanation</strong>: 
The pairs for the given input are 
2<sup>1 </sup>&gt; 1<sup>2</sup> , 3<sup>1</sup> &gt; 1<sup>3 </sup>, 3<sup>2</sup> &gt; 2<sup>3</sup> , 4<sup>1</sup> &gt; 1<sup>4</sup> , 
5<sup>1</sup> &gt; 1<sup>5&nbsp;</sup>.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. You only need to complete the function<strong> countPairs()&nbsp;</strong>that takes <strong>X, Y, M, N</strong> as <strong>parameters </strong>and returns the total number of pairs.</span><br>
<br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O((N + M)log(N)).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1).</span><br>
<br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ M, N ≤ 10<sup>5</sup><br>
1 ≤ X[i], Y[i]&nbsp;≤ 10<sup>3</sup></span></p>
</div>