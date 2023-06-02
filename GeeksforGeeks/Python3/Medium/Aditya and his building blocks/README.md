# Aditya and his building blocks
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Aditya has arranged some of his building blocks in N columns. Each column has a certain number of blocks given by an array A.<br>
Each element of A(i.e. Ai) is the height of the ith column. Aditya now has M blocks left. He doesn't like small columns.<br>
So he wants to maximize the minimum of all heights. He may or may not use all of the M blocks.<br>
Determine the maximized height.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>â€‹Input :</strong> arr[ ] = {1, 2, 3, 4, 5} and M = 6 
<strong>Output :</strong> 4
<strong>Explanation:</strong>
Final heights of blocks - 4 4 4 4 5
</span></pre>

<p><br>
<span style="font-size:18px"><strong>â€‹Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input :</strong> arr[ ] = {2, 8, 9} and M = 4 <strong>
Output :</strong>  6
<strong>Explanation:
</strong>Final heights of blocks - 6 8 9 
</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong>maximised_height()</strong> that takes an array <strong>(arr)</strong>, sizeOfArray <strong>(n)</strong>, an integer <strong>M</strong>&nbsp;and return the maximized height. The driver code takes care of the printing.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N*LOG(N)).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1).</span></p>

<p>&nbsp;</p>

<p><br>
<span style="font-size:18px"><strong>Output :</strong>&nbsp;<br>
For each test case, print the required answer in a new line.</span></p>

<p><span style="font-size:18px"><strong>Constraints :</strong><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ M ≤ 10<sup>4</sup><br>
1 ≤ Ai ≤ 10<sup>4</sup></span></p>
</div>