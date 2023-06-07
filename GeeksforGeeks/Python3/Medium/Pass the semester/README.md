# Pass the semester
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Satish wants to prepare for tomorrow's exam. He knows the distribution of marks for the subject along with time to learn the concepts.<br>
You are given the remaining time for the exam along with marks for each topic and passing marks for the subject.<br>
Find the max marks Satish can attain by studying max no of the topic in max no hours not exceeding <strong>(p)</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input :</strong> arr[ ] = {{12, 10},{16, 10},
         {20, 10},{24, 10},{8, 3}}
        N = 5, W = 40, P = 21
<strong>Output :</strong> YES 36
<strong>Explanation:</strong> Marks needed to pass the subject  
10 + 10 + 3 = 23 Time taken to achieve the 23 
marks : 12 + 6 + 8 =36 So, return 36.
</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input :</strong> arr[ ] = {{1, 3}, {5, 10}, {3, 12}}
&nbsp;        N = 3, W = 9, P = 10  <strong>
Output :</strong>  YES 9</span></pre>

<p><br>
<br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong>Ispossible()</strong> that takes a 2-d array <strong>(arr)</strong>, sizeOfArray <strong>(n), </strong>time<strong>&nbsp;</strong>remaining for exam&nbsp;<strong>W, </strong>Passing Marks<strong> P,</strong>&nbsp;and return maximum time taken If it is not possible then return <strong>-1</strong>. The driver code takes care of the printing.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N*W).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N*W).</span></p>

<p>&nbsp;</p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong></span></p>

<p><span style="font-size:18px">1 ≤ N ≤ 1000</span></p>

<p><span style="font-size:18px">1 ≤ W ≤ 1000</span></p>

<p><span style="font-size:18px">1 ≤ P ≤ 100</span></p>

<p><span style="font-size:18px">1 ≤ U,V ≤ 25</span></p>
</div>