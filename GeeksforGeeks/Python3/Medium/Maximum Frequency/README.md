# Maximum Frequency
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an interger array <strong>arr[]&nbsp;</strong>of size <strong>n</strong>&nbsp;and an interger <strong>k</strong>.In one operation,&nbsp;you can&nbsp;choose an index <strong>i</strong> where 0<u>&lt;</u>i Return the <strong>maximum frequency</strong> of an element after using <strong>atmost</strong> k <strong>Increment&nbsp;</strong>operations.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n=3
arr[] = {2,2,4},k=4
<strong>Output:</strong> 3
<strong>Explanation</strong>: Apply two operations on index 0 and two operations
on index 1 to make arr[]={4,4,4}.Frequency of 4 is 3.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n=4
arr[] = {7,7,7,7},k=5
<strong>Output:</strong> 4
<strong>Explanation</strong>: It is optimal to not use any operation.
Frequency of 7 is 4.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>max</strong><strong>Frequency()&nbsp;</strong>which takes the array arr[] ,interger n &nbsp;and integer&nbsp; k as input and returns the maximum frequency of an element.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(nlogn).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(1).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n,k&nbsp;≤ 10<sup>5</sup><br>
1 ≤ arr[i]&nbsp;≤ 10<sup>6</sup></span></p>
</div>