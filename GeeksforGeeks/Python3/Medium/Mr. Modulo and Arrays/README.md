# Mr. Modulo and Arrays
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Mr. Modulo lives up to his name and is always busy taking&nbsp;modulo of numbers and making&nbsp;new problems.<br>
Now he comes up with another problem. He has an array of integers with <strong>n</strong>&nbsp;elements and wants to find a pair of elements <strong>{arr[i], arr[j]} </strong>such that&nbsp;<strong>arr[i] ≥ arr[j]</strong> and&nbsp;<strong>arr[i] % arr[j]</strong> is&nbsp;maximum among all possible pairs where&nbsp;<strong>1 ≤ i, j ≤ n.</strong><br>
Mr. Modulo needs some help to solve this problem. Help him to find this maximum value&nbsp;<strong>arr[i] % arr[j]</strong>.&nbsp;</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n=3
arr[] = {3, 4, 7} 
<strong>Output:</strong> 3
<strong>Explanation</strong>: There are 3 pairs which satisfies 
&nbsp;            arr[i] &gt;= arr[j] are:-
             4, 3 =&gt; 4 % 3 = 1
             7, 3 =&gt; 7 % 3 = 1
             7, 4 =&gt; 7 % 4 = 3
             Hence maximum value among all is 3.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n=4
arr[] = {4, 4, 4, 4} 
<strong>Output:</strong> 0
</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong>maxModValue</strong>() that takes <strong>array arr and n</strong> as parameters and return the&nbsp;required answer.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(nLog(n) + Mlog(M)) n&nbsp;is total number of elements and M is maximum value of all the elements.<br>
<strong>Expected Auxiliary Space:</strong> O(1).</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n&nbsp;≤ 10<sup>5</sup></span></p>

<p><span style="font-size:18px">1 ≤ arr[i]&nbsp;≤ 10<sup>5</sup></span></p>
</div>