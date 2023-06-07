# Combination Sum II
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array of integers <strong>arr, </strong>length of the array &nbsp;<strong>N,&nbsp;</strong>and&nbsp;an integer <strong>K</strong>, find all the unique combinations in arr where the sum of the combination is equal to <strong>K</strong>. Each number can only be used once in a combination.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> </span>
<span style="font-size:18px">N = 5, K = 7</span>
<span style="font-size:18px">arr[] = { 1, 2, 3, 3, 5 }</span>
<strong><span style="font-size:18px">Output:</span></strong>
<span style="font-size:18px">{ { 1, 3, 3 }, { 2, 5 } }</span>
<strong><span style="font-size:18px">Explanation:</span></strong>
<span style="font-size:18px">1 + 3 + 3 = 7</span>
<span style="font-size:18px">2 + 5 = 7</span></pre>

<p><span style="font-size:18px">Example 2:</span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<span style="font-size:18px">N = 6, K = 35</span>
<span style="font-size:18px">arr[] = { 5, 10, 15, 20, 25, 30 }</span>
<strong><span style="font-size:18px">Output:</span></strong>
<span style="font-size:18px">{ { 5,10, 20 }, { 5, 30 }, { 10, 25 }, { 15, 20 } }</span>
<strong><span style="font-size:18px">Explanation:</span></strong>
<span style="font-size:18px">5 + 10 + 20 = 35</span>
<span style="font-size:18px">5 + 30 = 35</span>
<span style="font-size:18px">10 + 25 = 35</span>
<span style="font-size:18px">15 + 20 = 35</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>CombinationSum2()</strong> which takes arr[],n, and k as input parameters and returns all the unique combinations.</span><br>
&nbsp;</p>

<p><strong><span style="font-size:18px">Constraints:</span></strong><br>
<span style="font-size:18px">1 &lt;= N &lt;= 100<br>
1 &lt;= arr[i] &lt;= 50<br>
1 &lt;= K &lt;= 30</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(K * 2<sup>N</sup>)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N)</span></p>
</div>