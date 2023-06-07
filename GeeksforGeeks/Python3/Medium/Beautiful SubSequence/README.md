# Beautiful SubSequence
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Nowadays Babul is solving problems on sub-sequence. He is struck with a problem in which he has to find the longest sub-sequence in an array A of size&nbsp; N&nbsp;such that for all (i,j) where </span><span style="font-size:18px">i</span><span style="font-size:18px">!=j either A[i] divides A[j] or vice versa. If no such sub-sequence exists then print -1. Help him to accomplish this task.</span></p>

<p><span style="font-size:20px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:20px"><strong>â€‹</strong><strong>Input :</strong> arr[ ] = {5, 3, 1, 4, 7</span><span style="font-size:20px">}
<strong>Output :</strong> 2
<strong>Explanation:</strong>
Longest Sub Sequence are {5,1} , {4,1}, 
{3,1} etc. So, size is 2.</span><span style="font-size:20px">

</span></pre>

<p><span style="font-size:20px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:20px"><strong>Input :</strong> arr[ ] = {2, 4, 6, 1, 3, 11</span><span style="font-size:20px">} <strong>
Output :</strong> 3 </span></pre>

<p><br>
<br>
<span style="font-size:20px"><strong>Your Task:</strong><br>
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong>longest_Subsequence()</strong> that takes an array <strong>(arr)</strong>, sizeOfArray <strong>(n)</strong>, and return the length of the longest subsequence of&nbsp;the array. The driver code takes care of the printing.</span></p>

<p><span style="font-size:20px"><strong>Expected Time Complexity:</strong>&nbsp;O(N<sup>2</sup>).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints : </strong><br>
2 ≤ N ≤ 2000<br>
1 ≤ A[i] ≤ 10<sup>5</sup></span></p>
</div>