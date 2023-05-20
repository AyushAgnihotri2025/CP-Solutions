# Count of AP Subsequences
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>A</strong>&nbsp;of&nbsp;<strong>N</strong> positive integers. The task is to count the number of Arithmetic Progression subsequence in the array.</span></p>

<p><span style="font-size:18px"><strong>Note:</strong> Empty sequence or single element sequence is Arithmetic Progression.&nbsp;</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input :</strong> 
N = 3
A[] = { 1, 2, 3 }
<strong>Output : </strong>
8
<strong>Explanation:</strong>
Arithmetic Progression subsequence from the 
given array are: {}, { 1 }, { 2 }, { 3 }, { 1, 2 },
{ 2, 3 }, { 1, 3 }, { 1, 2, 3 }.
</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input :
</strong>N = 3
A[] = { 10, 20, 30,} <strong>
Output :</strong>
8
<strong>Explanation:</strong> 
Arithmetic Progression subsequence 
from the given array are: {}, { 10 }, 
{ 20 }, { 30 }, { 10, 20 }, { 20, 30 }, 
{ 10, 30 }, { 10, 20, 30 }.</span></pre>

<p><br>
<strong><span style="font-size:18px">Your Task:</span></strong><br>
<span style="font-size:18px">You don't need to read input or print anything. Your task is to complete the function <strong>count()</strong>&nbsp;which takes an integer <strong>N </strong>and<strong>&nbsp;</strong>an array <strong>A</strong>&nbsp;as input parameters and returns the total count of AP sub-sequences in the array.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N * (Minimum value in A - Maximum Value in A))&nbsp;<br>
<strong>Expected Space Complexity:</strong> O(N)<br>
<br>
<strong>Constraints:</strong><br>
1&lt;= N &lt;=100<br>
1&lt;= A[i] &lt;=100</span></p>
</div>