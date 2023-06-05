# Valid Pair Sum
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array of size <strong>N</strong>, find the number of distinct pairs <strong>{i, j} (i != j)</strong>&nbsp;in the array such that the sum of <strong>a[i]</strong> and <strong>a[j]</strong> is greater than 0.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 3, a[] = {3, -2, 1}</span>
<span style="font-size:18px"><strong>Output:</strong> 2</span>
<span style="font-size:18px"><strong>Explanation:</strong> {3, -2}, {3, 1} are two 
possible pairs.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 4, a[] = {-1, -1, -1, 0}</span>
<span style="font-size:18px"><strong>Output:</strong> 0
<strong>Explanation:</strong> There are no possible pairs.</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task: </strong>&nbsp;<br>
You don't need to read input or print anything. Complete the function <strong>ValidPair()</strong> which takes the array<strong> a[ ] </strong>and size of array <strong>N</strong> as input parameters and returns the count of such pairs.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N * Log(N))<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5</sup>&nbsp;<br>
-10<sup>4</sup>&nbsp; ≤ a[i] ≤ 10<sup>4</sup></span></p>
</div>