# Last Match
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two strings A and B, you need to find the last&nbsp;occurrence ( 1 based indexing) of string B in string A.</span></p>

<p><span style="font-size:18px">&nbsp;</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
A = abcdefghijklghifghsd
B = ghi
<strong>Output:</strong>
13<span style="font-size:20px">
</span><strong>Explanation:</strong>
ghi occurs at position 13 for the
last time in string A.
</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
A = abdbccaeab
B = abc</span><span style="font-size:18px">
<strong>Output:</strong>
-1
<strong>Explanation:</strong></span>
<span style="font-size:18px">abc is not a substring of A</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function<strong> findLastOccurence() </strong>which takes two strings A and B&nbsp;as input parameters and returns the position of the last occurrence of B in A. If B&nbsp;is not present in A, return -1.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(len(A))<br>
<strong>Expected Space Complexity:</strong> O(len(A))</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constarints:</strong><br>
1&lt;=T&lt;=100<br>
1&lt;=len(B)&lt;=10<sup>5</sup><br>
1&lt;=len(A)&lt;=10<sup>6</sup><br>
len(A)&gt;=len(B)</span><br>
&nbsp;</p>
</div>