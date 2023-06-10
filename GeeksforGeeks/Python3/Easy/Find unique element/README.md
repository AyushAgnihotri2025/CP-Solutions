# Find unique element
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:20px"><span style="font-family:arial,helvetica,sans-serif">Given an array of size n which contains all elements occurring in multiples of&nbsp;<strong>K</strong>, except one element which doesn't occur in multiple of <strong>K</strong>. Find that unique element.</span></span><br>
&nbsp;</p>

<p><span style="font-size:20px"><span style="font-family:arial,helvetica,sans-serif"><strong>Example 1:</strong></span></span></p>

<pre><span style="font-size:20px"><span style="font-family:arial,helvetica,sans-serif"><strong>Input : 
</strong>n = 7, k = 3
arr[] = {6, 2, 5, 2, 2, 6, 6}
<strong>Output : </strong>
5
<strong>Explanation:</strong>
Every element appears 3 times except 5.</span></span></pre>

<p>&nbsp;</p>

<p><span style="font-size:20px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:20px"><span style="font-family:arial,helvetica,sans-serif"><strong>Input  : 
</strong>n = 5, k = 4
arr[] = {2, 2, 2, 10, 2}
<strong>Output :
</strong>10
<strong>Explanation:</strong>
Every element appears 4 times except 10.</span></span></pre>

<p>&nbsp;</p>

<p><span style="font-size:20px"><span style="font-family:arial,helvetica,sans-serif"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>findUnique()</strong>&nbsp;which takes the array <strong>A[]</strong>, its size <strong>N</strong><strong> </strong>and an integer<strong> K</strong> as inputs and returns the element with single occurence.</span></span></p>

<p>&nbsp;</p>

<p><span style="font-size:20px"><span style="font-family:arial,helvetica,sans-serif"><strong>Expected Time Complexity:</strong> O(N. Log(A[i]) )<br>
<strong>Expected Auxiliary Space:</strong> O( Log(A[i]) )</span></span></p>

<p>&nbsp;</p>

<p><span style="font-size:20px"><span style="font-family:arial,helvetica,sans-serif"><strong>Constraints:</strong><br>
3&lt;= N&lt;=2*10<sup>5</sup><br>
2&lt;= K&lt;=2*10<sup>5</sup><br>
1&lt;= A[i]&lt;=10<sup>9</sup></span></span></p>
</div>