# Techfest and the Queue
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given n, a, b find out the sum of the power of primes that occur in&nbsp;prime factorization of the numbers between a to b(inclusive).</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>n = 14, a = 9, b = 12
<strong>Output: </strong>8
<strong>Explanation: </strong>For p=9, prime factorization 
is:3<sup>2</sup>&nbsp;So, sum of the powers of primes is: 2
For p=10, prime factorization is : 2<sup>1</sup>x5<sup>1</sup>&nbsp;
So, sum of the powers of primes is: 2
For p=11, prime factorization is : 11<sup>1</sup>&nbsp;
So, sum of the powers of primes is: 1
For p=12, prime factorization is : 2<sup>2</sup>x 3<sup>1</sup>&nbsp;
So, sum of powers of primes is: 3
Therefore the total sum is 2+2+1+3=8.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anyhting. Your task is to complete the function&nbsp;<strong>Sum()&nbsp;</strong>which takes n, a and b as input parameter and returns the sum of power of primes&nbsp;that occur in prime prime factorization of the numbers between a to b(inclusive).</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Compelxity:&nbsp;</strong>O(k*logk) where k = b-a<br>
<strong>Expected Space Comeplxity:&nbsp;</strong>O(k*logk)</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= a &lt;= b &lt;= n &lt;= 10<sup>12</sup><br>
1 &lt;= b-a &lt;= 10<sup>5</sup></span></p>
</div>