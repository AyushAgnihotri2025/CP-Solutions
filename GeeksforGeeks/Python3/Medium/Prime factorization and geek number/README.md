# Prime factorization and geek number
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">As we know that every number &gt;=2 can be represented as natural powers of primes(prime factorization). Also <a href="https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic" target="_blank">prime factorization is unique for a number</a>.&nbsp;</span></p>

<p><span style="font-size:18px">Eg. 360 = 2<sup>3</sup>3<sup>2</sup>5<sup>1</sup></span></p>

<p><span style="font-size:18px">Today we are interested in <strong>geek</strong> numbers.&nbsp;A <strong>geek</strong> number is a number whose prime factorization only contains powers of unity.Below are some geek numbers.</span></p>

<p><span style="font-size:18px">Eg. 2 = 2<sup>1</sup><br>
&nbsp; &nbsp; 22 = 2<sup>1</sup>11<sup>1</sup></span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> N = 22
<strong>Output:</strong> Yes
<strong>Explaination:</strong> 22 = 2<sup>1</sup>11<sup>1</sup>. Where all the 
powers of prime numbers are one.</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> N = 4
<strong>Output:</strong> No
<strong>Explaination:</strong> 4 = 2<sup>2</sup>. Where all the 
powers of all the prime are not one.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function <strong>geekNumber()</strong> which takes N as input parameter and returns 1 if it a geek number. Otherwise, returns 0.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(sqrt(N))<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>6</sup>&nbsp;&nbsp;</span></p>
</div>