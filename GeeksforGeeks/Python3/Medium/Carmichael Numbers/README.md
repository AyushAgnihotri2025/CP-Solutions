# Carmichael Numbers
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">A number n is said to be a Carmichael number if it satisfies the following modular arithmetic condition:</span></p>

<pre><span style="font-size:18px">  power(b, n-1) MOD n = 1, 
  for all b ranging from 1 to n such that b and 
  n are relatively prime, i.e, gcd(b, n) = 1 </span></pre>

<p><span style="font-size:18px">Given a positive integer n, find if it is a Carmichael number.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> n = 8
<strong>Output:</strong> 0
<strong>Explaination:</strong> 3 is relatively prime to 
8 but 3<sup>(8 - 1)</sup>%8 = 2187%8 != 1</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> n = 3
<strong>Output:</strong> 1
<strong>Explaination:</strong> For both 1 and 2 the 
condition satisfied.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function<strong> isCarmichael()</strong> which takes n as input parameter and returns 1 if it is a carmichael number. Otherwise, returns 0.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(n*Logn)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n ≤ 100000</span></p>
</div>