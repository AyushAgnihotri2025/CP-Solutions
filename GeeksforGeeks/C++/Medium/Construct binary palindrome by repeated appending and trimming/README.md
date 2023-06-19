# Construct binary palindrome by repeated appending and trimming
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given <strong>n</strong> and<strong> k</strong>, Construct a palindrome of size <strong>n</strong> using the&nbsp;binary representation of the number <strong>k</strong>.To construct the&nbsp;palindrome&nbsp;you can use the binary number of size&nbsp;<strong>k</strong> as many times as you wish and also you can trim all&nbsp;the&nbsp;&nbsp;zeros&nbsp;from the end.<strong>The palindrome must always begin with 1 and contains the maximum number of zeros.</strong></span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1 :</strong></span></p>

<pre><span style="font-size:18px"><strong>Input :</strong> n = 5, k = 6
<strong>Output :</strong> 11011
<strong>Explanation:</strong> Binary representation of 6 is
110.After combining 110
twice and trimming the extra 0 in 
the end we get 11011</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>n = 5, k = 8
<strong>Output: </strong>10001</span>
<span style="font-size:18px"><strong>Explanation:</strong> Binary representation of 8 is
1000.After combining 1000 twice and trimming
the extra 0 in the end we get 10001.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anything. Your task is to complete the function <strong>binaryPalindrome()</strong> that takes two integers<strong> n,</strong>&nbsp;<strong>k</strong>&nbsp;and return a string of size n.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(n).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1).</span><br>
<br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n&nbsp;≤ 10<sup>5</sup><br>
1 ≤ k&nbsp;≤ 10<sup>5</sup></span></p>
</div>