# Longest common substring value of two numbers
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two integers N and M. Find the longest common contiguous subset in binary representation of both the numbers and print its decimal value.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 10, M = 11
<strong>Output:</strong> 5
<strong>Explanation</strong>: 10 in Binary is "1010" and
11 in Binary is "1011". The longest common
contiguous subset is "101" which has a
decimal value of 5.</span>
</pre>

<p><span style="font-size:18px">â€‹<strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: N = 8, M = 16
<strong>Output:</strong> 8
<strong>Explanation</strong>: 8 in Binary is "1000" and
16 in Binary is "10000". The longest common
contiguous subset is "1000" which has a
decimal value of 8.
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>longestCommon()&nbsp;</strong>which takes two integers N and M as inputs and returns the Decimal representation of the longest common contiguous subset&nbsp;in the Binary representation of N and M.<br>
<strong>Note</strong>: If there's a tie in the length of the longest common contiguous subset, return the one with the highest decimal value among them.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O((log(max (N, M))<sup>3</sup>).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O((log(max (N, M))<sup>2</sup>).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt;=N,M&lt;=10<sup>18</sup></span></p>

<p>&nbsp;</p>
</div>