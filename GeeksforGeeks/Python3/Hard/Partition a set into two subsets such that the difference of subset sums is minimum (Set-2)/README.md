# Partition a set into two subsets such that the difference of subset sums is minimum (Set-2)
## Hard
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a set of n integers, divide the set in two subsets, S1 and S2, of n/2 sizes each such that the difference of the sum of two subsets is as minimum as possible. The task is to print that two subset S1 and S2. Elements in S1 and S2 should be present in same format as given in input.</span></p>

<p><span style="font-size:18px"><strong>Note:</strong>&nbsp;</span></p>

<ol>
	<li><span style="font-size:18px">If n is even, then sizes of two subsets must be strictly n/2 </span></li>
	<li><span style="font-size:18px">if n is odd, then size of one subset must be (n-1)/2 and size of other subset must be (n+1)/2.</span></li>
	<li><span style="font-size:18px">n is&nbsp;strictly greater than 1.</span></li>
	<li><span style="font-size:18px">Minimum <strong>Diff = abs(s1-s2)</strong>, where s1&gt;s2.</span></li>
</ol>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> 
arr[] = {3, 4, 5, -3, 100, 
         1, 89, 54, 23, 20}
<strong>Output: </strong>
148 148
<strong>Explanation:</strong>  Both output subsets 
are of size 5 and sum of elements in 
both subsets is same (148 and 148).
So the minimum difference will be 0.</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> 
arr[] = {13, -17, 6, 48, -44, -14}
<strong>Output:
</strong>-10 2
<strong>Explanation:</strong> The sums of elements in 
two subsets are -10 and 2 respectively.
So the minimum difference will be (2-(-10))
=12.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Complete the function&nbsp;<strong><code>minDifference</code>()&nbsp;</strong>which takes&nbsp;<strong>N</strong>&nbsp;and array&nbsp;<strong>arr&nbsp;</strong>as input parameters and returns the array which incudes sum of each sub-arrays.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(2^N)<br>
<strong>Expected Space Complexity:&nbsp;</strong>O(2*N)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
2 &lt;= N &lt;= 20<br>
-10000 &lt;= arr[i] &lt;= 10000</span></p>
</div>